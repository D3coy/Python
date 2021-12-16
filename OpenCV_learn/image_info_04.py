import sys
import numpy as np
import cv2 as cv
import os

def main():
    window_name = "original"
    img_name = 'cat.jpg'
    img_fpath = os.path.join(os.path.dirname(__file__), img_name)
    image = cv.imread(img_fpath, cv.IMREAD_UNCHANGED)

    print("\n\n________[IMAGE PROPERTIES]________")
    print("[i] image:   %s" % img_name)
    print("[i] channels:    %d" % image.shape[2])                       # число каналов картинки (RGB, хотя в OpenCV - BGR )
    print("[i] pixel depth: %d bits" % int(image.dtype.name[-1:]))      # глубина в битах (0-255 . x . x)
    print("[i] width:   %d pixels" % image.shape[0])                    # ширина картинки в пикселях 
    print("[i] height:  %d pixels" % image.shape[1])                    # высота картинки в пикселях
    print("[i] image size:  %d bytes" % image.size)                     # память занимаемая картинкой
    print("[i] width step:  %d bytes" % image.strides[0])               # расстояние между соседними по вертикали точками изображения (число байт в одной строчке картинки)
    
    cv.imshow(window_name, image)
    cv.waitKey(0)
    cv.destroyWindow(window_name)
    return

if __name__ == "__main__":
    main()