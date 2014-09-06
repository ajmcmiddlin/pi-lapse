pi-lapse
========
Time lapse photography for your raspberry pi.

Scripts under pi are for your pi, scripts under video are (will be - they're not
done yet) for generating a video from your stills.

Hardware
--------
* Raspberry Pi
* Raspberry Pi camera module

Install
-------
These steps get your pi setup and install the init script so that the time lapse
starts when the pi does. This is useful when running headless in a car or some
other environment. Stop after step 3 if you want to kick things off manually.

1. run `raspi-config` and enable your camera if you haven't already
2. update apt and install requirements
	+ `sudo apt-get update`
	+ `sudo apt-get upgrade`
	+ `sudo apt-get install python-picamera`
3. Clone this git repository to your pi
4. Modify pi/pi-lapse.sh to refer to the correct user, and directory. The cmd
   variable may also be modified by adding a numeric argument that specifies the
   number of seconds to wait between pictures. pi-lapse.sh is adapted from
   [fhd's system v init script
   template](https://github.com/fhd/init-script-template)
5. Install the modified init script: `sudo cp pi/pi-lapse.sh /etc/init.d`
6. Set the init script to run at startup `sudo update-rc.d pi-lapse.sh defaults`

Notes
-----
* I'm not a python developer, so this is probably not pythonic. Send me pull
  requests if this really bothers you.
* I hacked this up over a couple of days while on holidays to scratch an itch.
  It's not well tested and comes with no warranty - USE AT OWN RISK.


Useful Links
------------
* [picamera docs](http://picamera.readthedocs.org/en/release-1.8/index.html)
* [creating video from stills with
  ffmpeg](http://programmer-art.org/articles/tutorials/ffmpeg-time-lapse). You
  can use the link-sequence.py script under video to link your photos as described
  here. This link is where I got the code for that script from.
* [fhd's system v init script](https://github.com/fhd/init-script-template)
