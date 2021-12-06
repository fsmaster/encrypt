#!/bin/bash
#./root/.bashrc
source $HOME/.profile
if [ -e /root/rsyncjob-googlephotos.lock ]
then
  echo "Rsync job already running...exiting"
  exit
fi

touch /root/rsyncjob-googlephotos.lock

#your code in here
sshpass -p "password" rsync -R -avzh /storage/googlephotos/ admin@192.168.12.5:/mnt/HD/HD_a2/igor_hdd/storage/googlephotos/
#delete lock file at end of your job

rm /root/rsyncjob-googlephotos.lock
