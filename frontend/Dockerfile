# Frontend statique - serveur HTTP léger
FROM nginx:alpine

# Copier les fichiers statiques
COPY frontend/index.html /usr/share/nginx/html/
COPY frontend/app.js /usr/share/nginx/html/
COPY frontend/styles.css /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

USER nginx

CMD ["nginx", "-g", "daemon off;"]
