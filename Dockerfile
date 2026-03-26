# Utilisation d'une image Python très légère (Alpine)
FROM python:3.11-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier le script Python dans le conteneur
COPY wake.py /app/

# Définir un utilisateur non-root pour des raisons de sécurité
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Variables d'environnement par défaut (peuvent être surchargées au runtime)
# Exemple: docker run -e MAC_ADDRESS="C8:7F:54:05:E1:09" -e TARGET_IP="176.186.167.152" -e TARGET_PORT=7 mon-image-wol
ENV MAC_ADDRESS=""
ENV TARGET_IP="255.255.255.255"
ENV TARGET_PORT=9

# Commande à exécuter lorsque le conteneur démarre
CMD ["python", "wake.py"]
