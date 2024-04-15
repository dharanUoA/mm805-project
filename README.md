<a name="readme-top"></a>

# MM805 Project - DynamicVision: Real-Time Gesture & Background Evolution

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
            <li><a href="#run">Run the application</a></li>
        </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE Assignment -->

## About The Project

DynamicVision is a computer vision project that focuses on real-time gesture recognition and dynamic background evolution. It aims to capture, analyze, and respond to dynamic hand gestures while adapting to changes in the background environment. The project leverages modern machine learning techniques, such as convolutional neural networks and point cloud processing, to achieve accurate gesture detection and classification. The literature review highlights state-of-the-art approaches like Hand PointNet for 3D hand pose estimation, real-time gesture detection using CNNs, and continuous gesture recognition based on skeleton data. The project's objectives include creating a dataset, training a neural network model, converting it for web deployment, and integrating it into a web application. DynamicVision has the potential to revolutionize user interactions with digital systems, providing more intuitive and immersive experiences.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

#### Dataset creating and model training

- python 3.8
- mediapipe
- open-cv
- tensorflow
- scikit-learn

#### Web application

- tensorflowjs
- react

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Download and install python 3.8 from [https://www.python.org/downloads/](https://www.python.org/downloads/).
<br />
Download and install node js from [https://nodejs.org/en](https://nodejs.org/en).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

### Dataset Creation

Use file [dataset_creation.py](./Dataset%20Creation%20and%20Model%20Training/dataset_creation.py) for dataset creation.

- Current dataset labels: [labels.csv](./Dataset%20Creation%20and%20Model%20Training/model/labels.csv)
- Current keypoints dataset: [keypoints.csv](./Dataset%20Creation%20and%20Model%20Training/model/keypoints.csv)

Steps for new dataset creation:
1. Create 2 new csv files, one for labels and second for keypoints file in [model](./Dataset%20Creation%20and%20Model%20Training//model/) directory.
2. Add gesture names separated by new line in newly created labels file.
3. Update the `LABELS_FILE_PATH` and `KEYPOINTS_FILE_PATH` file path in [constants.py](./Dataset%20Creation%20and%20Model%20Training//utils//constants.py).
4. pip install required python dependicies.
5. Execute below in cmmand prompt or terminal 
```sh
cd "Dataset Creation and Model Training"
py dataset_creation.py
```
5. A new python window will open, which will capture access the webcam and show the captured results. By raising your hands, you can check that the application will local the hand and finds 21 hand points and draws the results in the output as well.
6. A new data row can be added by pressing the number keys.