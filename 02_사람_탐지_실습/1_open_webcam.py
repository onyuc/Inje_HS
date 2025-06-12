# OpenCV 라이브러리를 불러옵니다. (영상 처리에 사용하는 도구)
import cv2

# 노트북의 카메라를 켭니다. 숫자 0은 기본 카메라를 의미합니다.
cap = cv2.VideoCapture(0)

# 카메라에서 한 장의 사진(프레임)을 읽어옵니다.
# ret: 성공했는지(True/False)
# frame: 실제 영상 이미지 데이터
ret, frame = cap.read()

# 불러온 영상을 화면에 보여줍니다.
# "frame_inje"는 창의 제목입니다.
cv2.imshow("frame_inje", frame)
# 숫자가 없거나 0이면, 아무 키가 눌릴 때까지 무한히 기다립니다.
# 창을 닫지 않으면 프로그램이 바로 종료되기 때문에 꼭 필요합니다.
cv2.waitKey()

# 더 이상 카메라를 사용하지 않으니 종료합니다.
cap.release()

# 열려 있는 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()