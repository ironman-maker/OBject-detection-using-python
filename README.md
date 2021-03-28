# OBject-detection-using-python

# Installing the Tensorflow OD-API and configuring the model

Lets start by installing tensorflow object detection api using Git. 
I'm Using linux for this project, but the process works same with windows and MacOS.

Firstly let's clone the master branch of the Tensorflow Models repository:

  git clone https://github.com/tensorflow/models.git

And here's how docker will help us :)

From the root of our git repository:
( Docker should be installed and configured before using the below commands )

  docker build -f research/object_detection/dockerfiles/tf1/Dockerfile -t od .
  docker run -it od

