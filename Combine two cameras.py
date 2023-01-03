import cv2

# Create a VideoCapture object for each webcam
webcam1 = cv2.VideoCapture(0)
webcam2 = cv2.VideoCapture(1)

# Set the dimensions of the output frame
width = 1280
height = 720

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
