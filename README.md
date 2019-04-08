[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/BumbleBee0819/Real-time-video-abstraction/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# Real time video abstraction
This python project implements the algorithm described in "Real-Time Video Abstraction" (Winnemöller, Olsen, & Gooch, 2006).
This code is part of the final project of CSC 589 (2015 Spring) by Dr. Bei Xiao.


The algorithm includes the following steps.
1) Convert the input image from RGB space to CIELab space.
    "color.rgb2lab" is used to do the conversion, which separates the luminance channel (L) from the chrominance channel (a, b).

2) Bilateral filter.
3) Color quantization of L channel.
4) DoG Edge detection.
5) Color space conversion.


Demo results:
<br>
<img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage1.jpg" width="400"/> <img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final1.jpg" width="400"/>
<br>
<img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage2.png" width="400"/> <img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final2.jpg" width="400"/>
<br>
<img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/TestImage3.jpg" width="400"/> <img src="https://github.com/BumbleBee0819/Real-time-video-abstraction/blob/master/results/Final3.jpg" width="400"/>
