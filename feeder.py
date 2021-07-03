import motion.p3picam as motion_detect
import picamera
from datetime import datetime

motionstate = False # for motion detection
picPath = "/home/pi/code/feeder/motion/motion_pictures/" # location of picture storage folder


#### Get the current time
def getTime():
    currentTime = datetime.now()
    return currentTime
    


###### motion detection code #####################

def captureImage (currentTime, picPath):
    #generate picture name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("picture has been taken")
        




while True:
    motionstate = motion_detect.is_there_motion()
    print(motionstate)
    if motionstate:
        currentTime = getTime()
        captureImage(currentTime, picPath)
        

################################################### 