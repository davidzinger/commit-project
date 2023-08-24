FROM public.ecr.aws/b4r2w2z1/trafex/php-nginx:latest

# copy logo 
COPY ./COMMIT-Logo-1-scaled.jpg /var/www/html/logo.jpg

#copy content
COPY ./index.php /var/www/html/index.php