# Hosting for data pipeline development

# Digital Ocean
 - [doctl](https://github.com/digitalocean/doctl) — command line tool for provisioning 
    Digital Ocean droplets
 - [dotool.sh](https://github.com/devops-study-group/digitalocean) — 
    make doctl easier to work with.

## Secure backup a Linux volume over a network
- Backup: `dd if=/dev/sda | gzip -1 - | ssh user@hostname dd of=sda.img.gz`
- Restore: `ssh user@hostname dd if=sda.img.gz | gunzip -1 - | dd of=/mnt/sda.img`
- Test: `fdisk ./sda.img` returns block size and start of each partition
- Make mount point: `mkdir /mnt/partname`
- Calc offset: start * blocksize. E.g. 2048*512 = 1048576
- Mount: `mount -o loop, offset=OFFSET hda.img /mnt/partname`
- Ready to use at `/mnt/partname`

## Provision checklist
- create droplet with SSH key (not root login)
- create SSH Public Key for user

## Configuration checklist
- create a username on new droplet
- give publc keys to study group members

# Platforms
- [Digital Ocean Droplets](https://digitalocean.com)
- [Google Data Studio](https://developers.google.com/datastudio/)
- [AWS](https://aws.amazon.com/)
