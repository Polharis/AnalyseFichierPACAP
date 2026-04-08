from scapy.all import *
from fonctionsSeparationSelonProtocoleEthernet import *
from datetime import datetime
#Cette fonction permert d'ajouter les informations d'un paquet ARP dans la liste PCAPARP


def ajoutePaquetARP(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(paquet[ARP].psrc)
    listePaquet[2].append(paquet[ARP].pdst)
    listePaquet[3].append(None) # lorsqu'une information n'est pas présente dans un paquet, je met None
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet IP dans la liste PCAPIPV4
def ajoutePaquetIP(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(paquet[IP].src)
    listePaquet[2].append(paquet[IP].dst)
    listePaquet[3].append(paquet[IP].ttl)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet IPv6 dans la liste PCAPIPV6
def ajoutePaquetIPv6(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(None)
    listePaquet[2].append(None)
    listePaquet[3].append(None)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet IP dans la liste PCAPIPV4
def ajoutePaquetVLAN8021Q (paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(paquet[IP].src)
    listePaquet[2].append(paquet[IP].dst)
    listePaquet[3].append(paquet[IP].ttl)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet MPLS dans la liste PCAPMPLS
def ajoutePaquetMPLS(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(paquet[IP].src)
    listePaquet[2].append(paquet[IP].dst)
    listePaquet[3].append(paquet[IP].ttl)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet LLDP dans la liste PCAPLLDP
def ajoutePaquetLLDP(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(None)
    listePaquet[2].append(None)
    listePaquet[3].append(paquet[LLDPDUTimeToLive].ttl)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet WakeOnLan dans la liste PCAPWakeOnLan
def ajoutePaquetWakeOnLan(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(None)
    listePaquet[2].append(None)
    listePaquet[3].append(None)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))

#Cette fonction permert d'ajouter les informations d'un paquet WakeOnLan dans la liste PCAPWakeOnLan
def ajoutePaquetWakeOnLan(paquet,Nb,listePaquet):
    listePaquet[0].append(Nb)
    listePaquet[1].append(paquet[IP].src)
    listePaquet[2].append(paquet[IP].dst)
    listePaquet[3].append(paquet[IP].ttl)
    listePaquet[4].append(len(paquet))
    # date sous format AAAA-MM-JJ HH:MM:SS milisecondes
    listePaquet[5].append(datetime.fromtimestamp(float(paquet.time)))