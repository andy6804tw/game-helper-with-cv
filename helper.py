import time
import cv2
import mss
import numpy as np
global roi

def find_different(arr):
    for num,i in enumerate(arr):
        if (arr.count(i)==1):
            return num
    else:
        return 0

with mss.mss() as sct:  
    sct.shot(mon=0, output='screenshot.png')
    # Read image
    im = cv2.imread("screenshot.png")
    cv2.namedWindow("ROI selector",0)
    cv2.resizeWindow("ROI selector", 640, 480)
    # Select ROI
    roi = cv2.selectROI(im, False, False)
    cv2.destroyWindow("ROI selector")
    # Part of the screen to capture
    left=roi[0]/2
    top=roi[1]/2
    width=roi[2]/2
    height=roi[3]/2
    monitor = {"top": top, "left": left, "width": width, "height": height}
    print(roi)
    while(1):
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        
        #####
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.2,10)
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            cycleArray = []
            for (x, y, r) in circles:
                cycleArray.append(list(img[y,x,:]))
                # draw the circle in the output image, and draw a center point
                # corresponding to the center of the circle
            #print(circles)
            nn = find_different(cycleArray)
            for num,(x, y, r) in enumerate(circles):
                if num==nn:
                    cv2.circle(img, (x, y), r, (0, 255, 0), -1)
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        #####
        # Display the picture
        cv2.namedWindow("Lyto Different Color Helper",0)
        cv2.resizeWindow("Lyto Different Color Helper", 411, 784)
        cv2.imshow("Lyto Different Color Helper", img)


        print("fps: {}".format(1 / (time.time() - last_time)))
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

