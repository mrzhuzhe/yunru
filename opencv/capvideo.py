import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1920)

cap.set(cv.CAP_PROP_FOCUS, 255)  

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')

output = "./out/"

#out = cv.VideoWriter('./out/output.mp4', fourcc, 2.0, (640,  480))
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #frame = cv.flip(frame, 0)
    # write the flipped frame
    #out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('r'):
        _name = output + str(count)
        cv.imwrite(_name + ".jpg", frame)
        print(_name, "saved")
        count += 1

    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
#out.release()
cv.destroyAllWindows()