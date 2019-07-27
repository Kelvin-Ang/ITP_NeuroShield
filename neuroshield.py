import NeuroMem as nm
import GVcomm_SPI as comm
import sys
from imageProcessing import *
from PIL import ImageEnhance
from PIL import Image

ip = ImageProcessor()


class NeuroShield:
	
	def __init__(self):
		if (comm.Connect() != 0):
			print ("KNS! Check your NeuroShield connection la BODOH!!!\n")
			sys.exit()
		else:
			print ("Win liao loh! NeuroShield connected, need do work liao...")
		self.name = "NeuroShield"
		
	def clearData(self):
		nm.ClearNeurons()
				
	#with crop			
	def recogn(self,image):	
		imsrc = cv.imread('recog/recog.png')
		cv.imshow('main', imsrc)	#img1
		cv.waitKey(1)
		
		img = cv.imread(image)
		ip.convertGrayScale(img)
		ip.cropROI('recog/recog.png','image/cropped_gs.png')
		img2 = cv.imread('image/cropped_gs.png')
		img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVector(img2))
		#self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		print("Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		return self.dist, self.cat, self.nid
		
	#without crop	
	def recogn_WOC(self,image):	
		imsrc = cv.imread('recog/recog.png')
		cv.imshow('main', imsrc)	#img1
		cv.waitKey(1)
		
		img = cv.imread(image)
		ip.convertGrayScale(img)
		#ip.cropROI('recog/recog.png','image/cropped_gs.png')
		img2 = cv.imread('recog/recog.png')
		img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVector(img2))
		#self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		self.recoNbr, self.dist, self.cat, self.nid, = nm.Classify(vector, vlen, 2)

		#print("Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		print("RecoNbr = " + repr(self.recoNbr) + "Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		return self.recoNbr, self.dist, self.cat, self.nid	
		
		
	def recogn_Lines_GS_WC(self,image):	
		img = cv.imread(image)
		ip.convertGrayScale(img)
		ip.cropROI('recog/recog.png','image/cropped_gs.png')
		img1 = ip.edgeDetection('image/cropped_gs.png')
		img2 = cv.imread('image/canny.png')
		img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVector(img2))
		self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		print("Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		return self.dist, self.cat, self.nid	



	#train without color wtih crop
	def train_GS_WC(self,image,catergory,count):
		img = cv.imread(image)
		#ip.convertGrayScale(img)
		ip.cropROI('image/capture.png','image/cropped_gs.png')
		
		x = 0.6
		#change birghtness
		for i in range(0,10,1):
			ip.adjust_brightness('image/cropped_gs.png','image/cropped_gs'+str(i)+'.png', x+(i/10.0))
			img2 = cv.imread('image/cropped_gs.png')
			img2 = ip.convertGrayScale(img2)
			vlen,vector = (ip.convertToVector(img2))
			nm.Learn(vector,vlen,catergory)	
			print(x+(i/10.0))
		
		img3 = Image.open('image/cropped_gs.png')
		rotated_img = img3.rotate(180)
		rotated_img.save('image/rotate_' + str(180) +'.png')
		img3 = cv.imread('image/rotate_' + str(180) +'.png')
		img3 = ip.convertGrayScale(img3)
		vlen,vector = (ip.convertToVector(img3))
		nm.Learn(vector,vlen,catergory)	
		
		print('IMAGE LEARNED')
		print(str(count))
		

	
	def train_Lines_RGB_WC(self,image,catergory):
		img = cv.imread(image)
		#ip.convertGrayScale(img)		
		ip.cropROI('image/capture.png','image/cropped_gs.png')
		img1 = ip.edgeDetection('image/cropped_gs.png')
		img2 = cv.imread('image/canny.png')
		#img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVectorRGB(img2))
		nm.Learn(vector,vlen,catergory)	
		print('IMAGE LEARNED')


	#train with color with crop	
	def train_RGB_WC(self,image,catergory):
		img = cv.imread(image)
		#ip.convertGrayScale(img)
		ip.cropROI('image/capture.png','image/cropped_gs.png')
		img2 = cv.imread('image/cropped_gs.png')
		#img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVectorRGB(img2))
		nm.Learn(vector,vlen,catergory)	
		print('IMAGE LEARNED')
		
	#train with color without crop	
	def train_RGB_WOC(self,image,catergory):
		img = cv.imread(image)
		#ip.convertGrayScale(img)
		#ip.cropROI('image/capture.png','image/cropped_gs.png')
		img2 = cv.imread(image)
		#img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVectorRGB(img2))
		nm.Learn(vector,vlen,catergory)	
		print('IMAGE LEARNED')		
		
		
	#train without color without crop	
	def train_GS_WOC(self,image,catergory):
		img = cv.imread(image)
		ip.convertGrayScale(img)
		#ip.cropROI('image/capture.png','image/cropped_gs.png')
		img2 = cv.imread(img)
		#img2 = ip.convertGrayScale(img2)
		vlen,vector = (ip.convertToVectorRGB(img2))
		nm.Learn(vector,vlen,catergory)	
		print('IMAGE LEARNED')				

	
