import picamera
import time
from picamera.array import PiRGBArray
import cv2 as cv
import ctypes
import RPi.GPIO as GPIO
import NeuroMem as nm
import numpy as np
import sys
from PIL import ImageEnhance
from PIL import Image
import math


GPIO.setmode(GPIO.BOARD)
toggleLight = 18
light1 = 22
light2 = 32
light3 =	36
light4 = 37

toggleBtn = 7
GPIO.setup(toggleBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(toggleLight, GPIO.OUT)
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.setup(light3, GPIO.OUT)
GPIO.setup(light4, GPIO.OUT)

LENGTH=256
bytearray = ctypes.c_int * LENGTH
vector=bytearray()

roiW = int(250)
roiH = int(250)
bW = int(4)
bH = int(4)
normalize = int(1)


angle_cat1 = int(180)
rotate_count_cat1 = int(0)

angle_cat2 = int(180)
rotate_count_cat2 = int(0)

angle_cat3 = int(180)
rotate_count_cat3 = int(0)

angle_cat4 = int(180)
rotate_count_cat4 = int(0)

angle_recog = int(180)
rotate_count_recog = int(0)


def cam():
    with picamera.PiCamera() as camera:
        camera.resolution = (250, 250)
        x = 1
        while x == 1:
            if not GPIO.input(toggleBtn):
                GPIO.output(toggleLight, False)
                return
            camera.capture('recog/cat500.jpg')
            #test2()
            #for i in range(7):
            recog()
		
def cat1():
  
  with picamera.PiCamera() as camera:
    camera.resolution = (250, 250)
    camera.capture('image/111.png')
    detect_and_crop('image/111.png', 'image/111.png')
    
    time.sleep(1)

    # learn1()

    print 'cat1'
   

def cat2():
  
  
  with picamera.PiCamera() as camera:
    camera.resolution = (250, 250)
    camera.capture('image/222.png')
    detect_and_crop('image/222.png', 'image/222.png')
    
    time.sleep(1)

    # learn2()

    print 'cat2'
   

def cat3():  
  
  with picamera.PiCamera() as camera:
    camera.resolution = (250, 250)
    camera.capture('image/333.png')
    detect_and_crop('image/333.png', 'image/333.png')
    
    time.sleep(1)

    # learn2()

    print 'cat3'		
			

def cat4(): 
  
  with picamera.PiCamera() as camera:
    camera.resolution = (250, 250)
    camera.capture('image/444.png')
    detect_and_crop('image/444.png', 'image/444.png')
    
    time.sleep(1)

    # learn2()

    print 'cat4'

def compare():
  img1 = cv.imread('image/test.png')
  img2 = cv.imread('image/test.png')
  img3 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
  
  cv.imshow('img1',img1)
  cv.imshow('img3',img3)
  np.set_printoptions(threshold=sys.maxsize)
  print('img1: ' + str(img1))
  print("**************************************")
  print(len(img1[1][1]))
  print(len(img1[1]))
  print(len(img1))
  print("**************************************")
  print(len(img3[1]))
  print(len(img3))
  print("**************************************")
  print('img3: ' + str(img3))
  cv.waitKey(0)
  
def learn1():
  global angle_cat1, rotate_count_cat1    
  
  #detect_and_crop('111.jpg', '111_cropped.png')
  pill_img = Image.open('image/111.png')
  rotated_img = pill_img.rotate(angle_cat1)
  rotated_img.save('image/111_rotate_' + str(angle_cat1) +'.png')
      
  try:
    # Load an image for analysis
    #list = ['111_cropped.png','111_cropped2.png']

    #for i in range(len(list)):
      
      #imsrc=cv.imread(list[i])
    #imsrc=cv.imread('111_rotate.jpg')
    imsrc=cv.imread('image/111_rotate_' + str(angle_cat1) +'.png')
    #cv.imshow('cat1', imsrc)	#img1
    cv.waitKey(1)	
      
    img = cv.cvtColor(imsrc, cv.COLOR_BGR2GRAY)
    #print(edges)
    
    imW=img.shape[1]
    imH=img.shape[0]
    print("imW = " + str(int(imW)))
    print("imH = " + str(int(imH)))
    print("Image = " + repr(imW) + " x " + repr(imH))
    imCtrX= imW/2
    imCtrY= imH/2

    
    roiW = img.shape[1]
    roiH = img.shape[0]
    roiL = int(0)
    roiT = int(0)
    #roiL= int(imCtrX - roiW/2)
    #roiT= int(imCtrY - roiH/2)
    bW = int(2)
    bH = int(2)
    normalize = int(1)
    
    # prepare image to hold the ROI overlay
    imdisp=img.copy()
    cv.rectangle(imdisp,(roiL, roiT),(roiL+roiW, roiT+roiH),(255,0,0),1)
    #cv.imshow('Learn central ROI', imdisp)
    cv.waitKey(1)

    # Learn ROI at center of the image
    vlen, vector=GetGreySubsample2(img, roiL, roiT, roiW, roiH, bW, bH, normalize)
    nm.Learn(vector,vlen,1)		#set learn cat as 1
  except:
    print('errorrrrrr')

  print("IMAGE 1 LEARNED") 
  
  #angle_cat1 += 45
  
  
		
def learn2():
  global angle_cat2, rotate_count_cat2

  #detect_and_crop('222.jpg', '222_cropped.png')
  pill_img = Image.open('image/222.png')
  rotated_img = pill_img.rotate(angle_cat2)
  rotated_img.save('image/222_rotate_' + str(angle_cat2) +'.png')
      
  
  # Load an image for analysis
  #list = ['222_cropped.png','222_cropped2.png']
  try:
      
    #for i in range(len(list)):
      
      #imsrc=cv.imread(list[i])
    #imsrc=cv.imread('222_rotate.jpg')
    imsrc=cv.imread('image/222_rotate_' + str(angle_cat2) +'.png')

   
    #cv.imshow('cat1', imsrc)	#img1
    cv.waitKey(1)	
      
    img = cv.cvtColor(imsrc, cv.COLOR_BGR2GRAY)
    #print(edges)
    
    imW=img.shape[1]
    imH=img.shape[0]
    print("imW = " + str(int(imW)))
    print("imH = " + str(int(imH)))
    print("Image = " + repr(imW) + " x " + repr(imH))
    imCtrX= imW/2
    imCtrY= imH/2

    
    roiW = img.shape[1]
    roiH = img.shape[0]
    roiL = int(0)
    roiT = int(0)
    #roiL= int(imCtrX - roiW/2)
    #roiT= int(imCtrY - roiH/2)
    bW = int(2)
    bH = int(2)
    normalize = int(1)
    
    # prepare image to hold the ROI overlay
    imdisp=img.copy()
    cv.rectangle(imdisp,(roiL, roiT),(roiL+roiW, roiT+roiH),(255,0,0),1)
    #cv.imshow('Learn central ROI', imdisp)
    cv.waitKey(1)

    # Learn ROI at center of the image
    vlen, vector=GetGreySubsample2(img, roiL, roiT, roiW, roiH, bW, bH, normalize)
    nm.Learn(vector,vlen,2)		#set learn cat as 2
      
  except:
    print('errorrrrrr')
  
  print("IMAGE 2 LEARNED")
  
  #angle_cat2 += 45
  
def learn3():
  global angle_cat3, rotate_count_cat3

  #detect_and_crop('222.jpg', '222_cropped.png')
  pill_img = Image.open('image/333.png')
  rotated_img = pill_img.rotate(angle_cat2)
  rotated_img.save('image/333_rotate_' + str(angle_cat3) +'.png')
     
  
  # Load an image for analysis
  #imsrc=cv.imread('cat3.jpg')
  imsrc=cv.imread('image/333_rotate_' + str(angle_cat3) +'.png')

  #cv.imshow('cat1', imsrc)	#img1
  cv.waitKey(1)	
  
  img = cv.cvtColor(imsrc, cv.COLOR_BGR2GRAY)
  
  imW=img.shape[1]
  imH=img.shape[0]
  print("imW = " + str(int(imW)))
  print("imH = " + str(int(imH)))
  print("Image = " + repr(imW) + " x " + repr(imH))
  imCtrX= imW/2
  imCtrY= imH/2

  
  roiW = img.shape[1]
  roiH = img.shape[0]
  roiL = int(0)
  roiT = int(0)
  #roiL= int(imCtrX - roiW/2)
  #roiT= int(imCtrY - roiH/2)
  bW = int(2)
  bH = int(2)
  normalize = int(1)
  
  # prepare image to hold the ROI overlay
  imdisp=img.copy()
  cv.rectangle(imdisp,(roiL, roiT),(roiL+roiW, roiT+roiH),(255,0,0),1)
  #cv.imshow('Learn central ROI', imdisp)
  cv.waitKey(1)

  # Learn ROI at center of the image
  vlen, vector=GetGreySubsample2(img, roiL, roiT, roiW, roiH, bW, bH, normalize)
  nm.Learn(vector,vlen,3)		#set learn cat as 3
  print("IMAGE 3 LEARNED")	
  
  #angle_cat3 += 45
  
def learn4():
  global angle_cat4, rotate_count_cat4

  pill_img = Image.open('image/444.png')
  rotated_img = pill_img.rotate(angle_cat4)
  rotated_img.save('image/444_rotate_' + str(angle_cat4) +'.png')
     
  
  # Load an image for analysis
  #imsrc=cv.imread('cat3.jpg')
  imsrc=cv.imread('image/444_rotate_' + str(angle_cat4) +'.png')
  
  cv.waitKey(1)	
  
  img = cv.cvtColor(imsrc, cv.COLOR_BGR2GRAY)
  
  imW=img.shape[1]
  imH=img.shape[0]
  print("imW = " + str(int(imW)))
  print("imH = " + str(int(imH)))
  print("Image = " + repr(imW) + " x " + repr(imH))
  imCtrX= imW/2
  imCtrY= imH/2

  
  roiW = img.shape[1]
  roiH = img.shape[0]
  roiL = int(0)
  roiT = int(0)
  #roiL= int(imCtrX - roiW/2)
  #roiT= int(imCtrY - roiH/2)
  bW = int(2)
  bH = int(2)
  normalize = int(1)
  
  # prepare image to hold the ROI overlay
  imdisp=img.copy()
  cv.rectangle(imdisp,(roiL, roiT),(roiL+roiW, roiT+roiH),(255,0,0),1)
  #cv.imshow('Learn central ROI', imdisp)
  cv.waitKey(1)

  # Learn ROI at center of the image
  vlen, vector=GetGreySubsample2(img, roiL, roiT, roiW, roiH, bW, bH, normalize)
  nm.Learn(vector,vlen,4)		#set learn cat as 4
  print("IMAGE 4 LEARNED")	
  
  #angle_cat4 += 45
	
		
def recog():

  
  global angle_recog, rotate_count_recog
  # Load an image for analysis
  
  imsrc = cv.imread('recog/cat500.jpg')
  detect_and_crop('recog/cat500.jpg', 'recog/cat500.png')
  #pill_img = Image.open('recog/cat500.jpg')
  #rotated_img = pill_img.rotate(angle_recog)
  #rotated_img.save('recog/cat500_rotate_' + str(angle_recog) +'.png')
  imsrc = cv.imread('recog/cat500.png')
  
  cv.imshow('main', imsrc)	#img1
  cv.waitKey(1)
  
  imgl = cv.cvtColor(imsrc, cv.COLOR_BGR2GRAY)
  imW=imgl.shape[1]
  imH=imgl.shape[0]
  
  
  print("imW = " + str(int(imW)))
  print("imH = " + str(int(imH)))
  print("Image = " + repr(imW) + " x " + repr(imH))
  imCtrX= imW/2
  imCtrY= imH/2
  
  roiW = imW
  roiH = imH
  roiL = int(0)
  roiT = int(0)
  #roiL= int(imCtrX - roiW/2)
  #roiT= int(imCtrY - roiH/2)
  bW = int(2)
  bH = int(2)
  normalize = int(1)
   
  # Recognize ROI at same position, expect a distance of 0
  vlen, vector =GetGreySubsample2(imgl, roiL, roiT, roiW, roiH, bW, bH, normalize)
  dist, cat, nid = nm.BestMatch(vector, vlen)
  print("Reco cat = " + repr(cat) + " at dist =" + repr(dist) + " NID = " + repr(nid))
  if (cat == 1):
    #print("Reco cat = " + repr(cat) + " at dist =" + repr(dist) + " NID = " + repr(nid))
    GPIO.output(light1, True)
    GPIO.output(light2, False)
    GPIO.output(light3, False)
    GPIO.output(light4, False)
    return 1

  elif (cat == 2): 
    #print("Reco cat = " + repr(cat) + " at dist =" + repr(dist) + " NID = " + repr(nid))
    GPIO.output(light1, False)
    GPIO.output(light2, True)
    GPIO.output(light3, False)
    GPIO.output(light4, False)
    return 2

  elif (cat == 3): 
    #print("Reco cat = " + repr(cat) + " at dist =" + repr(dist) + " NID = " + repr(nid))
    GPIO.output(light1, False)
    GPIO.output(light2, False)
    GPIO.output(light3, True)
    GPIO.output(light4, False)
    return 3
  
  elif (cat == 4): 
    #print("Reco cat = " + repr(cat) + " at dist =" + repr(dist) + " NID = " + repr(nid))
    GPIO.output(light1, False)
    GPIO.output(light2, False)
    GPIO.output(light3, False)
    GPIO.output(light4, True)
    return 4
    
  else:
    GPIO.output(light1, False)
    GPIO.output(light2, False)
    GPIO.output(light3, False)
    GPIO.output(light4, False)

  angle_recog += 45  

#-----------------------------------------------------
# Extract a subsample of the ROI at the location X,Y
# using a block size bW*bH and amplitude normalization on or off
# return the length of the output vector
#-----------------------------------------------------
def GetGreySubsample2(image, roiL, roiT, roiW, roiH, bW, bH, normalize):
  # subsample blocks of BWxBH pixels from the ROI [Left, Top, Width, Height]
  # vector is the output to broadcast to the neurons for learning or recognition
  print("roiH")
  print(roiH)
  print("roiw")
  print(roiW)
  p = 0
  bH = int(math.ceil(roiH / 15.0))
  print("bH: ")
  print(bH)
  bW = int(math.ceil(roiW / 15.0))
  print("bW: ")
  print(bW)
  for y in range(roiT, roiT + roiH, bH):
    print("y")
    print(y)
    for x in range(roiL, roiL + roiW, bW):
      print("x")
      print(x)
      Sum=0	
      for yy in range(bH):
          
        #print("yy")
        #print(yy)
        for xx in range (bW):
          #print("xx")
          #print(xx)
          # to adjust if monochrome versus rgb image array
          if (y+yy < roiH and x+xx < roiW):
            Sum += image[y+yy, x+xx]
          
      #print("SUM ")
      
      #print(p)
      vector[p] = (int)(Sum / (bW*bH))

      
      #log the min and max component
      min = 255
      max = 0
      if (max < vector[p]):
        max = vector[p]
      if (min > vector[p]):
        min = vector[p]
      
      p=p+1
    
  if ((normalize == 1) & (max > min)):
    for i in range (0, p):
      Sum= (vector[i] - min) * 255
      vector[i] = (int)(Sum / (max - min))
      
  # return the length of the vector which must be less or equal to 256
  return p, vector




###############
def detect_and_crop(input, output):
  try:
    img = cv.imread(input)
    #img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 90, 250)

    ## find the non-zero min-max coords of canny
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)

    ## crop the region
    cropped = img[y1:y2, x1:x2]
    cv.imwrite(output, cropped)

    #tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
    #cv2.imshow("tagged", tagged)
    #cv2.waitKey()
  except:
    print('@@@@@@@@ CROPPING ERROR @@@@@@@@@@')
    
  
      
def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  
  return result
    
      
      


