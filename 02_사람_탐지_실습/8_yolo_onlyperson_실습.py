from ultralytics import YOLO
import cv2

# 모델 불러오기
model = YOLO("yolo11n.pt")

# 웹캠 연결
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 객체 탐지
    results = model(frame)
    annotated = results[0].plot()

    # 출력 이미지의 크기를 절반으로 줄이기
    resized_annotated = cv2.resize(annotated, (annotated.shape[1] // 2, annotated.shape[0] // 2))
    
    cv2.imshow("웹캠 실시간 탐지", resized_annotated)
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
