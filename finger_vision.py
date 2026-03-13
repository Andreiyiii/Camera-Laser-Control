import cv2
import mediapipe as mp
import serial
import time

PORT_ARDUINO = 'COM5' 

try:
    arduino = serial.Serial(PORT_ARDUINO, 9600)
    time.sleep(2) 
except:
    print(f"Couldnt connect")
    arduino = None


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    succes, frame = cap.read()
    if not succes:
        break
        
    # flip image to represent direction correctly
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # using RGB instead of BGR
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rezultat = hands.process(imgRGB)
    
    if rezultat.multi_hand_landmarks:
        for handLms in rezultat.multi_hand_landmarks:
            # pointing finger
            x_deget = handLms.landmark[8].x
            y_deget = handLms.landmark[8].y
            
            # X axis on 0 to 180
            unghiX = int(x_deget * 180)
            
            # Y is between 45 si 115 for motor limitation
            unghiY = int(25 + (y_deget * 90))
            
            #send data 
            if arduino:
                comanda = f"X{unghiX}Y{unghiY}\n"
                arduino.write(comanda.encode())
        

            cx, cy = int(x_deget * w), int(y_deget * h)
            cv2.circle(frame, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)


    cv2.imshow("Laser Tracker", frame)
    

    if cv2.waitKey(1) == 27:   # Apasa ESC pentru a iesi
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()