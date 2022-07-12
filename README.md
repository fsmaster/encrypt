# encrypt

ENC_SECRET='password'

export ENC_SECRET


echo "secret" | gpg --batch --passphrase-fd 0 --output a.txt.gpg --symmetric a.txt

echo "secret" | gpg --batch --passphrase-fd 0 --output b.txt --decrypt a.txt.gpg

or similified 

gpg --batch --passphrase secret --output 21.txt.gpg --symmetric 2.txt

gpg --batch --passphrase secret --output 21.txt --decrypt 21.txt.gpg

 
 sshpass -p "password" rsync -R -avzh /storage/googlephotos/ admin@192.168.12.5:/mnt/HD/HD_a2/igor_hdd/storage/googlephotos/


 sshpass -p "password" rsync -R -avzh  admin@192.168.12.5:/mnt/HD/HD_a2/igor_hdd/ /storage/igor_hdd/
 
 #when have ssh error

sshpass -p "password" rsync -R -avzh -e "ssh -o StrictHostKeyChecking=no  -o UserKnownHostsFile=/dev/null"  admin@192.168.12.5:/mnt/HD/HD_a2/ /storage/nas_3tb/

\# -o UserKnownHostsFile=/dev/null -beacause of old NAS, do not store known_hosts

#cron:
34      16      *       *       *       /home/ubuntu/projects/scripts/nas-googlephotos.sh>/var/log/nas-googlephotos.log


#on mikrotik do some routing and config per https://strongvpn.com/setup-mikrotik-6-l2tp/

# on windows

route add 192.168.12.0 mask 255.255.255.0 192.168.4.38 metric 1

# on linux

 ip route add 192.168.12.5 via 192.168.4.38

# decrypt

ENC_SECRET='password'

export ENC_SECRET

1. configure decrypt.yml as example
\#destination is source, decrypt is destination, other keys are ignored
- service:
    name: lessons
    source: /storage/temp
    destination: /storage/gpg/lessons
    decrypt: /storage/decrypt-temp/lessons
    test: /storage/gpg-test/temp

2. run decrypt.py
3. 
