import glob,os,time,sys
#my_path ='/storage/Downloads/'
#files = glob.glob(my_path + '/**/*.*', recursive=True)

#print (files)
#for file in files:
#    print(file)


import yaml

SECRET=os.getenv('ENC_SECRET')
if SECRET is None:
    print("no ENC_SECRET, exiting, h: tia int i pbmega seat full +xinxin")
    sys.exit(-1)

def enc(source,destination):
    print (source,destination)
    files = glob.glob(source + '/**/*.*', recursive=True)
    for source_file in files:
        destination_file=source_file.replace(source,destination)+'.gpg'
        print (source_file)
        print (destination_file)
        if not os.path.exists(destination_file):
            print ("not exists "+str(destination_file))
            destination_dir=os.path.dirname(destination_file)
            if not os.path.exists(destination_dir):
                print("creating "+str(destination_dir))
                os.makedirs(destination_dir)

            cmd='gpg --batch --passphrase '+SECRET +' --output \''+destination_file+'\''+' --symmetric \''+source_file+'\''
#            print(cmd)
            result = os.popen(cmd)
            time.sleep(10)
            print(result)
#    print(files)



with open("enc.yml", "r") as stream:
    try:
       y=yaml.safe_load(stream)
       l=(len(y))
       for i in range(0,l):
           source=y[i]["service"]["source"]
           destination=y[i]["service"]["destination"]
           enc (source,destination)

    except yaml.YAMLError as exc:
        print(exc)root@dell:/home/ig#
