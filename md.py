import cv2 as cv

video = cv.VideoCapture('video-path.mp4')
if not video.isOpened():
    print("Error: Could not open video file.Using system camera")
    video=cv.VideoCapture(0)

#subtractor object
subtractor=cv.createBackgroundSubtractorMOG2(20,50)

#visualization
while True:

    ret,frame=video.read()

    if ret:
        mask=subtractor.apply(frame)
        cv.imshow('Mask',mask)

        if cv.waitKey(5)==ord('X') or cv.waitKey(5)==ord('x') :
            break
    else:
        video = cv.VideoCapture('video-path.mp4')
        if not video.isOpened():
            print("Error: Could not open video file.Using system camera")
            video=cv.VideoCapture(0)

cv.destroyAllWindows()
video.release()