
import cv2
import numpy as np
import time
import os
#code here
#main vriables
thresh =0.3;
Rx=165;
Ry =126;
Gx=505;
Gy=127;
Bx=337;
By=127;
Rxx=292;
Ryy =286;
Gxx=633;
Gyy=286;
Bxx=462;
Byy=286;
#color functions :
def isred(R,th) :
    #1 - thresholding
    #r2,t2 = cv2.threshold(R[:,:,2],127,255,cv2.THRESH_BINARY)
    #t2=~t2;
    t2 = cv2.inRange(R,[0,0,100],[50,50,255])

    #2 - sum
    ratio2 = sum(sum(t2))/sum(sum(np.ones(t2.shape)));
    #print ratio2
    #return if >theshold
    if (ratio2>=th) :
        return True;
    else :
        return False;

def isgreen(G,th):
    #1 - thresholding
    # r,t = cv2.threshold(G[:,:,1],127,255,cv2.THRESH_BINARY)
    # t=~t;
    t = cv2.inRange(G, [0, 100, 0], [50, 255, 50])

    #2 - sum
    ratio = sum(sum(t))/sum(sum(np.ones(t.shape)));
    #print ratio
    #return if >theshold
    if (ratio>=th) :
        return True;
    else :
        return False;

def isblue(B,th):
    #1 - thresholding
    #r1,t1 = cv2.threshold(B[:,:,0],127,255,cv2.THRESH_BINARY)
    #t1=~t1;
    t1 = cv2.inRange(B, [100, 0, 0], [255, 50, 50])
    #2 - sum
    ratio1 = sum(sum(t1))/sum(sum(np.ones(t1.shape)));
    #print ratio1
    #return if >theshold
    if (ratio1>=th) :
        return True;
    else :
        return False;

#camera and thread making

cap = cv2.VideoCapture(1);



cv2.startWindowThread();
cv2.namedWindow("mon",1);

#while loop
#img =cv2.imread("blue.png");
#cv2.imshow("mon",img);    
#cv2.waitKey()
while (True):
#m =['green.png','blue.png','red.png']
#for i in m:
    [ret,img] = cap.read();
    #img =cv2.imread(i);
    cv2.imshow("mon",img);
    #cv2.waitKey()
    
    R = img[Ry:Ryy,Rx:Rxx];
    G = img[Ry:Ryy,Gx:Gxx];
    B = img[By:Byy,Bx:Bxx];
    #cv2.imshow("mon",R);
    #cv2.waitKey()
    #cv2.imshow("mon",G);
    #cv2.waitKey()
    #cv2.imshow("mon",B);
    #cv2.waitKey()
    if(isred(R,thresh)) :
        print "Red Valve Open";
    if (isblue(B,thresh)):
        print "Blue Valve Open";
    if(isgreen(G,thresh)):
        print "Green Valve Open";
    
    
