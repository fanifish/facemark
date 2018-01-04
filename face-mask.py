from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2


#apply lines on image using opencv
def drawLines(i, j, shape, image, cycle=False):
    for k in range(i, j):
        x1, y1 = shape[k-1]
        x2, y2 = shape[k]
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),1)
        if cycle:
            x1, y1 = shape[i-1]
            x2, y2 = shape[j-1]
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),1)

def main(args):
  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor(args["shape_predictor"])
  # load the input image, resize it, and convert it to grayscale
  image = cv2.imread(args["image"])
  image = imutils.resize(image, width=500)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
  # detect faces in the grayscale image
  rects = detector(gray, 1)
  # loop over the face detections
  for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
 
    # convert dlib's rectangle to a OpenCV-style bounding box
    # [i.e., (x, y, w, h)], then draw the face bounding box
    (x, y, w, h) = face_utils.rect_to_bb(rect)
#    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
    # show the face number
    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
 
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for (x, y) in shape:
      cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
    #draw lines on jaw line
    drawLines(1, 17, shape, image)
    #draw lines on eye brow
    drawLines(18, 22, shape, image)
    drawLines(23, 27, shape, image)
    #draw line on nose
    drawLines(28, 31, shape, image)
    drawLines(32, 36, shape, image)
    #draw line on eye
    drawLines(37, 42, shape, image, cycle=True)
    drawLines(43, 48, shape, image, cycle=True)
    #draw line on outer and inner lips
    drawLines(49, 60, shape, image, cycle=True)
    drawLines(61, 68, shape, image, cycle=True)

    x1,y1 = shape[40]
    x2,y2 = shape[43]
    dist_btn_eyes = x2 - x1
    print('eye dist ' + str(dist_btn_eyes))
    print('eye ratio ' + str((dist_btn_eyes/w)))
  # show the output image with the face detections + facial landmarks
  cv2.imshow("Output", image)
  cv2.waitKey(0)






# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
  help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
  help="path to input image")
args = vars(ap.parse_args())
main(args)





