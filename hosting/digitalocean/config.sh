USER=root
NEWUSER=dataops

config-help(){
  echo "
  remote configuration file v 001
  -------------------------------
  Run this remotely via local machine via:
   1) scp config.sh ssh user@host:config.sh
   2) ssh user@host: "source config.sh && config-init"
  Or by:
    dotool-config
"
}

config-update-os(){
  apt update
  apt -y upgrade
}

config-add-user(){
  useradd -m -s /bin/bash $NEWUSER
  usermod -a -G sudo $NEWUSER
}

config-security(){
  echo "%sudo   ALL=(ALL:ALL)  NOPASSWD: ALL" >> /etc/sudoers
}

config-copy-keys(){
  mkdir /home/$NEWUSER/.ssh
  cp /root/.ssh/authorized_keys /home/$NEWUSER/.ssh/authorized_keys
  chown -R $NEWUSER:$NEWUSER /home/$NEWUSER/.ssh
  chmod 0700 /home/$NEWUSER/.ssh
  chmod 0600 /home/$NEWUSER/.ssh/authorized_keys
}

# This local functions will be called. Comment out as needed.
config-init(){
  config-update-os
  config-add-user
  config-copy-keys
  config-security
}
