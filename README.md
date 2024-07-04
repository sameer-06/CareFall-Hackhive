# CareFall - Enhancing Elderly Care with the Power of Intel oneAPI

![Screenshot](img/Screenshot%202024-03-20%20010923.png)

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
   - **Additional Functionality**: The system sends SMS alerts using a GSM module connected to the device, ensuring timely notifications to caregivers. Make sure the GSM module is properly connected and configured for sending messages.

3. **Camera Interface Module (`camra.py`)**:
   - **Purpose**: Handles the interaction with the camera device for capturing video frames.
   - **Dependencies**: OpenCV
   - **Usage**: The `camra.py` module provides functions to initialize the camera and capture frames for fall detection.

4. **Model Evaluation Module (`evaluate.py`)**:
   - **Purpose**: Evaluates the performance of the trained fall detection model using a test dataset.
   - **Dependencies**: TensorFlow, OpenCV, ImageDataGenerator
   - **Usage**: Execute the `evaluate.py` script to assess the accuracy and other performance metrics of the trained model.

## System Setup
.
1. **Dependencies Installation**:
   - Ensure all required dependencies are installed in your environment. Refer to the Dependencies section for details.

2. **Dataset Preparation**: 
   - Prepare a dataset containing images of elderly individuals in various poses, including falls and non-falls, for training the model.

3. **Model Training**: 
   - Run the `train.py` script to train the fall detection model using the prepared dataset.

4. **Model Evaluation**:
   - Optionally, use the `evaluate.py` script to evaluate the performance of the trained model on a test dataset.

5. **System Deployment**: 
   - Deploy the trained model and related modules (`simck.py`, `camra.py`) in the target environment, such as a retirement community facility.

## Running the System

1. **Fall Detection Module**:
   - Execute the `simck.py` script to initialize the fall detection system.
   - Ensure that the camera device is connected and accessible.
   - The system will capture video frames from the camera feed, analyze them using the trained model, and provide real-time fall detection alerts.
   - Additionally, the system sends SMS alerts using a GSM module connected to the device, ensuring timely notifications to caregivers. Make sure the GSM module is properly connected and configured for sending messages.

## Demo Video and Test Images

[![Demo Video](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/372626a3-703d-4bc8-92a0-02fd83b3771a.png)](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/372626a3-703d-4bc8-92a0-02fd83b3771a)

## Section Files 

### Section 1: Fall Detection and SMS Notification
- **File(s):** `sec1.txt`
- **Description:** This section focuses on implementing normal fall detection prediction and sending SMS notifications to a designated module.

### Section 2: Custom Image Processing
- **File(s):** *Additional files uploaded*
- **Description:** This section addresses various issues encountered and their resolutions. It involves utilizing custom images for certain aspects of the project.

### Section 3: OpenPose Integration and Lie Detection
- **File(s):** *Additional files uploaded*
- **Description:** Discusses the integration of OpenPose for pose detection and lie detection in video streams. It covers challenges faced and the solutions implemented.

## Output:
<img src="WhatsApp Image 2024-03-22 at 12.54.34 AM.jpeg" alt="WhatsApp Image 2024-03-20 at 12.52.07 AM" style="width: 400px; margin-right: 10px;">

### Section 4: Full Model Deployment
- **File(s):** *Additional files uploaded*
- **Description:** This section marks the deployment of the full model. It likely incorporates all the functionalities developed in previous sections and may include optimizations or additional features.

## Test Image and How it Works 

![00091_00016](00091_00016.gif)
![00091_00016](00091_00031.gif)

## Web Pages :

<div style="display: flex; justify-content: center;">
  <img src="WhatsApp%20Image%202024-03-20%20at%2012.52.07%20AM.jpeg" alt="WhatsApp Image 2024-03-20 at 12.52.07 AM" style="width: 400px; margin-right: 10px;">
  <img src="WhatsApp%20Image%202024-03-20%20at%2012.52.08%20AM%20(1).jpeg" alt="WhatsApp Image 2024-03-20 at 12.52.08 AM (1)" style="width: 400px; margin: 0 10px;">
  <img src="WhatsApp%20Image%202024-03-20%20at%2012.52.08%20AM.jpeg" alt="WhatsApp Image 2024-03-20 at 12.52.08 AM" style="width: 400px; margin-left: 10px;">
</div>

## Local Development

To run the Elder Patient Tracking System locally for development or testing purposes, follow these steps:

1. Clone this repository to your local machine.
2. Ensure all required dependencies mentioned in the "Dependencies Installation" section are installed in your environment.
3. Prepare a small dataset containing sample images or videos for testing the fall detection system.
4. Run the `simck.py` script to initialize the fall detection system locally. Make sure you have a camera connected and accessible.
5. Monitor the output to observe real-time fall detection alerts on your local machine.
6. Optionally, you can simulate SMS alerts by configuring a virtual GSM module or by modifying the code to print messages instead.

## Conclusion

The Elder Patient Tracking System provides an innovative and reliable solution for monitoring and detecting falls among elderly individuals. By leveraging advanced technologies and comprehensive analysis, the system significantly enhances the safety and well-being of residents in retirement community settings.

## License

This project is licensed under the MIT License.



