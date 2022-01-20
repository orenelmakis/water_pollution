#!/usr/bin/env python 

import os
import numpy
import cv2


os.chdir(os.getcwd()+'/water_pollution/')
IMAGES_DIR_NAME = '2022-01-10 Tests'

class image_filter:
    def __init__(self,images_dir):
        self.images_dir = images_dir
        self.images = self.get_images()


    def get_images(self):
        files = os.listdir('./' + self.images_dir)
        images_names = [x for x in os.listdir('./2022-01-10 Tests') if x[-3:].lower() == 'jpg']
        images = []
        for i in images_names:
            img = cv2.imread('./' + self.images_dir + '/' + i)
            shape = (1280,780)
            img = cv2.resize(img,shape)
            images.append(img)
        images = numpy.array(images)
        print(images.shape)
        return images

    def create_RGB_images(self):
        for i in range(len(self.images)):
            name_img = str(i) + ".jpg"
            cv2.imwrite("./ImagesRGB/"+name_img,self.images[i])
            cv2.imwrite("./ImagesRGB/"+"R"+name_img,self.images[i][:,:,0])
            cv2.imwrite("./ImagesRGB/"+"G"+name_img,self.images[i][:,:,1])
            cv2.imwrite("./ImagesRGB/"+"B"+name_img,self.images[i][:,:,2])





def main():
    image_class = image_filter(IMAGES_DIR_NAME) 
    image_class.create_RGB_images()

if __name__ == "__main__":
    main()

