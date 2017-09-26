# -*- coding: utf-8 -*-
"""
Created on Mon May 01 11:19:52 2015

@author: Wenyan
"""


import cv2  
import matplotlib.pyplot as plt
from skimage import io,color
import numpy as np
from PIL import Image
from scipy import misc
from math import tanh
from scipy import signal


''' 0. Modifiable Parameters'''
# Step 2
# Bilateral filter
s = 9 #Diameter of each pixel neighborhood that is used during filtering
sigmacolor = 17
sigmaspace = 17

# Step 3
# Color quantization
phieq = 20 # controls sharpness of the trasition from one bin to another
# when dealing with faces/fine details, use phieq=2

# Step 5
# Dog edge detection
sigma = 1 # Gaussian sigma
phie = 5  # typically [0.75,5] controls the sharpness of the activation falloff
tau = 0.981 # typically [0,1] control the center-sourround difference required for cell activation




''' 1. Convert RGB Space to CIE LAB Space '''
 
rgb = io.imread('TestImage.jpg')

lab = color.rgb2lab(rgb)
L, a, b = lab[:,:,0], lab[:,:,1], lab[:,:,2]
m1, n1 = L.shape



''' 2. Bilateral Filtering L, a, b Channel Seperately '''

L = np.float32(L)
a = np.float32(a)
b = np.float32(b)

L0 = L
for i in range(3):
    L = cv2.bilateralFilter(L, s, sigmacolor, sigmaspace)
    a = cv2.bilateralFilter(a, s, sigmacolor, sigmaspace)
    b = cv2.bilateralFilter(b, s, sigmacolor, sigmaspace)


## Show bilateral filtered image

#plt.imshow(L,cmap=plt.cm.gray)
#plt.title('L_bilateral filtered')
#plt.xticks([]),plt.yticks([])
#plt.show()

#plt.imshow(a,cmap=plt.cm.gray)
#plt.xticks([]),plt.yticks([])
#plt.title('a_bilateral filtered')
#plt.show()

#plt.imshow(b,cmap=plt.cm.gray)
#plt.xticks([]),plt.yticks([])
#plt.title('b_bilateral filtered')
#plt.show()

lab1 = lab
lab1[:,:,0] = L
lab1[:,:,1] = a
lab1[:,:,2] = b
rgb1 = color.lab2rgb(lab1)

img2 = Image.new( 'RGB', (n1,m1),'black') 
pixel = img2.load()

for i in range(m1):
    for j in range(n1): 
        #pixel[j,i]=((blurL[i,j]),(blura[i,j]),(blurb[i,j]))
        #pixel[j,i]=((L[i,j]),(a[i,j]),(b[i,j]))
        pixel[j,i] = int(255*rgb1[i,j,0]),int(255*rgb1[i,j,1]),int(255*rgb1[i,j,2])
    

misc.imsave('bilateral filtered image.jpg',img2) 




'''3. Color Quantization of L'''

# 8 BINS
def qnearest(f):
    if f >= 0 and f < 100.0/16:
            q=0
    elif f >= 100.0/16 and f < 12.5 + 100.0/16:
        q = 12.5
    elif f >= 12.5+100.0/16 and f < 25 + 100.0/16:
        q = 25
    elif f >= 25 + 100.0/16 and f<37.5 + 100.0/16:
        q = 37.5
    elif f >= 37.5 + 100.0/16 and f < 50 + 100.0/16:
        q = 50
    elif f >= 50 + 100.0/16 and f < 62.5 + 100.0/16:
        q = 62.5
    elif f >= 62.5 + 100.0/16 and f < 75 + 100.0/16:
        q = 75
    elif f >= 75 + 100.0/16 and f < 87.5+100.0/16:
        q = 87.5
    elif f >= 93.75:
        q = 100
   
    '''
    ## 10 BINS
    if f>=0 and f<5:
        q=0
    elif f>=5 and f<15:
        q=10
    elif f>=15 and f<25:
        q=20
    elif f>=25 and f<35:
        q=30
    elif f>=35 and f<45:
        q=40
    elif f>=45 and f<55:
        q=50
    elif f>=55 and f<65:
        q=60
    elif f>=65 and f<75:
        q=70
    elif f>=75 and f<85:
        q=80
    elif f>=85 and f<95:
        q=90
    elif f>=95 and f<100:
        q=100
    '''
    return q
    

Quantum = np.zeros((m1, n1))
for i in range(m1):
    for j in range(n1):
        Quantum[i,j]=qnearest(L[i,j])+5*tanh((L[i,j]-qnearest(L[i,j]))/phieq)
   

L = Quantum
lab1 = lab

lab1[:,:,0] = L
lab1[:,:,1] = a
lab1[:,:,2] = b
        
rgb1 = color.lab2rgb(lab1)

img2 = Image.new( 'RGB', (n1, m1),'black') 
pixel = img2.load()
for i in range(m1):
    for j in range(n1): 
        #pixel[j,i]=((blurL[i,j]),(blura[i,j]),(blurb[i,j]))
        #pixel[j,i]=((L[i,j]),(a[i,j]),(b[i,j]))
        pixel[j,i]=int(255*rgb1[i,j,0]),int(255*rgb1[i,j,1]),int(255*rgb1[i,j,2])
    

misc.imsave('color quantized image.jpg',img2) 

  
  

'''4. DoG Edge Detection'''

def gauss2D(shape,sigma):
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h =np.exp(-(x*x + y*y)/(2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


print 'sigma=',sigma
print 'phie=',phie
print 'tau=',tau


imge = signal.convolve(L0, gauss2D((5,5),sigma), mode = 'same')
imgr = signal.convolve(L0, gauss2D((5,5),sigma * 1.5), mode = 'same')


D = np.zeros((m1,n1))
for i in range(m1):
    for j in range(n1):
        if imge[i,j] - tau * imgr[i,j] > 0:
            D[i,j] = 1
        else:
            D[i,j] = 1 + tanh((imge[i,j] - tau * imgr[i,j]) * phie)


#plt.imshow(D,cmap='gray')
#plt.title('edges')
#plt.xticks([]),plt.yticks([])
#plt.show()
misc.imsave('edges.jpg',D)





''' 5. Overlay the Edges with the Color Image '''
#L=L+50*D

lab2 = lab
lab2[:,:,0] = L
lab2[:,:,1] = a
lab2[:,:,2] = b
        
rgb2 = color.lab2rgb(lab2)


img3 = Image.new('RGB', (n1, m1), 'black') 
pixel = img3.load()
for i in range(m1):
    for j in range(n1): 
        if D[i,j] < 0.1:
            r = g = b = 255 * D[i,j]
        else:
            r = 255 * rgb2[i, j, 0]
            g = 255 * rgb2[i, j, 1]
            b = 255 * rgb2[i, j, 2]
        
        pixel[j,i] = int(r), int(g), int(b)
        #print r,g,b
    

misc.imsave('final.jpg', img3) 






    
    


    
