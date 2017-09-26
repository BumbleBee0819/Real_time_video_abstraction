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
<img src="https://openclipart.org/image/2400px/svg_to_png/28580/kablam-Number-Animals-1.png" width="200"/> <img src="https://openclipart.org/download/71101/two.svg" width="300"/>

