import cv2
import mediapipe as mp
import serial
ser=serial.Serial('COM5',9600)


kamera=cv2.VideoCapture(0)
cizim=mp.solutions.drawing_utils
el_mod=mp.solutions.hands
mavi=(255,0,0)
yesil=(0,255,0)
with el_mod.Hands(static_image_mode=True) as eller:
    while True:
        ret, frame=kamera.read()
        frame=cv2.flip(frame,1)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=eller.process(rgb)

        yukseklik,genislik,_=frame.shape

        if result.multi_hand_landmarks:
            for ellandmark in result.multi_hand_landmarks:
                for koordinat in el_mod.HandLandmark:
                    koordinat1=ellandmark.landmark[4]
                    koordinat2 = ellandmark.landmark[20]
                    center1 = (int(koordinat1.x * genislik), int(koordinat1.y * yukseklik))
                    center2 = (int(koordinat2.x * genislik), int(koordinat2.y * yukseklik))
                    cv2.circle(frame,center1,6,(0,0,255),-1)
                    cv2.circle(frame,center2,6, (0, 0, 255), -1)
                    cv2.line(frame,center1,center2,mavi,4)
                    mesafe=int(abs(koordinat2.x-koordinat1.x)*genislik)
                    #print(mesafe)
                    org = (80,80)
                    cv2.putText(frame,"Mesafe: " + str(mesafe),org,cv2.FONT_HERSHEY_SIMPLEX,1,yesil,3)
                    if mesafe>220:
                        ser.write('A'.encode())
                    elif mesafe > 180:
                        ser.write('B'.encode())
                    elif mesafe > 140:
                        ser.write('C'.encode())
                    elif mesafe > 100:
                        ser.write('D'.encode())
                    elif mesafe > 60:
                        ser.write('E'.encode())
                    elif mesafe > 30:
                        ser.write('F'.encode())
                    else:
                        ser.write('G'.encode())

        cv2.imshow("Görüntü",frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break
kamera.release()
cv2.destroyAllWindows()