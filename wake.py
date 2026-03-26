import binascii
import socket
import os
import re
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_mac(mac):
    """Vérifie si l'adresse MAC est dans un format valide."""
    if re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac):
        return True
    return False

def wake_on_lan(mac_address, ip_address='255.255.255.255', port=9):
    """Envoie un paquet magique (Wake-on-LAN) à l'adresse MAC spécifiée."""
    if not validate_mac(mac_address):
        logging.error(f"Format de l'adresse MAC invalide : {mac_address}")
        return False

    try:
        # Nettoyage et conversion de l'adresse MAC en bytes
        clean_mac = mac_address.replace(':', '').replace('-', '')
        mac_bytes = binascii.unhexlify(clean_mac)

        # Création du paquet magique : 6 octets de 0xFF suivis de 16 fois l'adresse MAC
        magic_packet = b'\xff' * 6 + mac_bytes * 16

        # Envoi du paquet magique sur le réseau (Broadcast)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(magic_packet, (ip_address, port))
        
        logging.info(f"Paquet Wake-on-LAN envoyé avec succès à {mac_address} via {ip_address}:{port}")
        return True
    except Exception as e:
        logging.error(f"Échec de l'envoi du paquet Wake-on-LAN : {e}")
        return False

if __name__ == "__main__":
    # Récupération de la configuration depuis les variables d'environnement
    MAC_ADDRESS = os.getenv("MAC_ADDRESS")
    TARGET_IP = os.getenv("TARGET_IP", "255.255.255.255")
    
    # Port par défaut 9 (Wake-on-LAN standard), ou 7 comme dans votre ancien script
    try:
        TARGET_PORT = int(os.getenv("TARGET_PORT", 9))
    except ValueError:
        logging.error("La variable d'environnement TARGET_PORT doit être un nombre entier.")
        exit(1)

    if not MAC_ADDRESS:
        logging.error("La variable d'environnement MAC_ADDRESS n'est pas définie. Veuillez la configurer avant l'exécution.")
        exit(1)

    wake_on_lan(MAC_ADDRESS, TARGET_IP, TARGET_PORT)
