# CareFall - Enhancing Elderly Care with the Power of Intel oneAPI

## Introduction
The Elder Patient Tracking System (EPTS) is a sophisticated solution designed to monitor and detect instances of falls among elderly residents in retirement communities. Leveraging deep learning techniques and real-time video analysis, the system offers timely alerts to caregivers, ensuring swift intervention and assistance in case of fall events.

## System Components
The Elder Patient Tracking System comprises the following components:

1. **Training Module (`train.py`)**:
   - **Purpose**: Trains a deep learning model to detect falls using monocular camera images.
   - **Dependencies**: TensorFlow, OpenCV, ImageDataGenerator
   - **Usage**: Execute the `train.py` script to train the model using the provided training dataset.

2. **Fall Detection Module (`simck.py`)**:
   - **Purpose**: Implements real-time fall detection using a trained deep learning model.
   - **Dependencies**: TensorFlow, OpenCV
   - **Usage**: Run the `simck.py` script to initialize the fall detection system, which captures video frames from a camera feed and makes predictions using the trained model.

3. **Camera Interface Module (`camra.py`)**:
   - **Purpose**: Handles the interaction with the camera device for capturing video frames.
   - **Dependencies**: OpenCV
   - **Usage**: The `camra.py` module provides functions to initialize the camera and capture frames for fall detection.

4. **Model Evaluation Module (`evaluate.py`)**:
   - **Purpose**: Evaluates the performance of the trained fall detection model using a test dataset.
   - **Dependencies**: TensorFlow, OpenCV, ImageDataGenerator
   - **Usage**: Execute the `evaluate.py` script to assess the accuracy and other performance metrics of the trained model.

## System Setup
1. ## Dependencies

The following dependencies are required to run the CareFall project:

- [scipy](https://pypi.org/project/scipy/): Scientific computing library for mathematical functions and algorithms.
- [matplotlib](https://matplotlib.org/): Visualization library for creating static, animated, and interactive visualizations in Python.
- [opencv](https://opencv.org/): Open-source computer vision and machine learning software library.
- [torch](https://pytorch.org/): Open-source machine learning framework that accelerates the path from research prototyping to production deployment.
- [torchvision](https://pytorch.org/vision/stable/index.html): Official PyTorch library for computer vision tasks.
- [scikit-image](https://scikit-image.org/): Collection of algorithms for image processing.
- [visdom](https://github.com/facebookresearch/visdom): Visualization tool for interactive data visualization.
- [json](https://docs.python.org/3/library/json.html): Library for parsing and serializing JSON data.
- [plotly](https://plotly.com/python/): Interactive graphing library for Python.
- [jsonpatch](https://pypi.org/project/jsonpatch/): Library for applying JSON patches.
- [dominate](https://github.com/Knio/dominate): Library for creating and manipulating HTML documents using Python code.
- [tqdm](https://github.com/tqdm/tqdm): Library for adding progress bars to Python code.
- [configargparse](https://github.com/bw2/ConfigArgParse): Library for parsing command-line arguments and configuration files.
- [yacs](https://github.com/rbgirshick/yacs): Yet Another Configuration System, a lightweight configuration system used in many open-source projects.
- [jupyter](https://jupyter.org/): Interactive computing platform for creating and sharing documents containing live code, equations, visualizations, and narrative text.

2. **Dataset Preparation**: Prepare a dataset containing images of elderly individuals in various poses, including falls and non-falls, for training the model.
3. **Model Training**: Run the `train.py` script to train the fall detection model using the prepared dataset.
4. **Model Evaluation**: Optionally, use the `evaluate.py` script to evaluate the performance of the trained model on a test dataset.
5. **System Deployment**: Deploy the trained model and related modules (`simck.py`, `camra.py`) in the target environment, such as a retirement community facility.

## Running the System
1. **Fall Detection Module**:
   - Execute the `simck.py` script to initialize the fall detection system.
   - Ensure that the camera device is connected and accessible.
   - The system will capture video frames from the camera feed, analyze them using the trained model, and provide real-time fall detection alerts.

## Demo Video and Test Images


[![Demo Video](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/372626a3-703d-4bc8-92a0-02fd83b3771a.png)](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/372626a3-703d-4bc8-92a0-02fd83b3771a)

[Demo Video](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/b6d2a14f-ef18-452a-837c-6c03bbb32154)


## Conclusion
Conclusion
The Elder Patient Tracking System provides an innovative and reliable solution for monitoring and detecting falls among elderly individuals. By leveraging advanced technologies and comprehensive analysis, the system significantly enhances the safety and well-being of residents in retirement community settings.
## This project is licensed under the MIT License and was developed by Jeyasundar R (CSE) and Ahamed Thaiyub A (CSE).
