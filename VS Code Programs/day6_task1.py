import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    model_complexity=2,
    smooth_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.resize(frame, (900, 700))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark

        left_shoulder = lm[11]
        right_shoulder = lm[12]

        shoulder_width = calculate_distance(left_shoulder, right_shoulder)

        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        cv2.putText(frame,
                    "Shoulder Width: " + str(round(shoulder_width, 3)),
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2)

    cv2.imshow("Body Measurement", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()