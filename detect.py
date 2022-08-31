import cv2
import numpy as np
from PIL import Image

from run_model import add_rating

class FaceRater:
    @staticmethod
    def detect_face(image_path=None, pil_img=None):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        if pil_img is None:
            # Read the input image
            cv_img = cv2.imread(image_path)
            pil_img = Image.open(image_path).convert('RGB')
        else:
            cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2RGBA)
        # Convert into grayscale
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # we return the maxium rating for that image
        max_rating = 0
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv_img = cv2.rectangle(cv_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            face_box = (x,y,x+w,y+h)
            # Add rating for the face
            rating = add_rating(img=pil_img.crop(face_box))
            if rating > max_rating:
                max_rating = rating
            cv_img =  cv2.putText(cv_img, 
                        str(round(rating,2)),
                        (x+w+round(w/25),y+round(h/2)),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=h/200,
                        color=(0, 0, 255),
                        thickness=round(h/100))
        # Display the output
        # cv2.imshow('img', cv_img)
        # cv2.waitKey()
        return cv_img, max_rating

if __name__=="__main__":
    FaceRater.detect_face("multi_test.jpg")