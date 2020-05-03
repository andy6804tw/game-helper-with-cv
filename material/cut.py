import cv2

# Read image
im = cv2.imread("fullscreen.png")

# Select ROI
r = cv2.selectROI(im, False, False)

# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
print(r)
print(im.shape)
# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)

cv2.destroyAllWindows()