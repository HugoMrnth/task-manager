# Frontend statique - serveur HTTP léger
FROM nginx:alpine

RUN addgroup -g 1001 -S nginx && adduser -S -D -H -u 1001 -h /var/cache/nginx -s /sbin/nologin -G nginx -g nginx nginx
USER nginx

# Copier les fichiers statiques
COPY frontend/index.html /usr/share/nginx/html/
COPY frontend/app.js /usr/share/nginx/html/
COPY frontend/styles.css /usr/share/nginx/html/

# Exposer le port 80
EXPOSE 80

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

# Lancer nginx
CMD ["nginx", "-g", "daemon off;"]
