import os
from ultralytics import YOLO

# 현재 파일 위치 기준으로 Classification_datasets 폴더 경로 생성
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "datasets/data.yaml") # 여기서 yaml 파일 위치를 수정해주세요!!

# 모델 불러오기
model = YOLO("yolo11n.pt")

# 마지막 2개 레이어 제외하고 모두 얼리기
# model.model.parameters()는 모든 파라미터를 순서대로 반환함
# 이를 리스트로 바꿔서 마지막 2개만 학습 가능하게 설정
params = list(model.model.parameters())
for p in params[:-2]:
    p.requires_grad = False  # 학습 안 됨
for p in params[-2:]:
    p.requires_grad = True   # 학습 됨

# 모델 학습
if __name__ == '__main__':
    results = model.train(data=data_dir, epochs=100, imgsz=320, device='cpu')

    # GPU 사용 가능하게 세팅해두 면 아래 설정 사용가능, 하지만 굉장히 세팅하기가 귀찮음
    # results = model.train(data=data_dir, epochs=100, imgsz=320, device=0)

