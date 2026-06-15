FROM nginx:alpine

# Copia todos os arquivos do diretório atual para a pasta padrão do Nginx
COPY . /usr/share/nginx/html

# Expõe a porta 80 que o Nginx usa internamente
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
