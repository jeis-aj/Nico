import cv2

# threshold = 0.45
classNames = []
classFiles = 'coco.names'
with open(classFiles,'rt') as f:
    classNames = f.read().strip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img,draw=True, nms=0.5,threshold=0.45,objects=[]):
    global className
    classIds, confs, bbox  = net.detect(img,nmsThreshold=nms,confThreshold=threshold)
    if len(objects) == 0:
        objects = classNames
    objectInfo = []
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(),bbox):
            className = classNames[classId-1]
            if className in objects:
                if (draw):
                    objectInfo.append([box, className])
                    cv2.rectangle(img,box,color=(0,255,255),thickness=1)
                    cv2.putText(img,classNames[classId-1],(box[0]+10,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    # cv2.putText(img,str(round(confidence*100,2)),(box[0]+90,box[1]+30),
                    #             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo,className

if __name__ == "__main__":
    cap = cv2.VideoCapture(2)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        success, img = cap.read()
        result,objects,id = getObjects(img,draw=True,nms=0.6,threshold=0.45,objects=['person'])
        if id == "person":
            print("a person ")
        print(id)
        cv2.imshow("output",result)
        cv2.waitKey(1)

