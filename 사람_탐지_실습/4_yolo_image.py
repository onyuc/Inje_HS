from ultralytics import YOLO
import cv2
import os

# 모델 불러오기
model = YOLO("yolo11n.pt")  # 가장 작은 모델 (n: nano)

# 이미지 불러오기
current_file_path = os.path.abspath(__file__) # 현재 파일의 경로
current_dir_path = os.path.dirname(current_file_path)
image_path = r"test_images\bus.jpg" # 로컬 이미지 파일 경로
image_path = os.path.join(current_dir_path, image_path) # 경로 합치기

img = cv2.imread(image_path)

# 객체 탐지 실행
results = model(img, conf=0.25)

# 탐지 결과 그리기
annotated = results[0].plot()

# 결과 보여주기
cv2.imshow("이미지 탐지 결과", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
