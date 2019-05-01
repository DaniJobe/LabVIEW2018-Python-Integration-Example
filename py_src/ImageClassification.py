import numpy as np
import cv2
import os

def convertToCV (image):
    npimage = np.array(image)
    ## Convert array to R, G and B Arrays ##
    rArray = npimage//65536
    gbArray = npimage%65536
    gArray = gbArray//256
    bArray = gbArray%256
    
    ## Convert R, G and B Arrays to one (3D) RGB Array ##
    rgbArray = np.dstack((bArray,gArray,rArray))

    image_array = np.uint8(rgbArray)
    return image_array

def convertToLV (npImage):
    ## Convert Numpy Array back to LabVIEW Color Image
    b = npImage[:, :, 0]
    g = npImage[:, :, 1]
    r = npImage[:, :, 2]

    r = r*65536
    g = g*256

    image = r+g+b

    return (image.tolist())
    
def findFaces(lvimage, scalefactor = 1.1, neighbors = 5):

    # Convert image to OpenCV image
    image_array = convertToCV(lvimage)
    
    #just making a copy of image passed, so that passed image is not changed 
    img_copy = image_array.copy()          
  
    #get path for the classifier to use
    training_set = os.path.dirname(os.path.abspath(__file__))+ '\data\haarcascade_frontalface_alt.xml'
	
    #get the training set
    face_cascade = cv2.CascadeClassifier(training_set)
    
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)          
    
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scalefactor, minNeighbors=neighbors);          
    
    #go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)              

    return (convertToLV(img_copy))

def findCorners (lvimage):
    # Convert image to OpenCV image
    img = convertToCV(lvimage)

    #make it black and white
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # find Harris corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    dst = np.uint8(dst)

    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

    # Now draw them
    res = np.hstack((centroids,corners))
    res = np.int0(res)
    img[res[:,1],res[:,0]]=[0,0,255]
    img[res[:,3],res[:,2]] = [0,255,0]

    #Package the corner locations as lists of tuples (arrays of clusters in LabVIEW)
    X = res[:,1]
    Y = res[:,0]
    oneCornerSet = list(zip(X, Y))
    otherCornerSet = list(zip(res[:,3],res[:,2]))

    #return to LabVIEW
    return (convertToLV(img), oneCornerSet, otherCornerSet)
