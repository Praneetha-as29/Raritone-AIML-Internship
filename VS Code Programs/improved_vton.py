import cv2
import mediapipe as mp
import numpy as np

# Load images
person = cv2.imread("person.jpg")
cloth = cv2.imread(
    "garment4.png",
    cv2.IMREAD_UNCHANGED
)

if person is None:
    print("person.jpg not found")
    exit()

if cloth is None:
    print("garment4.png not found")
    exit()

# Resize person image
person = cv2.resize(
    person,
    (700, 1000)
)

# Better garment size
cloth = cv2.resize(
    cloth,
    (300, 340)
)

h, w = cloth.shape[:2]

# Improved TPS-style warp
src = np.float32([
    [0, 0],
    [w, 0],
    [0, h],
    [w, h]
])

dst = np.float32([
    [20, 15],
    [w - 20, 5],
    [10, h],
    [w - 10, h - 20]
])

matrix = cv2.getPerspectiveTransform(
    src,
    dst
)

warped = cv2.warpPerspective(
    cloth,
    matrix,
    (w, h)
)

# Placement
x_offset = 200
y_offset = 170

# Alpha channel
alpha = warped[:, :, 3] / 255.0

# Edge smoothing improvement
alpha = cv2.GaussianBlur(
    alpha,
    (9, 9),
    0
)

# Overlay garment
for c in range(3):

    person[
        y_offset:y_offset+h,
        x_offset:x_offset+w,
        c
    ] = (

        alpha * warped[:, :, c]

        +

        (1 - alpha)

        *

        person[
            y_offset:y_offset+h,
            x_offset:x_offset+w,
            c
        ]

    )

# Pose Detection
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
            color=(0, 255, 0),
            thickness=2,
            circle_radius=4
        ),
        mp_draw.DrawingSpec(
            color=(255, 255, 255),
            thickness=2
        )
    )

cv2.imwrite(
    "improved_vton_output.jpg",
    person
)

print("Improved VTON completed")

cv2.imshow(
    "Improved VTON",
    person
)

cv2.waitKey(0)
cv2.destroyAllWindows()