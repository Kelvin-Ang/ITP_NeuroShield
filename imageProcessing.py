import cv2 as cv
# import picamera
from fake_picamera import PiCamera
import numpy as np
import math
import ctypes
from PIL import ImageEnhance
from PIL import Image

LENGTH=256
bytearray = ctypes.c_int * LENGTH
vector=bytearray()

class ImageProcessor:	
			
		
	def convertGrayScale(self,imageFileName):
		image = cv.imread(imageFileName)		
		img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
		cv.imwrite('image/grayscale.png', img)
		#print(img)
		return img
	
	
	def cropROI(self,imageFileName, outputFileName):
		try:
			img = cv.imread(imageFileName)
			#blur first
			blurred = cv.blur(img, (3,3))
			#get canny of blurred image
			canny = cv.Canny(blurred, 90, 250)

			## find the non-zero min-max coords of canny
			pts = np.argwhere(canny>0)
			y1,x1 = pts.min(axis=0)
			y2,x2 = pts.max(axis=0)

			## crop the region
			cropped = img[y1:y2, x1:x2]
			cv.imwrite(outputFileName, cropped)
			return cv.imread(outputFileName)

		except:
			print('@@@@@@@@ CROPPING ERROR @@@@@@@@@@')
		

	def edgeDetection(self,imageFileName):		
		img = cv.imread(imageFileName)
		blurred = cv.blur(img, (3,3))
		canny = cv.Canny(blurred, 90, 250)
				
		cv.imwrite('image/canny.png',canny)
		src = cv.imread('image/canny.png')
		tmp = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
		_,alpha = cv.threshold(tmp, 0, 255, cv.THRESH_BINARY)
		b, g, r = cv.split(src)
		rgba = [b, g, r, alpha]
		dst = cv.merge(rgba, 4)
		print dst
		cv.imwrite('image/canny.png',dst)
		return dst
		
	def convertToVector(self,imageFileName):
		img = self.convertGrayScale(imageFileName)
		p = 0
		imW=img.shape[1]
		imH=img.shape[0]
		bW = int(math.ceil(imW/15.0))
		bH = int(math.ceil(imH/15.0))
		for y in range(0, imH, bH):
			for x in range(0, imW, bW):
				Sum=0
				for yy in range(0, bH):
					for xx in range (0, bW):
						# to adjust if monochrome versus rgb image array
						if((y+yy<imH) and (x+xx<imW)):
							Sum += img[y+yy, x+xx]
				vector[p] = (int)(Sum / (bW*bH))
				#log the min and max component
				min = 255
				max = 0
				if (max < vector[p]):
					max = vector[p]
				if (min > vector[p]):
					min = vector[p]
				p=p+1
			
		if ((1 == 1) & (max > min)):
		  for i in range (0, p):
			  Sum= (vector[i] - min) * 255
			  vector[i] = (int)(Sum / (max - min))

		# return the length of the vector which must be less or equal to 256
		return p, vector
			  
	
	def rotate(self, imageFileName, angle):
		image = cv.imread(imageFileName)
		image_center = tuple(np.array(image.shape[1::-1]) / 2)
		rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
		result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
		return result
		
	def adjust_brightness(self,imageFileName, outputFileName, brightness_value):
		image = Image.open(imageFileName)
		enhancer_object = ImageEnhance.Brightness(image)
		out = enhancer_object.enhance(brightness_value)
		out.save(outputFileName)
		

class Camera:
	def captureImage(self,imageFileName):
		with picamera.PiCamera() as camera:
			camera.resolution = (250, 250)
			camera.exposure_mode = 'auto'
			return camera.capture(imageFileName)	
	
