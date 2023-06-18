import cv2
import mediapipe as mp
import numpy
import math
from app import Ui
import threading
import pyautogui
import tkinter


minx , miny ,maxx, maxy = 1,1,5,5
minset , maxset = False ,False
set_openmenu_point = 0

with open("setting/track.txt", "r") as f:
    setting = f.read().split("\n")

flip =False
if setting[0] == "True":
    flip = True

fix_val = int(float(setting[1]))

hold_1 , hold_2 = 0,0
hold_time = 20
while_hold = hold_time

w_screen = tkinter.Tk().winfo_screenwidth()
h_screen = tkinter.Tk().winfo_screenheight()
thread1 =  threading.Thread(target=Ui.create_menu)



def track():

    def show_menu():
        with open("Ui/val.txt" ,"w") as f :
            f.write("True")
    
    def check_menu():
        with open("Ui/val.txt" ,"r") as f :
            if f.read() == "True":
                return True
            else:
                return False

    def still_run():
            with open("Ui/end.txt" ,"r") as f :
                    if f.read() == "True":
                        return True
                    return False

    def mouse_mod():
            with open("Ui/mouse.txt" ,"r") as f :
                    if f.read() == "True":
                        return True
                    return False



    global minx , miny ,maxx, maxy , minset , maxset , set_openmenu_point , flip , fix_val , hold_1 ,hold_2 ,while_hold
    global w_screen, h_screen

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        static_image_mode=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Could not read frame from webcam.")
                break


            if hold_1 != 0 and hold_1 != 10 or hold_2 != 0 and hold_2 != 10:
                if while_hold <= hold_time:
                    while_hold -= 1
                    if while_hold == 0:
                        hold_1 , hold_2 = 0,0
                        while_hold = hold_time
            elif hold_1 != 0 and hold_1 != 10 and hold_2 != 0 and hold_2 != 10:
                if while_hold <= hold_time:
                    while_hold -= 1
                    if while_hold == 0:
                        hold_1 , hold_2 = 0,0
                        while_hold = hold_time
                        
            if hold_1 == 10 or hold_2 == 10:
                if hold_1 ==10:
                    with open("Ui/mouse.txt" ,"w") as f :
                        f.write("False")

            if hold_1 == 10 and hold_2 == 10:
                if not mouse_mod():
                    show_menu()
            if flip:
                image = cv2.flip(image, 1)

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            hand1_click , hand2_click = False , False
            cv2.rectangle(image,(int(minx),int(miny),int(abs(maxx-minx)),int(maxy)),(0,0,255),1)

            
            if results.multi_hand_landmarks:

                yc , xc = int(image.shape[0]/2), int(image.shape[1]/2)
                cv2.circle(image, (xc, yc), 3, (0, 0, 0), -1)
                
                if results.multi_hand_landmarks[0] :
                        
                    
                    finger_landmarks = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.WRIST]

                    xw1, yw1= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xw1, yw1), 5, (0, 0, 255), -1)

                    finger_landmarks = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
                    
                    xt1, yt1= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xt1, yt1), 5, (0, 255, 0), -1)
                    finger_landmarks = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                    xi1, yi1= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xi1, yi1), 5, (255, 255, 255), -1)


                    if xt1 -fix_val < xi1 < xt1 + fix_val and yt1 -fix_val < yi1 < yt1+fix_val :
                        hand1_click = True
                        if check_menu() and while_hold == hold_time and results.multi_handedness[0].classification[0].label == "Right":
                            pyautogui.click()
                        if mouse_mod() and while_hold == hold_time and results.multi_handedness[0].classification[0].label == "Right":
                            pyautogui.click()

                    if results.multi_handedness[0].classification[0].label == "Left":
                        if xt1 -fix_val < xi1 < xt1 + fix_val and yt1 -fix_val < yi1 < yt1+fix_val :
                            hold_1 += 1
                        if minset == False:
                            minx = xt1
                            miny = yt1


                    
                    if results.multi_handedness[0].classification[0].label == "Right":
                        if xt1 -fix_val < xi1 < xt1 + fix_val and yt1 -fix_val < yi1 < yt1+fix_val :
                            hold_2 += 1

                        cv2.line(image,(xw1,yw1),(xc,yc),(0,0,0))
                        if xw1 >= xc and yw1 <= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(yc-yw1) / numpy.sqrt(abs(yc-yw1)**2 + abs(xc-xw1)**2)) )
                        elif xw1 <= xc and yw1 <= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(xc-xw1) / numpy.sqrt(abs(yc-yw1)**2 + abs(xc-xw1)**2)) ) + 90
                        elif xw1 <= xc and yw1 >= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(yc-yw1) / numpy.sqrt(abs(yc-yw1)**2 + abs(xc-xw1)**2)) ) + 180
                        elif xw1 >= xc and yw1 >= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(xc-xw1) / numpy.sqrt(abs(yc-yw1)**2 + abs(xc-xw1)**2)) )+ 270
                        
                        if check_menu() and not math.isnan(angel):
                            pos_info= ""
                            with open("Ui/pos.txt" , "r") as f:
                                pos_info = f.read()
                            pos_info = pos_info.split("\n")
                            for pos in pos_info:
                                btn_angle = float(pos.split(";")[0])
                                xb,yb = float(pos.split(";")[1]),float(pos.split(";")[2])
                                if (btn_angle-10 <= angel <= btn_angle+10):
                                    pyautogui.moveTo(((w_screen/2)-250+xb), ((h_screen/2)-270+yb))
                        
                        if mouse_mod():
                            if minx <= xi1 <=maxx and miny <= yi1 <= maxy:
                                pyautogui.moveTo((xi1-minx)*(w_screen/(maxx-minx)),(yi1-miny)*(h_screen/(maxy-miny)))

                        if maxset == False:
                            maxx = xt1
                            maxy = (maxx-minx)*(h_screen/w_screen) 
    


                if len(results.multi_hand_landmarks) == 2 :
                        
                    finger_landmarks = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.WRIST]

                    xw, yw= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xw, yw), 5, (0, 0, 255), -1)

                    finger_landmarks = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.THUMB_TIP]
                    
                    xt, yt= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xt, yt), 5, (0, 255, 0), -1)
                    finger_landmarks = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                    xi, yi= int(finger_landmarks.x * image.shape[1]), int(finger_landmarks.y * image.shape[0])
                    cv2.circle(image, (xi, yi), 5, (255, 255, 255), -1)



                    if xt -fix_val < xi < xt + fix_val and yt -fix_val < yi < yt+fix_val :
                        hand2_click = True
                        if check_menu() and while_hold == hold_time and results.multi_handedness[0].classification[0].label == "Right":
                            pyautogui.click()
                        if mouse_mod() and while_hold == hold_time and results.multi_handedness[0].classification[0].label == "Right":
                            pyautogui.click()

                    if results.multi_handedness[1].classification[0].label == "Left":
                        if xt -fix_val < xi < xt + fix_val and yt -fix_val < yi < yt+fix_val :
                            hold_1 += 1
                        if minset == False:
                            minx = xt
                            miny = yt

                    if results.multi_handedness[1].classification[0].label == "Right":
                        if xt -fix_val < xi < xt + fix_val and yt -fix_val < yi < yt+fix_val :
                            hold_2 += 1
                        cv2.line(image,(xw,yw),(xc,yc),(0,0,0))
                        if xw >= xc and yw <= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(yc-yw) / numpy.sqrt(abs(yc-yw)**2 + abs(xc-xw)**2)) )
                        elif xw <= xc and yw <= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(xc-xw) / numpy.sqrt(abs(yc-yw)**2 + abs(xc-xw)**2)) ) + 90
                        elif xw <= xc and yw >= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(yc-yw) / numpy.sqrt(abs(yc-yw)**2 + abs(xc-xw)**2)) ) + 180
                        elif xw >= xc and yw >= yc :
                            angel = numpy.degrees( numpy.arcsin(abs(xc-xw) / numpy.sqrt(abs(yc-yw)**2 + abs(xc-xw)**2)) )+ 270
                        
                        if check_menu() and not math.isnan(angel):
                            pos_info= ""
                            with open("Ui/pos.txt" , "r") as f:
                                pos_info = f.read()
                            pos_info = pos_info.split("\n")
                            for pos in pos_info:
                                btn_angle = float(pos.split(";")[0])
                                xb,yb = float(pos.split(";")[1]),float(pos.split(";")[2])
                                if (btn_angle-10 <= angel <= btn_angle+10):
                                    pyautogui.moveTo(((w_screen/2)-250+xb), ((h_screen/2)-270+yb))
                                    
                        if mouse_mod():
                            if minx <= xi <=maxx and miny <= yi <= maxy:
                                pyautogui.moveTo((xi-minx)*(w_screen/(maxx-minx)),(yi-miny)*(h_screen/(maxy-miny)))

                        if maxset == False:
                            maxx = xt
                            maxy = (maxx-minx)*(h_screen/w_screen) 

                    if hand1_click and hand2_click:
                        minset ,maxset = True, True
                        set_openmenu_point = 1

                


            cv2.imshow("Hand Tracking", image)
            global thread1, thread
            if cv2.waitKey(1) & still_run():
                break


    cap.release()
    cv2.destroyAllWindows()
    exit()

thread = threading.Thread(target=track)
import time
thread1.start()
time.sleep(5)
thread.start()

thread1.join()
thread.join()
