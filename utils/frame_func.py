import cv2 as cv
import numpy as np

def crop_frame(frame, new_height, new_width):
    height, width, _ = frame.shape

    if new_width <= width and new_height <= height:
        x1, x2 = int(width/2 - new_width/2), int(width/2 + new_width/2)
        y1, y2 = int(height/2 - new_height/2), int(height/2 + new_height/2)
        return frame[y1:y2, x1:x2]

    return frame

def add_text(image, text, bg=(255, 255, 255), position=None, thickness=cv.FILLED, font=cv.FONT_HERSHEY_PLAIN, text_color=(0, 0, 0)):
    origin, end = position
    edited_image = image.copy()
    cv.rectangle(edited_image, origin, end, bg, thickness, lineType=cv.LINE_AA)
    cv.putText(edited_image, text=text, org=(
        origin[0]+10, origin[1]-10), fontFace=font, fontScale=0.9, color=text_color, lineType=cv.LINE_AA)
    return edited_image

def circle_img(img, centre, radius):
    img = np.array(img)
    mask = np.zeros_like(img)
    mask = cv.circle(mask, centre, radius, (255, 255, 255), cv.FILLED)
    alpha = cv.cvtColor(img, cv.COLOR_RGB2BGRA)
    alpha[:, :, 3] = mask[:, :, 0]
    return alpha