import time
import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    roi=(0,33,587,980)
    left=roi[0]
    top=roi[1]
    width=roi[2]/2-left
    height=roi[3]/2-top
    monitor = {"top": top, "left": left, "width": width, "height": height}

    while(1):
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        cv2.namedWindow("OpenCV",0)
        cv2.resizeWindow("OpenCV", 640, 480)
        # Display the picture
        cv2.imshow("OpenCV", img)


        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break