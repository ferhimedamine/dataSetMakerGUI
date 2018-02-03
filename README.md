# dataSetMakerGUI
python opencv implementation for quickly manually building data sets
Requires opencv (cv2) and numpy

def buildDataset(images, labels):

  images is 3D or 4D numpy array representing images, labels is 1D array of integers
  returns nothing but mutates labels based on what input is given
 
press 0-9 to write labels, n for next image, b for back one image and q for quit.

etc:
i = np.zeros([3,50,50])

l = np.zeros([3])

buildDataset(i,l)

