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

## To run the demo on web app

1. Execute below in command prompt or terminal

```sh
cd "Web-App-React"
npm i
npm start
```

2. Or use the link: [https://mm805-project.vercel.app/](https://mm805-project.vercel.app/)

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

Use file [dataset_creation.py](./Dataset-Creation-and-Model-Training/dataset_creation.py) for dataset creation.

- Current dataset labels: [labels.csv](./Dataset-Creation-and-Model-Training/model/labels.csv)
- Current keypoints dataset: [keypoints.csv](./Dataset-Creation-and-Model-Training/model/keypoints.csv)

Steps for new dataset creation:

1. Create 2 new csv files, one for labels and second for keypoints file in [model](./Dataset-Creation-and-Model-Training/model/) directory.
2. Add gesture names separated by new line in newly created labels file.
3. Update the `LABELS_FILE_PATH` and `KEYPOINTS_FILE_PATH` file path in [constants.py](./Dataset-Creation-and-Model-Training/utils/constants.py).
4. pip install required python dependicies.
5. Execute below in command prompt or terminal

```sh
cd "Dataset-Creation-and-Model-Training"
py dataset_creation.py
```

5. A new python window will open, which will capture access the webcam and show the captured results. By raising your hands, you can check that the application will local the hand and finds 21 hand points and draws the results in the output as well.
6. A new data row can be added by pressing the number keys.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Model Training

Use file [model_training.ipynb](./Dataset-Creation-and-Model-Training/model_training.ipynb) for model training.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Convert the Model to tensorflow js

1. Use the below colab link for conversion.
   <br />
   [colab.research.google.com](https://colab.research.google.com/drive/1zR1DRhOpe4no_TyRHoKwprGUTtEre7j5?usp=sharing)

2. The above notebook will generate 2 new two files bin and json in hand-gesture-classifier of colab. Download those files.

3. Place the above two files in one folder and place the folder in the below path of the web app project.
   <br />
   [models](./Web-App-React/public/models/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Run the Web App

1. Update the labels in `labels` and `labelsToDraw` variable of [App.js](./Web-App-React/src/App.js) at line no: `10`. Add all your labels in `labels` variable and add the labels for which you want to make changes in the view in `labelsToDraw` variable.
2. Update the view update logic in `draw()` function of [App.js](./Web-App-React/src/App.js)
3. Execute below in command prompt or terminal

```sh
cd "Web-App-React"
npm i
npm start
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
