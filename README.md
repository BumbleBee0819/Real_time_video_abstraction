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
<img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage1.jpg" style="float: left; width: 30%; margin-right: 1%; margin-bottom: 0.5em;">
<p> Original Image </p>
<img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage1.jpg" style="float: left; width: 30%; margin-right: 1%; margin-bottom: 0.5em;">
<p> Processed Image </p>
