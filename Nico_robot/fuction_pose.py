import cv2
import mediapipe as mp
from time import sleep

class poseDetection():
    def __init__(self,mode = False, complexity = 1, smooth = True,
                 detectionConf = 0.8, trackingconf = 0.8):
        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.detectionConf = detectionConf
        self.trackingconf = trackingconf

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.complexity,self.smooth,
                                     self.detectionConf,self.trackingconf)

    def findPose(self,img,draw=True) -> object:
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img
    def points(self,img,draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0))
        return lmList
    def checkPoints(self,img):
        list = []
        status = False
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                list.append([id, cx, cy])
                if list[12][1] > 370 and list[11][1] > 370 :
                    status = True
        return list, status


#
def main():
    detector = poseDetection()
    cap = cv2.VideoCapture(2)
    while True:
        success, img = cap.read()
        img = detector.findPose(img,True)
        lmList = detector.points(img,False)
        print(lmList)
        # print(lmList[7][1])

        if len(lmList) !=0:#and lmList[17][1] > 460
            if lmList[15][2] > 460  :
                print("fall Detected")
                sleep(1.0)

        cv2.imshow("output", img)
        cv2.waitKey(1)





if __name__ == "__main__":
    main()