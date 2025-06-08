# TODO

- TODO Momentan sind die Versionen für docker und Tutor hardcoded -> Variablen einführen.
  - [Tutor Releases](https://github.com/overhangio/tutor/releases)
  - To see newest Docker Releases run `apt-cache madison docker-ce | awk '{ print $3 }'`
- TODO The current script uses UFW for configuring Firewalls. But Docker bypasses UFW ... Currently 80 (http) and 443 (https) are open.
- TODO Video Tutorial OpenEdx & Tutor

# Complete Installation

sudo apt update
sudo apt upgrade -y

# install Docker and Docker Compose (following the official documentation)

## Add Docker's official GPG key:

sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

## Add the repository to Apt sources:

echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
 $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
 sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

VERSION_STRING=5:28.1.1-1~ubuntu.24.04~noble
sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin -y

-> create user based on setup_server.md
su academy

sudo usermod -aG docker ${USER}
su - ${USER}

## check

docker run hello-world
docker --version
docker-compose --version

# install Tutor

sudo apt install python3 python3-pip libyaml-dev -y

sudo apt install python3-venv -y
python3 -m venv .venv
source .venv/bin/activate
pip install "tutor[full]==19.0.2"

## check

tutor --version

# Firewall installation

-> DO NOT USE UFW INSTALL THE FIREWALL PLUGIN IN PLESK AND USE IT
GO TO PLESK FIREWALL AND ADD THE PORT TOO AS NEW RULE
Incoming > Allow > TCP > 81

sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

## check current UFW Configuration

sudo ufw status

# overwrite default ports

tutor config save --set ENABLE_WEB_PROXY=false --set CADDY_HTTP_PORT=81

output:
(Configuration saved to /home/academy/.local/share/tutor/config.yml
Environment generated in /home/academy/.local/share/tutor/env)

# Manual Installation Steps

echo "run manually: `tutor local launch`"
echo "create an admin user by running: `tutor local do createuser --staff --superuser admin admin@admin.com`"

# Now point the domains to the correct server port

create a new domain called learn.xxx.domainEnding
-> make sure to choose securing www. and all subdomains.

(under hosting & dns > apache)
add this config to both apache configs:
ProxyPreserveHost On
ProxyPass / http://127.0.0.1:81/
ProxyPassReverse / http://127.0.0.1:81/
