import NeuroMem as nm
import GVcomm_SPI as comm
import sys
from imageProcessing import *
from PIL import ImageEnhance
from PIL import Image
import logging

logging.basicConfig(filename = "test6.txt", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
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

	#train wtih crop and brightness
	def train_GS_WC_brightness(self,imageFileName,category):
		ip.cropROI(imageFileName,'image/cropped_gs.png')
		x = 0.6
		#change birghtness
		for i in range(0,10,1):
			ip.adjust_brightness('image/cropped_gs.png','image/cropped_gs.png', x+(i/10.0))
			vlen,vector = (ip.convertToVector('image/cropped_gs.png'))
			nm.Learn(vector,vlen,category)	
			#print(x+(i/10.0))
		
		#print('IMAGE LEARNED')
			
		
		
	#train without crop	
	def train_GS_WOC(self,imageFileName,category):
		vlen,vector = (ip.convertToVector(imageFileName))
		nm.Learn(vector,vlen,category)	
		#print('IMAGE LEARNED')			
		
		
	#train without crop with brightness	
	def train_GS_WOC_WB(self,imageFileName,category):
		x = 0.6
		for i in range(0,10,1):
			ip.adjust_brightness(imageFileName,'image/noCrop_brightness.png', x+(i/10.0))
			vlen,vector = (ip.convertToVector('image/noCrop_brightness.png'))
			nm.Learn(vector,vlen,category)	
			#print(x+(i/10.0))		
		#print('IMAGE LEARNED')				
			
	#train crop 
	def train_GS_WC(self,imageFileName,category):
		imgstr = 'ROI/trainWRoi.png'
		ip.cropROI(imageFileName,imgstr)
		vlen,vector = (ip.convertToVector(imgstr))
		nm.Learn(vector,vlen,category)	
		#print('IMAGE LEARNED')
		
	def recogn_W_crop(self, imageFileName):
		imgstr = 'ROI/Recogn_cropped.png'
		ip.cropROI(imageFileName, imgstr)
		logger.debug("converting to vector...")
		vlen,vector = (ip.convertToVector(imgstr))
		logger.debug("trying to match...")
		self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		print("Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		return self.dist, self.cat, self.nid

	#recog without color without crop for test
	def recogn_Wout_crop(self, imageFileName):
		logger.debug("converting to vector...")
		vlen,vector = (ip.convertToVector(imageFileName))
		logger.debug("trying to match...")
		self.dist, self.cat, self.nid = nm.BestMatch(vector, vlen)
		print("Reco cat = " + repr(self.cat) + " at dist =" + repr(self.dist) + " NID = " + repr(self.nid))
		return self.dist, self.cat, self.nid


	
