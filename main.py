from deepface import DeepFace
import cv2
import time

cap = cv2.VideoCapture(0)  # Webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Vaqtincha saqlash uchun fayl
    temp_img = "temp_frame.jpg"
    cv2.imwrite(temp_img, frame)
    
    try:
        # Tezkor tahlil
        analysis = DeepFace.analyze(temp_img, actions=['emotion'], enforce_detection=True)
        
        # Anti-spoofing qoidasi
        if analysis[0]['emotion']['neutral'] > 80:
            text = "EHTIYOT: Fake yuz (foto/video)"
            color = (0, 0, 255)  # Qizil
        else:
            text = "Haqiqiy yuz"
            color = (0, 255, 0)  # Yashil
            
        # Natijani ekranga chiqarish
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
    except:
        cv2.putText(frame, "Yuz topilmadi", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Anti-Spoofing System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()