import cv2, sys
import numpy as np

trainPath = "train/"
annotPath = "trainannot_rect/"
destPath = "cascade_training/positive_images/"


for i in range(0,750):

	filename = "{0:0=4d}.png".format(i+1)
	img = cv2.imread(trainPath + filename)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	annot = cv2.imread(annotPath + filename)
	annotMask = annot[:,:,0]

	num = 0

	for x in range(annotMask.shape[0]):
		for y in range(annotMask.shape[1]):
			if (annotMask[x,y] > 0):

				for x1 in range(x, annotMask.shape[0]):
					if annotMask[x1, y] == 0:
						break
				
				for y1 in range(y, annotMask.shape[1]):
					if annotMask[x, y1] == 0:
						break

				annotMask[x:x1+1, y:y1+1] = 0

				crop_img = img[x:x1, y:y1]
				print(x, x1, y, y1)
				cv2.imwrite(destPath + "{0:0=4d}-".format(i+1) + "{0:0=2d}.png".format(num+1), crop_img)
				num += 1


