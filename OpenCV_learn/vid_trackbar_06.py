import cv2 as cv
import os
import numpy as np

vCapture = ""

def trackBall_callback(pos= 0):
	vCapture.set(cv.CV_CAP_PROP_POS_FRAMES, 1)

def main():
    window_name = "original"
    vid_fname = 'test_video.mp4'
    vid_fpath = os.path.join(os.path.dirname(__file__), vid_fname)
    global vCapture
    vCapture = cv.VideoCapture(vid_fpath)
    fps = vCapture.get(cv.CAP_PROP_FPS)     # correct video playback speed (40Hz codec speed???)
    
    # __________________ [trackbar] __________________
    frames = int(vCapture.get(cv.CAP_PROP_FRAME_COUNT))     # quantity of frames
    currentPosition = 0         # trackball start pos
    width  = int(vCapture.get(cv.CAP_PROP_FRAME_WIDTH))     # width dimension of the video
    height = int(vCapture.get(cv.CAP_PROP_FRAME_HEIGHT))    # height
    startImage = np.zeros((height, width, 3), np.uint8)      # зануление матрицы пикселей (620х440) в каждой ячейке 3 разряда для RGB пикселя
    cv.imshow(window_name, startImage)
    cv.createTrackbar("trackbar_name", window_name, currentPosition, frames, trackBall_callback)
    # _________________________________________________

    print("\n\n________[VIDEO PROPERTIES]________")
    print("[i] file:   %s" % vid_fpath)
    print("[i] count:   %s" % frames)

    while (vCapture.isOpened()):
        ret, frame = vCapture.read()
        if ret:
            cv.imshow(window_name, frame)

        cv.waitKey(int(fps))
        
        # cut last 8bits of waitkey() key ASCII code return by (.. & 1111 1111)
        # !also! waitKey(..) awaits for key to be pressed and meanwhile display (1 frame for 1000ms/Hz of monitor) / changed to CAP_PROP_FPS property
        if cv.waitKey(int(fps)) and 0xFF == ord('q') or ret==False :
            vCapture.release()
            cv.destroyAllWindows()
            break

    else:
        print("Error opening video stream or file")
    return

if __name__ == "__main__":
    main()