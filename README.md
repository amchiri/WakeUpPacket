# Wake-on-LAN Dockerized

Un utilitaire simple pour envoyer des paquets magiques Wake-on-LAN via Docker, entièrement configurable par variables d'environnement.

## 🚀 Utilisation Rapide

1. **Configuration :**
   Copiez le fichier `.env.example` vers `.env` et remplissez l'adresse MAC.
   ```bash
   cp .env.example .env
   ```

2. **Lancement avec Docker Compose :**
   ```bash
   docker-compose up --build
   ```

3. **Lancement avec Docker seul :**
   ```bash
   docker build -t wake-on-lan .
   docker run --rm --network host -e MAC_ADDRESS="XX:XX:XX:XX:XX:XX" wake-on-lan
   ```

## ⚙️ Configuration (Variables d'environnement)

| Variable | Description | Défaut |
|----------|-------------|---------|
| `MAC_ADDRESS` | Adresse MAC de la cible (ex: `C8:7F:54:05:E1:09`) | *Requis* |
| `TARGET_IP` | Adresse IP de destination (Broadcast) | `255.255.255.255` |
| `TARGET_PORT` | Port UDP utilisé | `9` |

## 💡 Notes sur le réseau
Pour que le paquet de diffusion (broadcast) atteigne les machines sur votre réseau local depuis un conteneur, l'utilisation de `--network host` (ou `network_mode: host` dans Compose) est fortement recommandée.
