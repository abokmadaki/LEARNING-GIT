import cv2
import numpy as np
import time
def blur():
    #reading from disk
    img = cv2.imread("D:\ADC\Learning-Git\Filters\IMG-20200924-WA0007.jpg")
    gray_img = cv2.imread("D:\ADC\Learning-Git\Filters\IMG-20200924-WA0007.jpg",0)

    cv2.imshow("Image",img)
    cv2.imshow("Gray Image",gray_img)
    img=cv2.blur(img,ksize=(30,30))
    cv2.imshow("Blur Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# applying threshold to gray image
def grey_thres():
    photo= cv2.imread(r"D:\ADC\Learning-Git\Filters\images.jpeg")
    # resizing image
    photo=cv2.resize(photo,(320,240))

    # converting color image to gray scale
    gray=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

    ret,thresh2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)

    ret,thresh3=cv2.threshold(gray,125,255,cv2.THRESH_TRUNC)

    ret,thresh4=cv2.threshold(gray,125,255,cv2.THRESH_TOZERO)

    ret,thresh5=cv2.threshold(gray,125,255,cv2.THRESH_TOZERO_INV)

    cv2.imshow("original image",photo)
    cv2.imshow("ii",gray)
    cv2.imshow("binary threshold image",thresh1)

    cv2.imshow("binary inverted image",thresh2)

    cv2.imshow("truncated threshold image",thresh3)

    cv2.imshow("set to 0 image",thresh4)

    cv2.imshow("set to 0 inverted image",thresh5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def canny():

    img = cv2.imread(r"D:\ADC\Learning-Git\Filters\IMG_20200220_131141.jpg")
    img =cv2.resize(img,(520,620))
    # applying canny edge detection algo

    canny=cv2.Canny(img,50,150)
    cv2.imshow("Image",img)
    cv2.imshow("canny",canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    n=int(input("Which type of image do you wanna see\n Press 1 for blur \n 2 for Grey Threshold images\n 3 for edged images \n"))
    while n:
        if n==0:
            exit()
        elif n==1:
            blur()
        elif n==2:
            grey_thres()
        elif n==3:
            canny()
        else:
            print("Wrong input!")

        time.sleep(5)
        n=int(input("Which type of image do you wanna see\n Press 1 for blur \n 2 for Grey Threshold images\n 3 for edged images \n 0 for quit\n"))
    

