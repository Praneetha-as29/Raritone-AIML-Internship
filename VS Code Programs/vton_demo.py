import cv2
import mediapipe as mp

person = cv2.imread("person.jpg")
cloth = cv2.imread("garment.png")

if person is None:
    print("person.jpg not found")
    exit()

if cloth is None:
    print("garment.png not found")
    exit()

# Bigger full body view
person = cv2.resize(person, (700, 1000))

# Fixed shirt size
cloth = cv2.resize(cloth, (260, 320))

# Fixed placement
x_offset = 220
y_offset = 180

# Overlay shirt
person[
    y_offset:y_offset + 320,
    x_offset:x_offset + 260
] = cloth

# Pose detection
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=True,
    min_detection_confidence=0.7
)

rgb = cv2.cvtColor(
    person,
    cv2.COLOR_BGR2RGB
)

results = pose.process(rgb)

if results.pose_landmarks:

    mp_draw.draw_landmarks(
        person,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        mp_draw.DrawingSpec(
            color=(0,255,0),
            thickness=2,
            circle_radius=4
        ),
        mp_draw.DrawingSpec(
            color=(255,255,255),
            thickness=2
        )
    )

cv2.imwrite(
    "vton_output.jpg",
    person
)

cv2.imshow(
    "2D Virtual Try-On",
    person
)

cv2.waitKey(0)
cv2.destroyAllWindows()