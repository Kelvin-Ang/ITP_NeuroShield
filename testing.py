from button import *
from neuroshield import *
from imageProcessing import *

neuroShield = NeuroShield()
ip = ImageProcessor()

def trainModel_GS_WOC():
	#4 for loop
	#loop 15x
	for i in range(15):
		neuroShield.train_GS_WOC('trainModel/cat1_' + str(i) + '.png',1)		
	
	for i in range(15):
		neuroShield.train_GS_WOC('trainModel/cat2_' + str(i) + '.png',2)
		
	#for i in range(15):
	#	neuroShield.train_GS_WOC('trainModel/cat3_' + str(i) + '.png',3)

	#for i in range(15):
	#	neuroShield.train_GS_WOC('trainModel/cat4_' + str(i) + '.png',4)
		
def trainModel_GS_WC():
	#4 for loop
	#loop 15x
	for i in range(15):
		neuroShield.train_GS_WC('trainModel/cat1_' + str(i) + '.png',1,i)		
	
	for i in range(15):
		neuroShield.train_GS_WC('trainModel/cat2_' + str(i) + '.png',2,i)
		
	for i in range(15):
		neuroShield.train_GS_WC('trainModel/cat3_' + str(i) + '.png',3,i)

	for i in range(15):
		neuroShield.train_GS_WC('trainModel/cat4_' + str(i) + '.png',4,i)		
	




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
		print(dist,cat,nid)
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
	


					
			
			
