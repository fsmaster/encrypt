# encrypt

echo "secret" | gpg --batch --passphrase-fd 0 --output a.txt.gpg --symmetric a.txt

echo "secret" | gpg --batch --passphrase-fd 0 --output b.txt --decrypt a.txt.gpg

or similified 

gpg --batch --passphrase secret --output 21.txt.gpg --symmetric 2.txt

gpg --batch --passphrase secret --output 21.txt --decrypt 21.txt.gpg

 
 sshpass -p "password" rsync -R -avzh /storage/googlephotos/ admin@192.168.12.5:/mnt/HD/HD_a2/igor_hdd/storage/googlephotos/


 sshpass -p "password" rsync -R -avzh  admin@192.168.12.5:/mnt/HD/HD_a2/igor_hdd/ /storage/igor_hdd/

#cron:
34      16      *       *       *       /home/ubuntu/projects/scripts/nas-googlephotos.sh>/var/log/nas-googlephotos.log


#on mikrotik do some routing and config per https://strongvpn.com/setup-mikrotik-6-l2tp/
