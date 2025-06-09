# TODO

- video tutorial:

  - https://www.youtube.com/watch?v=-NF2xD5zRnc
    - but how to add ssl certs ?
      - https://www.youtube.com/watch?v=__UQNUMxp-0
      - besser: https://www.youtube.com/watch?v=1wy7mVRWQZY

- do this: https://docs.plesk.com/en-US/obsidian/deployment-guide/plesk-installation-and-upgrade-on-single-server/1click-plesk-installation/installing-plesk-for-linux-in-one-click.76444/
- do this: https://docs.plesk.com/en-US/obsidian/deployment-guide/plesk-installation-and-upgrade-on-single-server/plesk-single-server-postinstall-configuration.76454/

- https://www.youtube.com/watch?v=cchU2ThpBOQ

# START ...

sudo apt update
sudo apt upgrade -y

# TODO change root password

# install plesk

https://docs.plesk.com/en-US/obsidian/deployment-guide/plesk-installation-and-upgrade-on-single-server/1click-plesk-installation/installing-plesk-for-linux-in-one-click.76444/

# provide email and new admin password

# add following DNS records:

define a plesk URL under `Tools&Settings` > `Full hostname`
and add the following DNS record: `A plesk 165.22.82.171 DNS only Auto`

Now add a custom Domain under `Domains` and add an SSL/TSL certificate under `SSL/TSL certificates`
For this add DNS record: `A <@ for root> 165.22.82.171 DNS only Auto`
(make sure to secure all subdomains too -> check everything)
(access to the DNS Provider will be needed)

# TODO google and setup Mail client.
