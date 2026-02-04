# Frontend statique - serveur HTTP léger
FROM nginx:alpine

# Copier les fichiers statiques
COPY frontend/index.html /usr/share/nginx/html/
COPY frontend/app.js /usr/share/nginx/html/
COPY frontend/styles.css /usr/share/nginx/html/

# Exposer le port 80
EXPOSE 80

# Lancer nginx
CMD ["nginx", "-g", "daemon off;"]
