import cv2

# Open the device at the ID 0
import self as self

cap = cv2.VideoCapture(0)

# Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print('Could not open video device')

# To set the resolution

self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)

self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 160)

while (True):
    ret, frame = cap.read()

    # Display the resulting frame

    cv2.imshow('preview', 'frame')

    # Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()
