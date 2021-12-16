import cv2 as cv
import sys
import numpy as np

def main():
    height = 620
    width = 440
    image = np.zeros((height, width, 3), np.uint8)      # зануление матрицы пикселей (620х440) в каждой ячейке 3 разряда для RGB пикселя
    font = cv.FONT_HERSHEY_COMPLEX
    window_name = "hw_window"
    
    cv.putText(image, "Hello world!", (0, height //2), font, 1, (150, 0, 150), 2)
    cv.imshow(window_name, image)
    cv.waitKey(0)
    cv.destroyWindow(window_name)
    return

if __name__ == "__main__":
    main()