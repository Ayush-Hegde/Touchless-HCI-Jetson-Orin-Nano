import cv2
import mediapipe as mp
from gesture_logic import classify_gesture

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = "NO HAND"

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        fingers = [0, 0, 0, 0, 0]

        fingers[0] = 1 if lm[4].x < lm[3].x else 0
        fingers[1] = 1 if lm[8].y < lm[6].y else 0
        fingers[2] = 1 if lm[12].y < lm[10].y else 0
        fingers[3] = 1 if lm[16].y < lm[14].y else 0
        fingers[4] = 1 if lm[20].y < lm[18].y else 0

        gesture = classify_gesture(fingers)

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Gesture Debug Mode", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
