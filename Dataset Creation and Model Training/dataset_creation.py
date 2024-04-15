import csv
import cv2 as cv
import copy
import mediapipe as mp
import utils.constants as CONSTANTS 
from utils.cvfpscalc import CvFpsCalc


def main():
    cap_device = CONSTANTS.CAP_DEVICE
    cap_width = CONSTANTS.CAP_WIDTH
    cap_height = CONSTANTS.CAP_HEIGHT

    min_detection_confidence = CONSTANTS.MIN_DETECTION_CONFIDENCE

    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=CONSTANTS.MAX_NUM_HANDS,
        min_detection_confidence=min_detection_confidence,
    )

    cvFpsCalc = CvFpsCalc(buffer_len=10)

    while True:
        fps = cvFpsCalc.get()

        key = cv.waitKey(10)
        if key == 27:  # ESC
            break
        number = select_key(key)

        ret, image = cap.read()
        if not ret:
            break
        image = cv.flip(image, 1)
        debug_image = copy.deepcopy(image)

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        if results.multi_hand_landmarks is not None:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks,
                                                  results.multi_handedness):
                brect = CONSTANTS.calc_bounding_rect(debug_image, hand_landmarks)
                landmark_list = CONSTANTS.calc_landmark_list(debug_image, hand_landmarks)

                pre_processed_landmark_list = CONSTANTS.pre_process_landmark(
                    landmark_list)

                logging_csv(number, pre_processed_landmark_list)

                debug_image = CONSTANTS.draw_bounding_rect(debug_image, brect)
                debug_image = CONSTANTS.draw_landmarks(debug_image, landmark_list)

        debug_image = CONSTANTS.draw_info(debug_image, fps, number)

        cv.imshow('Hand Gesture Recognition', debug_image)

    cap.release()
    cv.destroyAllWindows()


def select_key(key):
    number = -1
    if 48 <= key <= 57:  # 0 ~ 9
        number = key - 48
    return number


def logging_csv(number, landmark_list):
    if (0 <= number <= 9):
        csv_path = 'model/keypoints.csv'
        with open(csv_path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([number, *landmark_list])
    return


if __name__ == '__main__':
    main()
