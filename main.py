import cv2
import time

from camera_module import get_finger_states
from gesture_logic import classify_gesture
import media_control as media

last_gesture = None
last_time = 0
COOLDOWN = 1.5  # seconds

print("Gesture-Controlled Media System Started")
print("Press ESC to exit")

while True:
    fingers, frame = get_finger_states()

    if fingers is not None:
        gesture = classify_gesture(fingers)
        current_time = time.time()

        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 255, 0),
            3
        )

        if gesture != last_gesture and (current_time - last_time) > COOLDOWN:

            if gesture == "FIST":
                media.play_pause()

            elif gesture == "THUMB_UP":
                media.volume_up()

            elif gesture == "PINKY":
                media.volume_down()

            elif gesture == "TWO_FINGERS":
                media.next_track()

            elif gesture == "PALM":
                media.stop()

            last_gesture = gesture
            last_time = current_time

    if frame is not None:
        cv2.imshow("Touchless Media Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
