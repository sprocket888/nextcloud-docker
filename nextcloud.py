import argparse
import os
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

# File locations for the Nextcloud data and such to be mounted as a volume
# These could become volumes later
NEXTCLOUD_MAIN_PATH="nextcloud"
NEXTCLOUD_APPS_PATH="nextcloud_apps"
NEXTCLOUD_CONFIG_PATH="nexcloud_config"
NEXTCLOUD_DATA_PATH="nextcloud_data"

# Persistant
MARIADB_DATA="mariadb"

# Config data
MARIADB_HOST="mariadb.dns.podman"
MARIADB_DATABASE="owncloud"
MARIADB_USER="owncloud"
MARIADB_PASSWORD="KhE1FwflA0svX"
MARIADB_ROOT_PASSWORD="Lvz1wCwJ8Q38aKe3K8tXMafIIyr47ReR"

def Update_Nextcloud():
    #Actions needed to update the containers
    print("...Pulling the latest containers")
    os.system("podman pull docker.io/library/mariadb:latest")
    os.system("podman pull docker.io/library/nextcloud:latest")

def Start_Nextcloud():
    #Actions needed to start nextcloud
    print("...Starting the database")
    os.system("podman run -d --name mariadb --label mariadb --rm" \
        " -e MARIADB_DATABASE="+MARIADB_DATABASE+"" \
        " -e MARIADB_ROOT_PASSWORD="+MARIADB_ROOT_PASSWORD+"" \
        " -e MARIADB_USER="+MARIADB_USER+"" \
        " -e MARIADB_PASSWORD="+MARIADB_PASSWORD+"" \
        " -v "+MARIADB_DATA+":/var/lib/mysql" \
        " --network nextcloud-net" \
        " -p 3306:3306" \
        " mariadb:latest")

    print("...Starting Nextcloud")
    os.system("podman run -d --name nextcloud --label nextcloud --rm" \
        " -e MYSQL_DATABASE="+MARIADB_DATABASE+"" \
        " -e MYSQL_HOST="+MARIADB_HOST+"" \
        " -e MYSQL_USER="+MARIADB_USER+"" \
        " -e MYSQL_PASSWORD="+MARIADB_PASSWORD+"" \
        " -e NEXTCLOUD_ADMIN_USER=admin" \
        " -e NEXTCLOUD_ADMIN_PASSWORD=password" \
        " -v "+NEXTCLOUD_MAIN_PATH+":/var/www/html" \
        " -v "+NEXTCLOUD_CONFIG_PATH+":/var/www/html/config" \
        " -v "+NEXTCLOUD_APPS_PATH+":/var/www/html/apps" \
        " -v "+NEXTCLOUD_DATA_PATH+":/var/www/html/data" \
        " --network nextcloud-net" \
        " -p 8080:80" \
        " nextcloud:latest")

def Stop_Nextcloud():
    #Actions needed to start nextcloud
    print("...Stopping Nexcloud containers")
    os.system("podman stop mariadb")
    os.system("podman stop nextcloud")

def Check_Env():
    # This will check the env to determine if it is OK to run
    print("Check_Env() is not implemented yet")

parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
parser.add_argument('action',choices=['start','stop','update'],metavar='command', type=str,
                    help='start, stop, update')

args = parser.parse_args()

print(args.action)

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