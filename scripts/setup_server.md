# TODO

- change default ssh port to reduce automated attacks
- install Fail2ban for brute-force protection -> not needed because of Plesk
- are monitoring tools needed ? -> not needed because of Plesk
- can we take snapchots of the current VPS server state ?
- while creating the user -> provide a password

# Update server

sudo apt update
sudo apt upgrade -y

# Allow SSH

sudo ufw enable
echo 'initial ufw status:'
sudo ufw status
sudo apt install openssh-server
sudo apt install ufw
sudo ufw allow 22/tcp
echo 'status now:'
sudo ufw status

# Create a new user and disable root

sudo adduser --disabled-password --gecos "" academy
echo "academy:yourpassword" | sudo chpasswd
sudo usermod -aG sudo academy
groups academy

# TODO disbale root: Kapitel 2:

https://www.liquidweb.com/blog/things-to-do-after-installing-a-ubuntu-server/#:~:text=1.,done%20during%20the%20installation%20process.

## after making changes restart SSH

sudo systemctl restart ssh

# For vulnerabilities (not needed yet)

### not needed because of Plesk

### sudo apt install lynis

### sudo lynis audit system

# Setup automatic security updates

### not needed because of Plesk

### sudo apt install unattended-upgrades

### sudo dpkg-reconfigure --priority=low unattended-upgrades
