import cv2 as cv
import os

def main():
    window_name = "original"
    vid_fname = 'test_video.mp4'
    vid_fpath = os.path.join(os.path.dirname(__file__), vid_fname)

    print("\n\n________[VIDEO PROPERTIES]________")
    print("[i] file:   %s" % vid_fpath)
    vCapture = cv.VideoCapture(vid_fpath)
    fps = vCapture.get(cv.CAP_PROP_FPS)     # correct video playback speed (40Hz codec speed???)

    while(vCapture.isOpened()):
        ret, frame = vCapture.read()
        if ret:
            cv.imshow(window_name, frame)
        
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