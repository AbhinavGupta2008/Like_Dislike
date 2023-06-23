




import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)



finger_tips =[8, 12, 16, 20]
thumb_tip= 4



def likeDislike(image,hand_landmarks):
    fingers=[]
    is_closed=0
    
    if hand_landmarks:
        
        
        landmarks=hand_landmarks[0].landmark
        thumbtip_y=landmarks[thumb_tip].y
        thumbB_y=landmarks[thumb_tip-4].y
    

    
    
        
        for lm_index in finger_tips:
            fintip_x=landmarks[lm_index].x
            fintipb_x=landmarks[lm_index-2].x
            
            if lm_index!=4:
                if fintip_x<fintipb_x:
                    fingers.append(1)
                    
                    

                if fintip_x>fintipb_x:
                    fingers.append(0)
        finc=fingers.count(1)
        

        if finc==4:
            is_closed=1
            print("true")
        else:
            is_closed=0
            print("false")
            print(f'fingers: {finc}')
            


        if is_closed==1:
            if thumbtip_y>thumbB_y:
                cv2.putText(image,"Dislike",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
       
                

            if thumbtip_y<thumbB_y:
                cv2.putText(image,"Like",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            
            
        
                    
            
        
        
        
def drawHandLanmarks(image, hand_landmarks):

    # Darw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)


while True:
    ret,image = cap.read()
    image = cv2.flip(image, 1)
    h,w,c = image.shape
    results = hands.process(image)


    # Get landmark position from the processed result
    hand_landmarks = results.multi_hand_landmarks

    # Draw Landmarks
    drawHandLanmarks(image, hand_landmarks)

    # Get Hand Fingers Position        
    likeDislike(image,hand_landmarks)
    cv2.imshow("hand tracking", image)
    cv2.waitKey(1)
cv2.destroyAllWindows()
