/**
*
*/

#include "adapredict.h"

using namespace std;
using namespace cv;
using namespace facecrop;

float adapredict_predictNoPreprocess( CvBoost & boost, cv::Mat & img ){
	vector<Mat> bank;
	gaborbank_getGaborBank(bank);
	return adapredict_predict( boost, bank, img, cv::Size(0,0), NULL );
}


float adapredict_predict( CvBoost & boost, std::vector<cv::Mat> & bank, cv::Mat & img, cv::Size scaleSize, const char * faceDetectConf ){
	Size suggSize;
	Mat * dest;
	Mat image;
	Mat scaled;

	if ( faceDetectConf != NULL ) {
		// Face cropping
		FaceDetector detector(faceDetectConf);
		facecrop_cropFace( detector, img, image, true );
		//delete &detector;
	} else {
		image=img;
	}

	if ( scaleSize.height!=0 && scaleSize.width!=0 ) {
		// Resizing
		resize( image, scaled, scaleSize, 0, 0, CV_INTER_AREA );
	} else {
		scaled=image;
	}

	gaborbank_getFilteredImgSize(scaled, bank, suggSize);
	cout << "DEBUG: Creating out matrix"<< endl;
	dest = new Mat( suggSize.width, suggSize.height, CV_8UC1 );
	cout << "DEBUG: Filtering "<< endl;
	gaborbank_filterImage(scaled, bank, *dest);
	cout << "DEBUG: Predicting"<< endl;
	float prediction = boost.predict( *dest, Mat(), Range::all(), false, false);
	delete dest;

	return prediction;
}