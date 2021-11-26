# encrypt

echo "secret" | gpg --batch --passphrase-fd 0 --output a.txt.gpg --symmetric a.txt

echo "secret" | gpg --batch --passphrase-fd 0 --output b.txt --decrypt a.txt.gpg

or similified 

gpg --batch --passphrase secret --output 21.txt.gpg --symmetric 2.txt

gpg --batch --passphrase secret --output 21.txt --decrypt 21.txt.gpg
