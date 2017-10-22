# pi-opencv

OpenCV-related scripts for the Raspberry Pi.

## Installing OpenCV

To install OpenCV on the Raspberry Pi, use `apt-get`.

## Take a Photo with OpenCV

To capture a photo from a webcam or USB camera using OpenCV:

```
$ python take_photo.py
```

Note that this imports OpenCV, which takes several seconds
and eats up about 10% of the memory available on the Pi.

If time is a factor, the photo-taking functionality should be 
incorporated into a Python script running continuously in the background.
(More likely.)

If memory use is a factor, the photo-taking functionality 
should be in a separate script that is only run when needed.
(Less likely.)
