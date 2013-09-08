Emotime
=======

_Recognizing emotional states in faces_

----------------------------------------------
Copyleft [CC-BY-NC 2013](http://creativecommons.org/licenses/by-nc/3.0/)

## Goal
This project aim to recognize main facial expressions (neutral, anger, disgust, fear, joy, sadness, surprise) in image 
sequence using the approaches described in:

* [Dynamics of Facial Expression Extracted Automatically from Video](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1384873)
* [Fully Automatic Facial Action Recognition in Spontaneous Behavior](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1613024)

## References

Here is listed some interesting material about machine learning, opencv, gabor transforms and other 
stuff that could be usefull to get in this topic:

 * [AdaBoost and the Super Bowl of Classifiers](http://www.inf.fu-berlin.de/inst/ag-ki/rojas_home/documents/tutorials/adaboost4.pdf)
 * [Tutorial on Gabor Filters](http://mplab.ucsd.edu/tutorials/gabor.pdf)
 * [Gabor wavelet transform and its application](http://disp.ee.ntu.edu.tw/~pujols/Gabor%20wavelet%20transform%20and%20its%20application.pdf)
 * [Gabor Filter Visualization](http://www.cs.umd.edu/class/spring2005/cmsc838s/assignment-projects/gabor-filter-visualization/report.pdf)

## Project Structure

	src
		\-->dataset 		scripts for crating and using a dataset for classiefiers training
		\-->facecrop 		utility for crop and register faces from images
		\-->gaborbank		utility for applying a set of gabor filters to an image
		\-->adaboost 		utility for train and use adaboost classifiers
	doc
							folder containing documentation
	resources
							folder containing third party resources (eg. OpenCV classifiers)
	assets
							output folder, where binaries and script will be installed


## Build

Dependencies

	* cmake
	* Python 2.7 
	* OpenCV 2.4.5

Compiling on linux

* mkdir build; cd build
* cmake .. ; make ; make install

Cross-compiling for windows

* mkdir build; cd build
* TBD


## Usage

Initialize and fill a dataset

	./initdataset.py [-h] [-v] dsPath config
	./filldatasetCohnKanade.py [-h] [-v] datasetFolder cohnKanadeFolder cohnKanadeEmotionsFolder

Crop faces from dataset and calculation gabor filters features

	./cropFaces.py [-h] [-v] datasetFolder faceDetectorCfg
	./calcFeatures.py [-h] [-v] datasetFolder


Prepare training files and train classifiers

	./trainfiles.py [-h] [-v] datasetFolder
	TBD

Use trained classifier

	TBD

## Dataset

The [Cohn-Kanade database](http://www.consortium.ri.cmu.edu/ckagree/) is one of the most used face database. In it's extended version (CK+) it contains also [FACS](http://en.wikipedia.org/wiki/Facial_Action_Coding_System) 
code labels (aka Action Units) and emotion labels (neutral, anger, contempt, disgust, fear, happy, sadness, surprise).




