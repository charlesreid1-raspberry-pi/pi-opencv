# pi-opencv

OpenCV-related scripts for the Raspberry Pi.

## Installing OpenCV

To install OpenCV on the Raspberry Pi, use `apt-get`.

## Take a Photo with OpenCV

To capture a photo from a webcam or USB camera using OpenCV:

```
$ python take_photo.py
```

Note that this imports OpenCV, which takes a few seconds and 10% of the Pi's memory.
* If time-constrained, incorporate photo-taking in a script that runs in the background.
* If memory-constrained, put in a script that is only run when needed.

