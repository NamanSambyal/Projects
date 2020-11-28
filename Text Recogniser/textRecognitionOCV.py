import cv2
import pytesseract
from PIL import Image

def gray(img):    # preprocessing gray scale
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"./preprocess/img_gray.png",img)
    
    return img


def blur(img) :   # blur
    
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite(r"./preprocess/img_blur.png",img)    
    
    return img_blur


def threshold(img):  # threshold
                     #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    
    img = cv2.threshold(img, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1]    
    cv2.imwrite(r"./preprocess/img_threshold.png",img)
    
    return img


def contours_text(orig, img, contours):       # text detection
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 

        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 255), 2) 
        
        cv2.imshow('cnt',rect)
        cv2.waitKey()

        # Cropping the text block for giving input to OCR 
        cropped = orig[y:y + h, x:x + w] 

        # Apply OCR on the cropped image 
        config = ('-l eng --oem 1 --psm 3')
        text = pytesseract.image_to_string(cropped, config=config) 

        return text


# Finding contours 

img = Image.open('sample1.png')

imgGgray = gray(img)
imgBlur = blur(imgGray)
imgThresh = threshold(imgBlur)

contours, _ = cv2.findContours(im_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

t = contours_text(_, img, contours)

text_file = open("text.txt", "w")

text_file.write(t)
text_file.close()

