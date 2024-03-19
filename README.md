
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

  [Demo Video](https://github.com/Ahamedthaiyub/CareFall/raw/main/assets/98688617/b6d2a14f-ef18-452a-837c-6c03bbb32154)

## Conclusion
The Elder Patient Tracking System provides an innovative and reliable solution for monitoring and detecting falls among elderly individuals. By leveraging advanced technologies and comprehensive analysis, the system significantly enhances the safety and well-being of residents in retirement community settings.

## License
This project is licensed under the MIT License.

## Contributors
- Jeyasundar R (CSE)
- Ahamed Thaiyub A (CSE)
