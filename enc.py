import glob,os,time,sys
#my_path ='/storage/Downloads/'
#files = glob.glob(my_path + '/**/*.*', recursive=True)

#print (files)
#for file in files:
#    print(file)


import yaml
import logging


logging.basicConfig(filename='enc.log', filemode='a', format='%(asctime)s [%(levelname)s] %(message)s ', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logging.info('Enc started')

SECRET=os.getenv('ENC_SECRET')
if SECRET is None:
    logging.error("no ENC_SECRET, exiting, h: tia int i pbmega seat full +xinxin")
    sys.exit(-1)

if not os.path.exists("enc.lock"):
    with open('enc.lock', 'w') as fp:
        pass
else:
    logging.error("evo.lock present, exitnig...")
    sys.exit(-1)




def get_hash(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

#    print(file_hash.digest())
    print(file_hash.hexdigest())


def same(name1, name2): 
  with open(name1, "rb") as one: 
    with open(name2, "rb") as two: 
      chunk = other = True 
      while chunk or other: 
        chunk = one.read(10485760) 
        other = two.read(10485760) 
        if chunk != other: 
          return False 
      return True 




def enc(source,destination,test):
    print (source,destination,test)
    files = glob.glob(source + '/**/*.*', recursive=True)
    for source_file in files:
        destination_file=source_file.replace(source,destination)+'.gpg'
        test_file=source_file.replace(source,test)
        print (source_file)
        print (destination_file)
        print (test_file)
        if not os.path.exists(destination_file):
            logging.debug ("not exists "+str(destination_file))
            destination_dir=os.path.dirname(destination_file)
            if not os.path.exists(destination_dir):
                logging.info("creating "+str(destination_dir))
                os.makedirs(destination_dir)

            if not os.path.exists(test_file):
                logging.debug ("test file not exists "+str(test_file))
                test_dir=os.path.dirname(test_file)
                if not os.path.exists(test_dir):
                    logging.info("creating test "+str(test_dir))
                    os.makedirs(test_dir)

            if os.path.exists(destination_file+'.tmp'):
                logging.info("dest tmp exists "+destination_file+".tmp, deleting")
                os.remove(destination_file+'.tmp')


            cmd='gpg -vv --batch --passphrase '+SECRET +' --output \''+destination_file+'.tmp\''+' --symmetric \''+source_file+'\''
            cmd_test='gpg -vv --batch --passphrase '+SECRET +' --output \''+test_file+'\''+' --decrypt \''+destination_file+'.tmp\''
#            print(cmd)
#            print(cmd_test)

            result = os.system(cmd)
#            logging.info("Done enc here")
#            time.sleep(3)
            result = os.system(cmd_test)
#            time.sleep(3)
#            print (get_hash(source_file))
#            print (get_hash(test_file))

            logging.debug("Comparing files...")
            if same(source_file,test_file):
                print("same, renaming")
                os.rename(destination_file+'.tmp',destination_file)
                os.remove(test_file)
                logging.info("Done "+destination_file)
            else:
                print("diff, not renaming")
                logging.error("bad DST file "+destination_file) 
#            logging.info(hashlib.md5(source_file).hexdigest())
#            logging.info(hashlib.md5(test_file).hexdigest())
#            time.sleep(10)
#            print(str(result))
#    print(files)



with open("enc.yml", "r") as stream:
    try:
       y=yaml.safe_load(stream)
       l=(len(y))
       for i in range(0,l):
           source=y[i]["service"]["source"]
           destination=y[i]["service"]["destination"]
           test=y[i]["service"]["test"]
           enc (source,destination,test)

    except yaml.YAMLError as exc:
        print(exc)
    except Exception as e:
        print(e)

os.remove("enc.lock")
