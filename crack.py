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
        cv2.namedWindow("OpenCV",0)
        cv2.resizeWindow("OpenCV", 640, 480)
        
        #####
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.2,10)
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            this = []
            for (x, y, r) in circles:
                this.append(list(img[y,x,:]))
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
            #print(circles)
            nn = find_different(this)
            for num,(x, y, r) in enumerate(circles):
                if num==nn:
                    cv2.circle(img, (x, y), r, (0, 255, 0), 4)
                    cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        #####
        # Display the picture
        cv2.resizeWindow("OpenCV", 411, 784)
        cv2.imshow("OpenCV", img)


        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

