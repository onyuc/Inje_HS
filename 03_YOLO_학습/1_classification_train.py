import os
from ultralytics import YOLO

# 현재 파일 위치 기준으로 Classification_datasets 폴더 경로 생성
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "Classification_datasets")

# 모델 불러오기
model = YOLO("yolo11n-cls.pt")

# 모델 학습
results = model.train(data=data_dir, epochs=3, imgsz=100)
