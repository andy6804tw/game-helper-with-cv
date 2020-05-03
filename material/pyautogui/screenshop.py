import imutils
import pyautogui
import cv2

while(1):
    pyautogui.pixel(965,442)
    pyautogui.screenshot("screenshot.png")
    image = cv2.imread("screenshot.png")
    cv2.imshow("Screenshot", image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()