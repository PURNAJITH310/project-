import cv2
import dropbox
import  time
import random

starttime=time.time()
print(starttime)
def takesnapshot():
    number= random.randint(0,100)
    pictureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        imagename="image"+str(number)+".png"
        ret,frame=pictureObject.read()
        print(ret)
        cv2.imwrite("image1.png",frame)
        starttime=time.time
        result=False
   
    pictureObject.release

    cv2.destoryAllWindows
      return imagename

 def upload_file(img_name):
      access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN" 
      file =img_name 
      file_from = file
      file_to="/testFolder/"+(img_name)
       dbx = dropbox.Dropbox(access_token)
      with open(file_from, 'rb') as f: 
          dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
          print("file uploaded")

def main():
    while(True):
        if((time.time()-starttime)>=5):
            name=takesnapshot()
            upload_file(name)
main()


            

