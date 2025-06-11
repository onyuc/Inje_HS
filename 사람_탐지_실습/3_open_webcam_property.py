import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

# 초기 밝기 값 읽기
brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
print("초기 밝기 값:", brightness)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("frame_inje", frame)

    key = cv2.waitKey(1)

    # 'q' 키로 종료
    if key == ord('q'):
        break

    #  키: 밝기 증가
    elif key == ord('w'):  # w
        brightness += 0.05
        cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
        print("밝기 증가:", brightness)

    # s 키: 밝기 감소
    elif key == ord('s'): # s
        brightness -= 0.05
        cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
        print("밝기 감소:", brightness)

cap.release()
cv2.destroyAllWindows()
