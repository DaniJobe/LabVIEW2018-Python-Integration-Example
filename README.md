# LabVIEW2018 Python Integration Example

This project demonstrates how to use Python nodes to communicate between LabVIEW and Python and gives you sample VIs to fill in and try it yourself. 

It contains several examples:
* A simple hello world function
* Adding two numbers
* Calculating the number of days since a date (using clusters and enums as inputs)
* Finding the maximum and minimum in an array of numbers (a function that returns multiple outputs)
* Dictionary lookup with key-value pairs (arrays of clusters as inputs)
* Using OpenCV to do facial recognition on an image using [Haar Cascades](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)
* Using OpenCV to find the corners in an image using [Harris Corner Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners)

## Prerequisites
LabVIEW 2018 or newer  
Python 3.6 (3.6.8 is recommended)  
pip 19 or newer

## Installation 
Clone or download the repo  
  
Install the python packages using pip: 

    cd [repo clone location]/py_src
    pip install -r requirements.txt

**Note:**  
You will need to have [configured pip and python in your computer's system environmental variables](https://www.computerhope.com/issues/ch000549.htm)

## Author

**Danielle Jobe** - *Initial work* - [DanielleJobe](https://github.com/DanielleJobe)
