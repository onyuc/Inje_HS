from ultralytics import YOLO
import cv2

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Define source as YouTube video URL
source = "https://youtu.be/LNwODJXcvt4"

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects

for result in results:
    output = result.plot()
    
    # 출력 이미지의 크기를 절반으로 줄이기
    resized_output = cv2.resize(output, (output.shape[1] // 2, output.shape[0] // 2))
    
    cv2.imshow("youtube", resized_output)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()