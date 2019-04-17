# LabVIEW2018 Python Integration Example

This project demonstrates and benchmarks two different ways to connect to python natively within LabVIEW (natively = without using third-party toolkits in LabVIEW):
* System executable vi  
* LabVIEW Python Nodes. 

Two different examples are demonstrated for each LV-Python integration method:
* A simple hello world function
* Using OpenCV to do facial recognition on an image file

The examples are looped and the execution time is calculated to demonstrate the difference in speed between the two methods of integration.  
**Spoiler!** LabVIEW Python nodes are way faster. 

## Prerequisites
LabVIEW 2018 or newer  
Python 3.6 (3.6.8 is recommended)  
OpenCV 3.4.2.17 or newer (can be installed via pip using requirements.txt)  
NumPY 1.15.1 or newer (can be installed via pip using requirements.txt)  

## Installation 
Clone or download the repo:  

    git clone https://github.com/DanielleJobe/LabVIEW2018_Python_Integration.git

Install the python packages using PIP: 

    cd [repo clone location]/py_src
    pip install -r requirements.txt

**Note:**  
You will need to have [configured pip and python in your computer's system environmental variables](https://www.computerhope.com/issues/ch000549.htm)

## Author

**Danielle Jobe** - *Initial work* - [DanielleJobe](https://github.com/DanielleJobe)

## License

This project uses code from the [OpenCV repository](https://github.com/opencv/opencv) so its license applies
