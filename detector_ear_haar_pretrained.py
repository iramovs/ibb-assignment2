import cv2, sys
import numpy as np

cascadeLeftEar = cv2.CascadeClassifier("models/haarcascade_mcs_leftear.xml")
cascadeRightEar = cv2.CascadeClassifier("models/haarcascade_mcs_rightear.xml")
class20_set1 = cv2.CascadeClassifier("models/classifier_20_set1_HAAR.xml")
class35_set1 = cv2.CascadeClassifier("models/classifier_35_set1_HAAR.xml")

scaleFactor = 1.05
minNeighbors = 5
model = 0
if (len(sys.argv) > 1):
	scaleFactor = float(sys.argv[1])
	minNeighbors = int(sys.argv[2])
	model = int(sys.argv[3])

imgPath = "test/"
annotPath = "testannot_rect/"


def detect(img):

	if model == 0:
		detectionListLeft = cascadeLeftEar.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
		detectionListRight = cascadeRightEar.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

		return list(detectionListLeft) + list(detectionListRight)

	elif model == 1:
		return class20_set1.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

	elif model == 2:
		return class35_set1.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

def list_to_mask(lst, size):

	mask = np.zeros(size, dtype=int)
	for x, y, w, h in lst:
		mask[y:y+h, x:x+w] = 1
	return mask

	
def vizualization(img, detectionList, annotMask):

	img[annotMask>0, 0] = 0
	img[annotMask>0, 1] = 0

	for x, y, w, h in detectionList:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imwrite('visualization.jpg', img)


def intersection_over_union(detectionMask, annotMask):

	intersection = sum(sum(np.logical_and(detectionMask, annotMask)))
	union = sum(sum(np.logical_or(detectionMask, annotMask)))
	return intersection/union

def precision(detectionMask, annotMask):

	truePositive = sum(sum(np.logical_and(detectionMask, annotMask)))
	falsePositive = sum(sum(np.logical_and(detectionMask, np.logical_not(annotMask))))
	if (truePositive == 0):
		return 0
	return truePositive/(truePositive+falsePositive)

def recall(detectionMask, annotMask):

	truePositive = sum(sum(np.logical_and(detectionMask, annotMask)))
	falseNegative = sum(sum(np.logical_and(np.logical_not(detectionMask), annotMask)))
	return truePositive/(truePositive+falseNegative)


results = np.empty((250,3))
results[:] = np.nan

for i in range(0,250):

	filename = "{0:0=4d}.png".format(i+1)
	img = cv2.imread(imgPath + filename)
	annot = cv2.imread(annotPath + filename)
	annotMask = annot[:,:,0]

	detectionList = detect(img)
	detectionMask = list_to_mask(detectionList, annotMask.shape)

	# vizualization(img, detectionList, annotMask)

	results[i,0] = intersection_over_union(detectionMask, annotMask)
	results[i,1] = precision(detectionMask, annotMask)
	results[i,2] = recall(detectionMask, annotMask)

	print(i, end="\r")

print("scaleFactor={} minNeighbors={} model={}".format(scaleFactor, minNeighbors, model))
print(np.average(results, 0))
print(np.std(results, 0))