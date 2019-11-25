import numpy as np
import cv2
import os
import urllib
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def store_img():
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n13104059'
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            urllib.urlretrieve(i,"neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg',resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))



store_img()







#for file_type in ['neg']:
#    for img in os.listdir(file_type):
#        if file_type == 'neg':
#            line = file_type+'/'+img+'\n'
#            with open('bg.txt','a') as f:
#                f.write(line)

#        elif file_type == 'pos':
#            line = file_type+'/'+img+' 1 0 0 50 50\n'
#            with open('info.dat','a') as f:
#		f.write(line)
