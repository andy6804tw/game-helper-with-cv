import mss


with mss.mss() as sct:
    sct.shot(mon=1, output='fullscreen.png')