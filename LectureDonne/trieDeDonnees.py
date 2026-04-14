import xml.etree.ElementTree  

from scapy.all import *
import datetime  
from datetime import timedelta  
#Cette fonction permet d'ajouter les informations d'un paquet ARP dans la liste PCAPARP



#Créer des couples clé-valeur : type de payload Ethernet, paquets associés

def ajouter_a_table_Par_Protocole(table, paquet,numero_paquet,filtres_actives):
    EtherType = paquet[Ether].payload.name
    #Si le payload en question n'a jamais été trouvé alors on le crée
    if EtherType not in table:
        table[EtherType] = []
    #On ajoute un dictionnaire par paquet

    #Si l'option ip_only est activée, on n'ajoute que les paquets de type IP ou IPv6
    if filtres_actives["ip_only"] and EtherType != 'IP' and EtherType != 'IPv6':
        return table
        
    #Si l'option arp_only est activée, on n'ajoute que les paquets de type ARP
    if filtres_actives["arp_only"] and EtherType != 'ARP' :
        return table
    
    #Si l'option ip_specifique est activée, on n'ajoute que les paquets provenant ou étant déstiné à l'adresse IP spécifiée
    if filtres_actives["ip_specifique"] is not None:
        if EtherType != 'IP' and EtherType != 'ARP' :
            return table
        if EtherType == 'IP' :
            if paquet[IP].src != filtres_actives["ip_specifique"] and paquet[IP].dst != filtres_actives["ip_specifique"]:
                return table
        elif EtherType == 'ARP' :
            if  paquet[ARP].psrc != filtres_actives["ip_specifique"] and paquet[ARP].pdst != filtres_actives["ip_specifique"]:
                return table
        

    table[EtherType].append(extraire_info(paquet, numero_paquet))
    return table

#L'appel paquet.proto renvoie un int qui est lié à un protocole de la couche 4,
# cette fonction permet de faire le lien entre ce numéro et le nom du protocole
def get_proto_name(proto_num):
    proto_map = {
        1: 'ICMP',
        6: 'TCP',
        17: 'UDP',
        41: 'IPv6',
        47: 'GRE',
        50: 'ESP',
        51: 'AH',
        58: 'ICMPv6',
        89: 'OSPF',
        132: 'SCTP'
    }
    for key in proto_map.keys() :
        if key == proto_num :
            return proto_map[proto_num] 
    return 'Unknown'

#L'appel paquet.ptype renvoie un int qui est lié à un protocole de la couche 3,
# cette fonction permet de faire le lien entre ce numéro et le nom du protocole
def get_arp_proto_name(arp_ptype_num):
    arp_proto_map = {
        2048: 'IPv4',
        2054: 'ARP',
        34525: 'IPv6'
    }
    for key in arp_proto_map.keys() :
        if key == arp_ptype_num :
            return arp_proto_map[arp_ptype_num] 
    return 'Unknown'


def extraire_info(paquet,num_paquet) : 
    #On ajoute d'abord les informations communes à tous les paquets
    Infos = {
        'id' : num_paquet,
        #Date sous format AAAA-MM-JJ HH:MM:SS millisecondes
        'time': datetime.datetime.fromtimestamp(float(paquet.time)),
        'mac_src': paquet[Ether].src,
        'mac_dst': paquet[Ether].dst
    }

    etherType = paquet[Ether].payload.name

    #Dans cette section on va avoir des types d'informations différents selon le type de payload du paquet Ethernet
    if paquet.haslayer('IP') :
        Infos['protocole IP'] = get_proto_name(paquet[IP].proto)
        Infos['ttl'] = paquet[IP].ttl
        Infos['source'] = paquet[IP].src
        Infos['destination'] = paquet[IP].dst
        Infos['ni IP ni ARP'] = False
        if paquet.haslayer('TCP') or paquet.haslayer('UDP') or paquet.haslayer('SCTP'):
            Infos['port_src'] = paquet.sport
            Infos['port_dst'] = paquet.dport
    elif paquet.haslayer('ARP') : 
        Infos['protocole ARP'] = get_arp_proto_name(paquet[ARP].ptype)
        Infos['source'] = paquet[ARP].psrc
        Infos['destination'] = paquet[ARP].pdst
        Infos['ni IP ni ARP'] = False
    else :
        #Pour repérer les paquets avec des payloads particuliers
        Infos['ni IP ni ARP'] = True
    return Infos



                      

#Cette fonction prend les dictionnaires de paquets de base 
#Et en fusionne certains entre eux sous certaines conditions : 
#Ne pas être séparé de plus de 'plage_temps' secondes du premier paquet pris en argument
#Avoir la même source et destination
#Ainsi, lorsqu'ils sont fusionnés, une nouvelle paire clé-valeur 'ids_fusionnes'
#apparaît qui liste tous les ids de paquets qui ont été fusionnés
def reunir_paquet_par_temps(table, plage_temps):

    # Si la plage de temps est nulle ou négligeable, on ne trie rien
    if plage_temps is None:
        return table
    if plage_temps <= 0.00001:
        print("ok")
        return table

    #Dans le cas contraire, on commence par transformer le nombre en secondes
    tolerance = timedelta(seconds=plage_temps)

    # On recrée une table avec les mêmes clés mais des listes vides
    nouvelle_table = {cle: [] for cle in table.keys()}

    for cle, donnee in table.items():   # cle = ex "ARP", donnee = liste de paquets
        for paquet in donnee:

            # On ignore les paquets sans source (ni IP ni ARP)
            if paquet.get("ni IP ni ARP", True):
                nouvelle_table[cle].append(dict(paquet))
                continue

            # Cherche un paquet déjà ajouté qui peut être fusionné
            paquet_fusionne = False
            for paquet_existant in nouvelle_table[cle]:

                #Critères de fusion de paquets
                meme_source      = paquet_existant.get("source")      == paquet.get("source")
                meme_destination = paquet_existant.get("destination")  == paquet.get("destination")
                temps_proche     = abs(paquet["time"] - paquet_existant["time"]) <= tolerance

                if meme_source and meme_destination and temps_proche:
                    # Fusion : on garde le time du premier paquet
                    # et on liste les ids fusionnés pour garder une trace
                    if "ids_fusionnes" not in paquet_existant:
                        paquet_existant["ids_fusionnes"] = [paquet_existant["id"]]
                    paquet_existant["ids_fusionnes"].append(paquet["id"])
                    paquet_fusionne = True
                    break

            # Aucun paquet similaire trouvé : on l'ajoute tel quel
            if not paquet_fusionne:
                nouvelle_table[cle].append(dict(paquet))  # dict() = copie indépendante

    return nouvelle_table

