import cv2
import numpy as np

def buildDataset(images, labels):
    print('press 0-9 for classes, n for next image, b for back one image and q for quit')
    print('there are '+str(len(images)) +' images')
    index = 0
    while index < len(images):
        print('index:'+str(index))
        print('current label = '+str(labels[index]))
        cv2.imshow('current image', images[0])
        key = cv2.waitKey(0) & 0xFF
        if ord('0') <= key <= ord('9'):
            labels[index] = key - ord('0')
            index+=1
        elif ord('n') == key:
            index+=1
        elif ord('b') == key:
            index-=1
        elif key  == ord('q'):
            break


if __name__ == '__main__':
    i = np.zeros([3,50,50])
    l = np.zeros([3])
    buildDataset(i,l)
    print(l)
