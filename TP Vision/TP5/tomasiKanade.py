import cv2
import numpy as np


#read images hna later on
img1 = cv2.imread('images/image1.jpg')
img2 = cv2.imread('images/image2.jpg')
img3 = cv2.imread('images/image3.jpg')
img4 = cv2.imread('images/image4.jpg')

sift = cv2.SIFT_create()


kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
kp3, des3 = sift.detectAndCompute(img3, None)
kp4, des4 = sift.detectAndCompute(img4, None)


matches = cv2.BFMatcher()

matches12 = matches.knnMatch(des1, des2, k=2)
matches13 = matches.knnMatch(des1, des3, k=2)
matches14 = matches.knnMatch(des1, des4, k=2)
matches23 = matches.knnMatch(des2, des3, k=2)
matches24 = matches.knnMatch(des2, des4, k=2)
matches34 = matches.knnMatch(des3, des4, k=2)

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=None,
                   flags=2)

good1 = []
for m, n in matches12:
    if m.distance < 0.75 * n.distance:
        good1.append(m)

resultImage1 = cv2.drawMatches(img1, kp1, img2, kp2, good1, None, **draw_params)
cv2.imwrite("images/matches1.jpg", resultImage1)
# cv2.imshow('matches1', resultImage1)
# cv2.waitKey(0)

# good2 = []
# for m, n in matches2:
#     if m.distance < 0.75 * n.distance:
#         good2.append(m)

# resultImage2 = cv2.drawMatches(img3, kp3, img4, kp4, good2, None, **draw_params)
# cv2.imwrite("images/matches2.jpg", resultImage2)
# # cv2.imshow('matches2', resultImage2)
# # cv2.waitKey(0)

# good3 = []
# for m, n in matches3:
#     if m.distance < 0.75 * n.distance:
#         good3.append(m)

# resultImage3 = cv2.drawMatches(img1, kp1, img3, kp3, good3, None, **draw_params)
# cv2.imwrite("images/matches3.jpg", resultImage3)
# # cv2.imshow('matches3', resultImage3)
# # cv2.waitKey(0)

# good4 = []
# for m, n in matches4:
#     if m.distance < 0.75 * n.distance:
#         good4.append(m)

# resultImage4 = cv2.drawMatches(img2, kp2, img4, kp4, good4, None, **draw_params)
# cv2.imwrite("images/matches4.jpg", resultImage4)
# # cv2.imshow('matches4', resultImage4)
# # cv2.waitKey(0)
