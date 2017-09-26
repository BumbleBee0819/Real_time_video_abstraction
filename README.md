# Real-time-video-abstraction
This python project implements the algorithm in "Real-Time Video Abstraction" (Winnemöller, Olsen, & Gooch, 2006).
This code is part of the final project of CSC 589 (2015S) by Dr. Bei Xiao.


The algorithm includes the following steps.
1) Convert the input image from RGB space to CIELab space.
    "color.rgb2lab" is used to do the conversion, and separate the luminance channel (L) and chrominance channel (a, b).

2) Bilateral filter.
3) Color quantization of L channel.
4) DoG Edge detection.
5) Color space conversion.

Demo results:
Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![](https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final1.jpg)  |  ![](https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage3.jpg)



![alt text](https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final2.jpg)
![alt text](https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final3.jpg)
