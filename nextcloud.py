import argparse
#from podman import PodmanClient

# ----------------------------------------
# Run this to spin up docker
#
# Need to have the docker data directorys
#     Main application  | docker
#     Added app dir     | docker_app
#     Docker config     | docker_config
#     Docker data dir   | docker_dir
#
#
# Pull the images
# Run the images with the env variables

APP_DESCRIPTION = "This applicaiton manages the running containerized nextcloud "
PODMAN_URI = "unix:///run/user/1000/podman/podman.sock"

def Update_Nextcloud():
    #Actions needed to update the containers
    print("Update_Nextcloud Not implemented yet")

def Start_Nextcloud():
    #Actions needed to start nextcloud
    print("Start_Nextcloud Not implemented yet")

def Stop_Nextcloud():
    #Actions needed to start nextcloud
    print("Stop_Nextcloud Not implemented yet")

def Check_Env():
    # This will check the env to determine if it is OK to run
    print("Check_Env() is not implemented yet")

parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
parser.add_argument('action',choices=['start','stop','update'],metavar='command', type=str,
                    help='start, stop, update')

args = parser.parse_args()

match args.action:
    case 'start':
        Start_Nextcloud()
    case 'stop':
        Stop_Nextcloud()
    case 'update':
        Update_Nextcloud()

#print(args.accumulate(args.integers))


#Older docker-compose based on

#version: '3'

#services:
#
#  nextcloud_db:
#    image: mariadb:latest
#    container_name: nextcloud-mariadb
#    networks:
#      -# nextcloud_network
#    volumes:
#      - nextcloud_db:/var/lib/mysql
#      - /etc/localtime:/etc/localtime:ro
#    environment:
#      - MYSQL_ROOT_PASSWORD=secret
#      - MYSQL_PASSWORD=mysql
#      - MYSQL_DATABASE=nextcloud
#      - MYSQL_USER=nextcloud
#    restart: unless-stopped
#
#  nextcloud:
#    image: nextcloud:latest
#    container_name: nextcloud
#    networks:
#      - nextcloud_network
#    depends_on:
#      - letsencrypt
#      - proxy
#      - nextcloud_db
#    volumes:
#      - nextcloud:/var/www/html
#      - ./app/config:/var/www/html/config
#      - ./app/custom_apps:/var/www/html/custom_apps
#      - ./app/data:/var/www/html/data
#      - ./app/themes:/var/www/html/themes
#      - /etc/localtime:/etc/localtime:ro
#    environment:
#      - VIRTUAL_HOST=nextcloud.theblockweb.com
#      - LETSENCRYPT_HOST=nextcloud.YOUR-DOMAIN
#      - LETSENCRYPT_EMAIL=YOUR-EMAIL
#    restart: unless-stopped
#
#volumes:
#  nextcloud_db:
#  nextcloud:
#  nextcloud_apps:
#  nextcloud_config:
#  nextcloud_data:
#
#networks:
#  nextcloud_network: