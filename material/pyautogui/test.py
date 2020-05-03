import cv2
import numpy as np
import os
import pyautogui
import cv2


while(True):
    img = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Screenshot", image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()