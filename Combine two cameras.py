import cv2
import torch

font = cv2.FONT_HERSHEY_SIMPLEX

# Create a VideoCapture object for each webcam
webcam1 = cv2.VideoCapture(0)
webcam2 = cv2.VideoCapture(1)

# add auto exposure
webcam1.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
webcam2.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
webcam1.set(cv2.CAP_PROP_FPS, 60)
webcam2.set(cv2.CAP_PROP_FPS, 60)
# Set the dimensions of the output frame
width = 1280
height = 720

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
labels = model.names

# Create a window to display the video
# cv2.namedWindow("Webcam1", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Webcam1", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Start an infinite loop to display the video from the webcams
while True:
    # Read frames from the webcams
    _, frame1 = webcam1.read()
    _, frame2 = webcam2.read()

    # Resize frame2 to a smaller size
    frame2 = cv2.resize(frame2, (320, 180))

    frame1 = cv2.flip(frame1, 0)

    # Gives results as a tensor
    results = model(frame1).xyxy[0]

    for i in range(results.size(dim=0)):
        row = results[i, :].numpy()
        tl = (int(row[0]), int(row[3]))
        br = (int(row[2]), int(row[1]))
        cv2.rectangle(frame1, tl, br, (0, 255, 0), 3)
        text = labels[row[5]]
        cv2.putText(frame1, text, tl, font, 2, (255,255,255), 2, cv2.LINE_AA)

    results = model(frame2).xyxy[0]

    for i in range(results.size(dim=0)):
        row = results[i, :].numpy()
        tl = (int(row[0]), int(row[3]))
        br = (int(row[2]), int(row[1]))
        cv2.rectangle(frame2, tl, br, (0, 255, 0), 3)
        text = labels[row[5]]
        cv2.putText(frame2, text, tl, font, 1, (255,255,255), 2, cv2.LINE_AA)

    # Add frame2 to the top-right corner of frame1
    x_offset = frame1.shape[1] - frame2.shape[1]
    y_offset = 0
    frame1[y_offset:y_offset+frame2.shape[0], x_offset:x_offset+frame2.shape[1]] = frame2

    # Display the resulting frame
    cv2.imshow("Webcam1", frame1)

    # Check if the user pressed "q" to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture objects
webcam1.release()
webcam2.release()

# Destroy the window
cv2.destroyAllWindows()
