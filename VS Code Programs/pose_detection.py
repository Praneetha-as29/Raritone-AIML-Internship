import cv2
import mediapipe as mp

image = cv2.imread("person.jpg")

image = cv2.resize(
    image,
    (600, 600)
)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = pose.process(rgb)

if results.pose_landmarks:

    mp.solutions.drawing_utils.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS
    )

cv2.imwrite("pose_output.jpg", image)

cv2.imshow("Pose Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()