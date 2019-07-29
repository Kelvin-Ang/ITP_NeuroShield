from button import *
from neuroshield import *
from imageProcessing import *

neuroShield = NeuroShield()
ip = ImageProcessor()
camera = Camera()

def learnWithCrop_angle():
	for x in range(6):
		logger.debug("Learning images with crop")
		#print('training cat1')
		neuroShield.train_GS_WC('trainModel/Cat1_'+ str(x) +'.png',1)
		#print('training cat2')
		neuroShield.train_GS_WC('trainModel/Cat2_'+ str(x) +'.png',2)
		#print('training cat3')
		neuroShield.train_GS_WC('trainModel/Cat3_'+ str(x) +'.png',3)
		#print('training cat4')
		neuroShield.train_GS_WC('trainModel/Cat4_'+ str(x) +'.png',4)
	print('Training completed...')
	
def learnWithCrop_based():
	logger.debug("Learning images with crop")
	#print('training cat1')
	neuroShield.train_GS_WC('trainModel/Cat1_'+ str(0) +'.png',1)
	#print('training cat2')
	neuroShield.train_GS_WC('trainModel/Cat2_'+ str(0) +'.png',2)
	#print('training cat3')
	neuroShield.train_GS_WC('trainModel/Cat3_'+ str(0) +'.png',3)
	#print('training cat4')
	neuroShield.train_GS_WC('trainModel/Cat4_'+ str(0) +'.png',4)
	print('Training completed...')
	
def learnWithCrop_angle_brightness():
	for x in range(6):
		logger.debug("Learning images with crop")
		#print('training cat1')
		neuroShield.train_GS_WC_brightness('trainModel/Cat1_'+ str(x) +'.png',1)
		#print('training cat2')
		neuroShield.train_GS_WC_brightness('trainModel/Cat2_'+ str(x) +'.png',2)
		#print('training cat3')
		neuroShield.train_GS_WC_brightness('trainModel/Cat3_'+ str(x) +'.png',3)
		#print('training cat4')
		neuroShield.train_GS_WC_brightness('trainModel/Cat4_'+ str(x) +'.png',4)
	print('Training completed...')
	
def runTest2():
	cat1 = 0
	cat2 = 0
	cat3 = 0
	cat4 = 0
	nocount = 0
	print('Starting Test2...')
	for x in range(4):		
		print('Testing category : ' +str(x+1))
		logger.debug("Testing category : "+str(x+1))
		for i in range(15):
			logger.debug('cat 1 : ' +str(cat1))
			logger.debug('cat 2 : ' +str(cat2))
			logger.debug('cat 3 : ' +str(cat3))
			logger.debug('cat 4 : ' +str(cat4))
			img = 'TestData/Cat' + str(x+1) +'_'+ str(i) + '.png'
			dist,cat,nid = neuroShield.recogn_W_crop(img)
			#print(dist,cat,nid)
			if(cat != (x+1)):
				nocount = nocount +1
				logger.debug("No count : " +str(nocount))
			if(x == 0 and cat == 1):
				cat1 = cat1 + 1
			if(x ==1 and cat == 2):
				cat2 = cat2 + 1
			if(x ==2 and cat == 3):
				cat3 = cat3 + 1
			if(x ==3 and cat == 4):
				cat4 = cat4 + 1
			
	print('cat 1 :' + str(cat1))
	print('cat 2 :' + str(cat2))
	print('cat 3 :' + str(cat3))
	print('cat 4 :' + str(cat4))
	logger.debug("Printing Final Results")
	logger.debug("cat 1 : " +str(cat1))
	logger.debug("cat 2 : " +str(cat2))
	logger.debug("cat 3 : " +str(cat3))
	logger.debug("cat 4 : " +str(cat4))
	logger.debug("No Count : " +str(nocount))
	logger.debug("Count : " +str(40-nocount))
	
def learnWoutCrop_angle():
	for x in range(6):
		logger.debug("Learning images without crop")
		#print('training cat1')
		neuroShield.train_GS_WOC('trainModel/Cat1_'+ str(x) +'.png',1)
		#print('training cat2')
		neuroShield.train_GS_WOC('trainModel/Cat2_'+ str(x) +'.png',2)
		#print('training cat3')
		neuroShield.train_GS_WOC('trainModel/Cat3_'+ str(x) +'.png',3)
		#print('training cat4')
		neuroShield.train_GS_WOC('trainModel/Cat4_'+ str(x) +'.png',4)
	print('Training completed...')
	
	
def learnWoutCrop_based():
	logger.debug("Learning images without crop")
	#print('training cat1')
	neuroShield.train_GS_WOC('trainModel/Cat1_'+ str(0) +'.png',1)
	#print('training cat2')
	neuroShield.train_GS_WOC('trainModel/Cat2_'+ str(0) +'.png',2)
	#print('training cat3')
	neuroShield.train_GS_WOC('trainModel/Cat3_'+ str(0) +'.png',3)
	#print('training cat4')
	neuroShield.train_GS_WOC('trainModel/Cat4_'+ str(0) +'.png',4)
	print('Training completed...')

def learnWoutCrop_angle_brightness():
	for x in range(6):
		logger.debug("Learning images without crop")
		#print('training cat1')
		neuroShield.train_GS_WOC_WB('trainModel/Cat1_'+ str(x) +'.png',1)
		#print('training cat2')
		neuroShield.train_GS_WOC_WB('trainModel/Cat2_'+ str(x) +'.png',2)
		#print('training cat3')
		neuroShield.train_GS_WOC_WB('trainModel/Cat3_'+ str(x) +'.png',3)
		#print('training cat4')
		neuroShield.train_GS_WOC_WB('trainModel/Cat4_'+ str(x) +'.png',4)
	print('Training completed...')
	
def runTest1():
	cat1 = 0
	cat2 = 0
	cat3 = 0
	cat4 = 0
	nocount = 0
	print('Starting Test1...')
	for x in range(4):		
		print('Testing category : ' +str(x+1))
		logger.debug("Testing category : "+str(x+1))
		for i in range(15):
			logger.debug('cat 1 : ' +str(cat1))
			logger.debug('cat 2 : ' +str(cat2))
			logger.debug('cat 3 : ' +str(cat3))
			logger.debug('cat 4 : ' +str(cat4))
			img = 'TestData/Cat' + str(x+1) +'_'+ str(i) + '.png'
			dist,cat,nid = neuroShield.recogn_Wout_crop(img)
			#print(dist,cat,nid)
			if(cat != (x+1)):
				nocount = nocount +1
				logger.debug("No count : " +str(nocount))
			if(x == 0 and cat == 1):
				cat1 = cat1 + 1
			if(x ==1 and cat == 2):
				cat2 = cat2 + 1
			if(x ==2 and cat == 3):
				cat3 = cat3 + 1
			if(x ==3 and cat == 4):
				cat4 = cat4 + 1
	print('cat 1 :' + str(cat1))
	print('cat 2 :' + str(cat2))
	print('cat 3 :' + str(cat3))
	print('cat 4 :' + str(cat4))
	logger.debug("Printing Final Results")
	logger.debug("cat 1 : " +str(cat1))
	logger.debug("cat 2 : " +str(cat2))
	logger.debug("cat 3 : " +str(cat3))
	logger.debug("cat 4 : " +str(cat4))
	logger.debug("No Count : " +str(nocount))
	logger.debug("Count : " +str(100-nocount))
	


		



def testRecogn():
	cat1_count = 0
	cat2_count = 0
	cat3_count = 0
	cat4_count = 0
	for i in range(50):
		img = cv.imread('test/test_cat1' + str(i) + '.png')
		dist,cat,nid = neuroShield.recogn('recog/recog.png')
		print(dist,cat,nid)
		if(cat == 1):
			cat1_count = cat1_count + 1
			
	for i in range(50):
		img = cv.imread('test/test_cat2' + str(i) + '.png')
		dist,cat,nid = neuroShield.recogn('recog/recog.png')
		print(dist,cat,nid)
		if(cat == 2):
			cat2_count = cat2_count + 1
				
	for i in range(50):
		img = cv.imread('test/test_cat3' + str(i) + '.png')
		dist,cat,nid = neuroShield.recogn('recog/recog.png')
		print(dist,cat,nid)
		if(cat == 3):
			cat3_count = cat3_count + 1
	
	for i in range(50):
		img = cv.imread('test/test_cat4' + str(i) + '.png')
		dist,cat,nid = neuroShield.recogn('recog/recog.png')
		#print(dist,cat,nid)
		if(cat == 4):
			cat4_count = cat4_count + 1
			
	percentageOfAcc_cat1 = (cat1_count / 50.0) * 100
	percentageOfAcc_cat2 = (cat2_count / 50.0) * 100
	percentageOfAcc_cat3 = (cat3_count / 50.0) * 100
	percentageOfAcc_cat4 = (cat4_count / 50.0) * 100
	overall = (percentageOfAcc_cat1 + percentageOfAcc_cat2 + percentageOfAcc_cat3 + percentageOfAcc_cat4) / 4
	
	print('percentageOfAcc_cat1 = ' + str(percentageOfAcc_cat1))
	print('percentageOfAcc_cat2 = ' + str(percentageOfAcc_cat2))
	print('percentageOfAcc_cat3 = ' + str(percentageOfAcc_cat3))
	print('percentageOfAcc_cat4 = ' + str(percentageOfAcc_cat4))
	print('overall = ' + str(overall))
			
			
i=15
redBtn = Button(13) 
	

					
def testAccuracy():	
	print("\n\nLearn without Crop Accuracy")		
	learnWoutCrop_based()
	runTest1()
	neuroShield.clearData()
	
	print("\n\nLearn without Crop with Angle Accuracy")
	learnWoutCrop_angle()
	runTest1()
	neuroShield.clearData()
	
	print("\n\nLearn without Crop with Angle and Brightness Accuracy")
	learnWoutCrop_angle_brightness()
	runTest1()
	neuroShield.clearData()
	
	print("\n\nLearn with Crop Accuracy")
	learnWithCrop_based()
	runTest2()
	neuroShield.clearData()
	
	print("\n\nLearn with Crop with Angle Accuracy")
	learnWithCrop_angle()
	runTest2()
	neuroShield.clearData()
	
	print("\n\nLearn with Crop with Angle and Brightness Accuracy")
	learnWithCrop_angle_brightness()
	runTest2()
	
def trainingeasy():
	for x in range(0,15):
		for y in range(3):
			time.sleep(1)
			print("waiting" + str(y))
		time.sleep(1)
		print("takeing ")
		camera.captureImage("TestData/Cat4_"+str(x)+".png")
	
#testAccuracy()
#trainingeasy()
#learnWithCrop_angle_brightness()
learnWithCrop_angle_brightness()
runTest2()
#neuroShield.train_GS_WC('trainModel/Cat1_1.png',1)
#neuroShield.recogn_W_crop('TestDataFixed/Cat1_1.png')
