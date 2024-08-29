GymProject
Overview
GymProject is a machine learning-based exercise classification system. This project allows users to upload workout videos, and the model will predict the exercise performed in each frame. The project utilizes TensorFlow for the model, Flask for the web interface, and OpenCV for video processing.

Features
Exercise Classification: Detects and classifies different exercises such as push-ups, sit-ups, lunges, and more from videos.
Data Augmentation: Uses advanced data augmentation techniques to improve model accuracy.
Model Training: Includes scripts to train a custom TensorFlow model using your own dataset.
Web Interface: Provides a simple web interface using Flask to upload videos and receive predictions.
Project Structure
bash
Copy code
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
Prerequisites
Python 3.8+
Virtualenv
Git LFS (for handling large files)
TensorFlow
OpenCV
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd GymProject
2. Set Up a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Download or Prepare Your Dataset
Organize your training data into subdirectories under the data/ folder, where each subdirectory represents a class (e.g., push-ups, sit-ups).
If you have test data, place it in a similar structure under test_data/.
5. Train the Model
To train the model on your dataset, run:

bash
Copy code
python create_model.py
6. Run the Application
Start the Flask application:

bash
Copy code
python app.py
You can now upload workout videos through the Flask interface and receive exercise predictions.

7. Test the Model
Use the test_set.py script to evaluate the model's accuracy on a separate test dataset:

bash
Copy code
python test_set.py
Known Issues
Large File Handling: Ensure Git LFS is correctly configured to manage large files, such as .mp4 and .h5 files.
Model Overfitting: If the model is overfitting, consider enhancing data augmentation or adjusting the model architecture.
Troubleshooting
RPC Failed; HTTP 400 Error: This error may occur if the repository is too large. Consider splitting the repository, reducing file sizes, or hosting large files separately.
Future Improvements
Implement more exercise categories.
Enhance the model's accuracy by using transfer learning.
Develop a more robust web interface with real-time video processing.
