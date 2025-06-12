
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened:
    exit() # 프로그램 종료

while True:
    ret, frame = cap.read()

    if not ret: #못 불러올 시 프로그램 종료료
        break

    # 보여주기용
    cv2.imshow("frame_inje", frame)

    key = cv2.waitKey(1)
    if key == ord('q'): # 창에 입력 가능!
        break

# 마무리용
cap.release()
cv2.destroyAllWindows()