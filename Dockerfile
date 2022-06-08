# Version: 0.0.1
FROM ubuntu:20.04
MAINTAINER Joshua "test@123.com"
RUN apt-get update -y && apt-get install -y nginx
RUN echo 'Hi, I am in your container' > /usr/share/nginx/html/index.html
EXPOSE 80
