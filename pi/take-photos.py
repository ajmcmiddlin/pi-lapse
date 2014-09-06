#!/usr/bin/env python

import sys
import signal
import time
import picamera

# Take a photo every `interval_s` seconds
interval_s = 5
# Loop guard - set to false to stop taking photos and exit
keep_going = True

# Stop taking photos if we get an interrupt signal (e.g. ctrl+c)
def sigint_handler(signal, frame):
    keep_going = False
    print "keep_going is now " + str(keep_going)

signal.signal(signal.SIGINT, sigint_handler)

# Override default interval if given
if len(sys.argv) > 1:
    interval = sys.argv[1]

camera = picamera.PiCamera()
while keep_going:
    print "keep going in while is " + str(keep_going)
    image_name = time.strftime("pi_lapse_%Y%m%d_%H%M%S.jpg", time.gmtime())
    print "About to capture " + image_name
    before_capture_s = time.time()
    camera.capture(image_name)

    # Take into account the time taken to take the photo when sleeping - we want
    # a capture every interval_s, not just to wait interval_s between starting a
    # capture
    next_sleep_s = interval_s - (time.time() - before_capture_s)
    if next_sleep_s > 0:
        time.sleep(next_sleep_s)

sys.exit(0)
