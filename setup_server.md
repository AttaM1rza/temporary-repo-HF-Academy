# TODO

- change default ssh port to reduce automated attacks
- install Fail2ban for brute-force protection -> not needed because of Plesk
- are monitoring tools needed ? -> not needed because of Plesk
- can we take snapchots of the current VPS server state ?

# Update server

sudo apt update
sudo apt upgrade -y

# Create a new user and disable root

sudo adduser academy
sudo usermod -aG sudo academy

# TODO disbale root: Kapitel 2: https://www.liquidweb.com/blog/things-to-do-after-installing-a-ubuntu-server/#:~:text=1.,done%20during%20the%20installation%20process.

## after making changes restart SSH

sudo systemctl restart ssh

# Allow SSH

sudo ufw enable
echo 'initial ufw status:'
sudo ufw status
sudo apt install openssh-server
sudo apt install ufw
sudo ufw allow 22/tcp
echo 'status now:'
sudo ufw status

# For vulnerabilities (not needed yet)

### not needed because of Plesk

### sudo apt install lynis

### sudo lynis audit system

# Setup automatic security updates

### not needed because of Plesk

### sudo apt install unattended-upgrades

### sudo dpkg-reconfigure --priority=low unattended-upgrades
