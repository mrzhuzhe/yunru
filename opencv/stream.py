from operator import xor
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FPS, 1)

fps = cap.get(cv.CAP_PROP_FPS)
print(fps)

def my_line(img, start, end):
    thickness = 2
    line_type = 8
    cv.line(img,
             start,
             end,
             (0, 0, 0),
             thickness,
             line_type)             

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # specific a small area s 
    _dx = 200
    _dy = 200
    _dw = 400
    _dh = 400
    _xl = _dx + _dw
    _yl = _dy + _dh
    my_line(gray, (_dx, _dy), (_xl, _dy))
    my_line(gray, (_dx, _dy), (_dx, _yl))
    my_line(gray, (_xl, _dy), (_xl, _yl))
    my_line(gray, (_dx, _yl), (_xl, _yl))
    # e

    # Display the resulting frame
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
    #cony_threshold = 100
    #thresh = cv.Canny(gray, cony_threshold, 1.25 * cony_threshold)

    # 显示等高线特定图案 s
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # Iterate through each contour
    result = []          ## 空列表
    centerPoints = []

    for c in contours:
        x,y,w,h = cv.boundingRect(c)
        #   filter outer point
        if (x > _dx and x + w < _xl and y > _dy and y + h < _yl and w < 45 and w > 15 ):
            
            #cv.rectangle(imgray, (x, y), (x+w, y+h), (255, 0, 255), 2)
            rect = cv.minAreaRect(c)
            box = cv.boxPoints(rect)
            box = np.int0(box)

            #   重算长宽
            _x, _y = np.int0((box[2] + box[0])/2)
            _w = np.linalg.norm(box[1] - box[0])
            _h = np.linalg.norm(box[2] - box[1])
            _vec1 = box[2] - [_x, _y]
            _vec2 = [_w/2, _h/2]
            _arccos = np.arccos(_vec1.dot(_vec2)/(np.linalg.norm(_vec1) * np.linalg.norm(_vec2)))
            #if (_w > 100 and _h > 100 and _w < 150 and _h < 150  ):
            if (_w / _h > 0.5 and _w / _h < 1.5 ):
                centerPoints.append([_x, _y])
                cv.drawMarker(gray, (_x, _y), (255,0,0))
                cv.putText(gray, "x: {0}, y: {1}, arccos: {2}".format(_x, _y, _arccos), (_x, _y), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
                result.append(box) 


    cv.drawContours(gray, result, -1, (255,255,0), 3)
    # 显示等高线特定图案 e
    

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

