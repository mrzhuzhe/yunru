import numpy as np
import cv2 as cv
import os
import time

cap = cv.VideoCapture(0)

# 设置分辨率
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

cap.set(cv.CAP_PROP_FOCUS, 170)  

# 改变焦距
def on_trackbar(val):
    cap.set(cv.CAP_PROP_FOCUS, val)  

def on_record_start():
    _record = True
    print("开始录制")
    
def on_record_end():
    _record = False
    print("停止录制")

def save_pics(_name, frame):
    cv.imwrite(_name + ".jpg", frame)
    print(_name, "已保存")

# 设置fps （无效）
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')

#out = cv.VideoWriter('./out/output.mp4', fqourcc, 2.0, (640,  480))
_record = False 

# 输出文件夹
output = "./out/" + str(time.time()) + "/"
count = 0
_frameCount = 0

# 每次新建一个文件夹
os.mkdir(output)

# 设置UI
cv.namedWindow("frame", cv.WINDOW_NORMAL)
cv.resizeWindow("frame", 1280, 720)
# 焦距
cv.createTrackbar("jiaoju", "frame" , 170, 255, on_trackbar)

# qt 有问题
#cv.createButton('record start', on_record_start)
#cv.createButton('record end', on_record_end)

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
        _record = True
        print("开始录制")
    
    if cv.waitKey(1) == ord('e'):
        _record = False
        print("停止录制")

    
    if cv.waitKey(1) == ord('p'):
        _name = output + "/cap_" + str(count)
        save_pics(_name, frame)
        count += 1

    if _record:
        if _frameCount % 10 == 0: 
            _name = output + str(count)             
            save_pics(_name, frame)
            count += 1
        _frameCount += 1

    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
#out.release()
cv.destroyAllWindows()