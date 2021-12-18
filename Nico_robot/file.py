import cv2
import fuction_pose as pose
import function_object as obj
import time

cap = cv2.VideoCapture(2)
cap.set(3,640)
cap.set(4,480)

##########################
detector = pose.poseDetection(detectionConf = 0.8, trackingconf = 0.8)
##########################
pTime = 0



while True:
    success, img = cap.read()
    objImg,info,objectId = obj.getObjects(img,True,nms=0.45,threshold=0.5,objects=['person'])
    ##################
    print(objectId)
    ##################

    # img = detector.findPose(img, True)
    # lmList = detector.points(img, False)
    if objectId == "person":
        print('person detected')
        img = detector.findPose(img,True)
        # img, status = detector.checkPoints(img)
        # if (status):
        #     print(" Warning ")



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    print(int(fps))
    # cv2.putText(img, str(int(fps)), (15,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),1)
    cv2.imshow("output", img)
    cv2.waitKey(1)