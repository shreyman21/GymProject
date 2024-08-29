# GymProject

## Overview

GymProject is a machine learning-based exercise classification system. This project allows users to upload workout videos, and the model will predict the exercise performed in each frame. The project utilizes TensorFlow for the model, Flask for the web interface, and OpenCV for video processing.

## Features

- **Exercise Classification**: Detects and classifies different exercises such as push-ups, sit-ups, lunges, and more from videos.
- **Data Augmentation**: Uses advanced data augmentation techniques to improve model accuracy.
- **Model Training**: Includes scripts to train a custom TensorFlow model using your own dataset.
- **Web Interface**: Provides a simple web interface using Flask to upload videos and receive predictions.

## Project Structure

```plaintext
GymProject/
├── app.py                 # Flask application for handling video uploads and predictions
├── create_model.py        # Script for training the TensorFlow model
├── extraction.py          # Script for extracting frames from videos and labeling them
├── test_set.py            # Script to test the model with a test dataset
├── data/                  # Directory containing training data (organized by class)
├── temp_frames/           # Temporary directory for storing video frames
├── .gitignore             # Git ignore file
├── venv/                  # Python virtual environment
└── exercise_model.h5      # Trained TensorFlow model (excluded from version control)

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed on your system.
- **Virtualenv**: For creating isolated Python environments.
- **Git LFS**: Git Large File Storage (LFS) is needed to handle large files like `.mp4` and `.h5`.
- **TensorFlow**: The machine learning library required for the model.
- **OpenCV**: For video processing and frame extraction.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd GymProject


