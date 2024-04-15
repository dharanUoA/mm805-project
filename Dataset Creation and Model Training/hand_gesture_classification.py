import csv
import copy

import cv2 as cv
import mediapipe as mp

import utils.constants as CONSTANTS
from utils.cvfpscalc import CvFpsCalc
from model.classifier import Classifier


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

    classifier = Classifier()

    with open(CONSTANTS.LABELS_FILE_PATH, encoding='utf-8-sig') as f:
        classifier_labels = csv.reader(f)
        classifier_labels = [
            row[0] for row in classifier_labels
        ]

    cvFpsCalc = CvFpsCalc(buffer_len=10)

    while True:
        fps = cvFpsCalc.get()

        key = cv.waitKey(10)
        if key == 27:  # ESC
            break

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
                
                hand_sign_id = classifier(pre_processed_landmark_list)

                debug_image = CONSTANTS.draw_bounding_rect(debug_image, brect)
                debug_image = CONSTANTS.draw_landmarks(debug_image, landmark_list)
                debug_image = draw_info_text(
                    debug_image,
                    brect,
                    handedness,
                    classifier_labels[hand_sign_id]
                )

        debug_image = CONSTANTS.draw_info(debug_image, fps, -1)

        cv.imshow('Hand Gesture Recognition', debug_image)

    cap.release()
    cv.destroyAllWindows()

def draw_info_text(image, brect, handedness, hand_sign_text):
    cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[1] - 22),
                 (0, 0, 0), -1)

    info_text = handedness.classification[0].label[0:]
    if hand_sign_text != "":
        info_text = info_text + ':' + hand_sign_text
    cv.putText(image, info_text, (brect[0] + 5, brect[1] - 4),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)

    return image


if __name__ == '__main__':
    main()
