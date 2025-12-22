import cv2 as cv
import numpy as np

cap = cv.VideoCapture("walking.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=100)

def process(image):
    mask = fgbg.apply(image)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    cv.imshow("mask", mask)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0,255,0), 2, 8)
        cv.circle(image, (int(rect[0][0]), int(rect[0][1])), 2, (255,0,0), 2, 8, 0)
    return image

while True:
    ret, frame = cap.read()
    cv.imshow("input", frame)
    result = process(frame)
    cv.imshow("result", result)
    k = cv.waitKey(50) & 0xff
    if k == 27:
        break
