from xml.etree.ElementTree import tostring

from scapy.all import *
from fonctionsSeparationSelonProtocoleEthernet import *
from datetime import datetime
#Cette fonction permert d'ajouter les informations d'un paquet ARP dans la liste PCAPARP


#Créer des couple clé valeur : protocoles ethernet, paquets associés
def ajouterATableParProtocole( table, paquet):
    keyExist = False
    EtherType = paquet[Ether].payload.name


    for key in table.keys() :
        if key == EtherType :
            table[EtherType].append(extraireInfo(paquet))
            keyExist = True
    if not keyExist :
        table[EtherType] = []
        table[EtherType].append(extraireInfo(paquet))
    
    return table

# l'appel paquet.proto renvoi un int qui est lié à un protocole de la couche 4,
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

#l'appel paquet.ptype renvoi un int qui est lié à un protocole de la couche 3,
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


def extraireInfo(paquet) : 
    #On ajoute d'abords les informations communes à tout les paquets
    Infos = {
        # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
        'time': datetime.fromtimestamp(float(paquet.time)),
        'mac_src': paquet[Ether].src,
        'mac_dst': paquet[Ether].dst
    }

    etherType = paquet[Ether].payload.name

    #Dans cette section on vas avoir des types d'informations différents selon le type de payload du paquet ethernet
    if paquet.haslayer('IP') :
        Infos['protocole IP'] = get_proto_name(paquet[IP].proto)
        Infos['ttl'] = paquet[IP].ttl
        Infos['source'] = paquet[IP].src
        Infos['destination'] = paquet[IP].dst
        Infos['ni IP ni ARP'] = False
    elif paquet.haslayer('ARP') : 
        Infos['protocole ARP'] = get_arp_proto_name(paquet[ARP].ptype)
        Infos['source'] = paquet[ARP].psrc
        Infos['destination'] = paquet[ARP].pdst
        Infos['ni IP ni ARP'] = False
    else :
        Infos['ni IP ni ARP'] = True
    return Infos