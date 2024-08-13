# AlertMinds

**AlertMinds** is an innovative project that leverages live camera feeds to monitor and analyze your focus during working or studying using YOLOv5 model. Based on the data collected, the project creates a personalized timetable and provides valuable insights through an attractive and user-friendly dashboard. Additionally, it features a chatbot built using a Feedforward Neural Network (FNN) that responds to simple questions.

## Features

- **Live Camera Feed Analysis:** Utilizes YOLO for real-time analysis of alertness levels.
- **Personalized Timetable Creation:** Generates a custom timetable based on your most alert periods.
- **Insightful Dashboard:** Provides visual insights and analytics on your focus and alertness patterns.
- **Chatbot Integration:** Includes an FNN-based chatbot that answers simple questions.

## Project Structure

- **Chatbot**
  - Contains the code and scripts for the FNN-based chatbot functionality.
- **Tkinter**
  - Files and scripts for the Tkinter-based frontend interface, including the dashboard.
- **label**
  - Contains code necessary for the execution of the YOLO model.
- **labelimg**
  - Contains code that launches a UI interface for labelling training images.
- **train**
  - Contains the custom weights of the YOLO model after training.
- **yolo5**
  - Contains the code for YOLOv5 model.
- **SleepDetection.ipynb**
  - Jupyter Notebook code that puts all the separate components together. Integrates the YOLO model with the live video capture done using OpenCV.

