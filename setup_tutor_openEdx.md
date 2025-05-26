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

sudo usermod -aG docker ${USER}
su - ${USER}

## check

docker run hello-world
docker --version
docker-compose --version

# install Tutor

sudo apt install python3 python3-pip libyaml-dev

sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install "tutor[full]==19.0.2"

## check

tutor --verison

# Firewall installation

sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

## check current UFW Configuration

sudo ufw status

# Manual Installation Steps

echo "run manually: `tutor local launch`"
echo "create an admin user by running: `tutor local do createuser --staff --superuser admin admin@admin.com`"
