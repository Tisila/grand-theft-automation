import numpy as np
from PIL import ImageGrab
import cv2
import time

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Cut up the good parts
    finger_parts_vertices = np.array([[465,275],[755,275],[755,835],[465,835],
        ], np.int32)
    processed_img = roi(processed_img, [finger_parts_vertices])
    # Applying binary threshold
    ret,processed_img = cv2.threshold(processed_img,20,255,cv2.THRESH_BINARY)
    # edge detection
    #processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
