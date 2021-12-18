import cv2
import mediapipe as mp
import time
# import fuction_pose as fp

cap = cv2.VideoCapture(2)
# cap.set(3,640)
# cap.set(4,480)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (100,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
    cv2.imshow("output", img)
    cv2.waitKey(1)
#





# class poseDetection():
#     def __init__(self,mode = False, complexity = 1, smooth = True,
#                  detectionConf = 0.5, trackingconf = 0.5):
#         self.mode = mode
#         self.complexity = complexity
#         self.smooth = smooth
#         self.detectionConf = detectionConf
#         self.trackingconf = trackingconf
#
#         self.mpDraw = mp.solutions.drawing_utils
#         self.mpPose = mp.solutions.pose
#         self.pose = self.mpPose.Pose(self.mode,self.complexity,self.smooth,
#                                      self.detectionConf,self.trackingconf)
#
#     def findPose(self,img,draw=True):
#         imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         self.results = self.pose.process(imgRGB)
#         if self.results.pose_landmarks:
#             if draw:
#                 self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,
#                                            self.mpPose.POSE_CONNECTIONS)
#         return img
#     def points(self,img,draw=True):
#         lmList = []
#         if self.results.pose_landmarks:
#             for id, lm in enumerate(self.results.pose_landmarks.landmark):
#                 h,w,c = img.shape
#                 cx, cy = int(lm.x*w), int(lm.y*h)
#                 lmList.append([id,cx,cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 5, (255, 0, 0))
#         return lmList
#
#
# #
#def main():
# cap = cv2.VideoCapture(0)
# detector = fp.poseDetection()
# while True:
#     success, img = cap.read()
#     # imgRgb = cv2.cvtColor()
#     img = detector.findPose(img,True)
#     lmList = detector.points(img,True)
#     print(lmList[7][1])
#
#     # if lmList[7][1] > 460:
#     #     print("fall Detected")
#
#     cv2.imshow("output", img)
#     cv2.waitKey(1)
#
#

#

# if __name__ == "__main__":
#     main()