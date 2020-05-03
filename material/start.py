import mss
import mss.tools
import cv2


# with mss.mss() as sct:
#     # The screen part to capture
#     monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
#     output = "screenshot.png".format(**monitor)

#     # Grab the data
#     sct_img = sct.grab(monitor)

#     # Save to the picture file
#     mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#     print(output)
with mss.mss() as sct:  
    sct.shot(mon=0, output='screenshot.png')
    # Read image
    im = cv2.imread("screenshot.png")
    cv2.namedWindow("ROI selector",0)
    cv2.resizeWindow("ROI selector", 640, 480)
    # Select ROI
    r = cv2.selectROI(im, False, False)

    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    print(r)
    print(im.shape)
    # Display cropped image
    cv2.namedWindow("Image",0)
    cv2.resizeWindow("Image", 640, 480)

    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)

    cv2.destroyAllWindows()