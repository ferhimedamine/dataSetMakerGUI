# dataSetMakerGUI
python opencv implementation for quickly manually building data sets
Requires opencv (cv2) and numpy

def buildDataSet(images, labels):
  images is 3 or 4d numpy array of images, labels is 1d array of integer labels
  returns nothing but mutates labels based on what input is given
 
press 0-9 to write labels, n for next image, b for back one image and q for quit.

etc:
i = np.zeros([3,50,50])

l = np.zeros([3])

buildDataset(i,l)

