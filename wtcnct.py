from cv2 import imread, vconcat, imwrite
from os import listdir, mkdir, rename
from os.path import exists as pathex
from natsort import os_sorted


def imageSave(pth, arr):
    resimg = vconcat(arr)
    return imwrite(pth, resimg)

path = input('Input folder contains images (example c:/manga): ')

ext = ('.jpg', '.png', '.gif')
list = [ f for f in os_sorted(listdir(path)) if f.endswith(ext) ]
images = [ imread(path+"\\"+i) for i in list ]

buf = path+"\\backup"
try:
    mkdir(buf)
except FileExistsError:
    None

try:
    mkdir(path+'\\result')
except FileExistsError:
    None

itr = 0
while len(images) != 0:
    imgs = [ ]

    print('Enter the number of the image that will be the end of the page. (Less than 45)')
    crpng = int(input("> "))

    if crpng > 0:
        nx = 0
        for i in images:
            if nx + 1 <= crpng:
                imgs.append(i)
                nx = nx + 1

        #for i in imgs: print(i.filename)

        imageSave(path+'\\result\\page_'+str(itr+1)+'.jpg', imgs)

        for i in range(nx):
            del imgs[0]
            rename(path+"\\"+list[0], buf+'\\'+list[0])
            del list[0]

        list = [ f for f in os_sorted(listdir(path)) if f.endswith(ext) ]
        images = [ imread(path+"\\"+i) for i in list ]
    else:
        print('Enter a number greater than zero!')

    itr = itr + 1
