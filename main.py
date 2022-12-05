from picamera import PiCamera 
from time import sleep 

while true: 
    camera = PiCamera()
    camera.rotation = 180
    camera.resolution = (1024,600)
    camera.framerate = 24
    camera.exposure_mode = auto 
    camera.awb_mode = auto 
    camera.brightness = 50 
    #camera.image_effect = denoise



    camera.start_recording()
    camera.wait_recording(20)
camera.stop_recording




 