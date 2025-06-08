# Installation and Setup Instructions for Plesk and Tutor.

## update the server

```
sudo apt update
sudo apt upgrade -y
```

## install and setup plesk (from official documentation) [takes up to 20min]

```
https://docs.plesk.com/en-US/obsidian/deployment-guide/plesk-installation-and-upgrade-on-single-server/1click-plesk-installation/installing-plesk-for-linux-in-one-click.76444/
```

open the link displayed and provide the required information: (admin) email, password, TODO: describe this step in more depth

overwrite the temprary plesk URL with `plesk.humanityfirst-academy.com` under `Tools&Settings` > `Full hostname`

and add the following DNS record: `A plesk 165.22.82.171 DNS only Auto`

now add the domain `humenityfirst-academy.com` under `Domains` and add a SSL/TSL certificate under `SSL/TSL certificates`

additionally add this DNS record: `A <@ for root> 165.22.82.171 DNS only Auto`. Make sure to choose securing www. and all subdomains. Note: direct access to DNS provider will be needed.

## install Docker and Docker-compose (following the official documentation)

note that `VERSION_STRING` specifies the version of docker that will be installed. To see newest Docker Releases run `apt-cache madison docker-ce | awk '{ print $3 }'`.

```
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
 $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
 sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

VERSION_STRING=5:28.1.1-1~ubuntu.24.04~noble
sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin -y
```

## create new user named academy

note that `yourpassword` is a placeholder

```
sudo adduser --disabled-password --gecos "" academy
echo "academy:yourpassword" | sudo chpasswd
sudo usermod -aG sudo academy
sudo usermod -aG docker academy
```

## verify if docker and docker-compose was installed successfully and the new created user can execute docker

```
docker --version
docker-compose --version
docker run hello-world
```

## install python, tutor and other dependencies

note if a newer version of tutor is required, adjust the version number below. All releases are listed here [Tutor Releases](https://github.com/overhangio/tutor/releases)

```
sudo apt install python3 python3-pip libyaml-dev -y
sudo apt install python3-venv -y
python3 -m venv .venv
source .venv/bin/activate
pip install "tutor[full]==19.0.2"
```

## setup port 81 for tutor

Go to firewall settings in plesk (install firewall plugin beforehand) and add a new rule: `Incoming` > `Allow` > `TCP` > `81`

```
tutor config save --set ENABLE_WEB_PROXY=false --set CADDY_HTTP_PORT=81
```

## run tutor [takes up to 10min]

run `tutor local launch` and configure it as following: Yes, provide domain name, enter (default chosen),Humanityfirst Academy, enter (default chosen), en, yes

setup access to openEdx application

in plesk create a new domain called learn.humanityfirst-academy.com. Make sure to choose securing www. and all subdomains.

add following DNS records: `A learn 165.22.82.171 DNS only Auto` and `CNAME *.learn learn.humanityfirst-academy DNS only Auto`.

under `hosting & dns` > `apache` add following config to both (http & htpps) apache configs

```
ProxyPreserveHost On
ProxyPass / http://127.0.0.1:81/
ProxyPassReverse / http://127.0.0.1:81/
```

## verify everything

now the openEdx application should be accessible over TODO add url
