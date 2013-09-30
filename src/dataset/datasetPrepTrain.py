#!/usr/bin/env python2
"""
   
"""

import cv2 as cv
import os
import itertools
import argparse

from os.path import join
from os.path import isfile
from os.path import isdir

_DATASET_CONFIG_FILE="dataset.conf"

def _dataset_multiclass1to1( config ):
  """ 
      
  """
  return [x for x in itertools.combinations( config['CLASSES'] , 2 )]

def dataset_prepTrain1to1Gabor( (goodClass,badClass),  dsFolder, config ):
  """ 
     Prepare train file with positive and negative samples generated by Gabor banks
  """
  print "INFO: Preparing training file for '%s' vs. '%s' " %(goodClass,badClass)

  goodPath=join(dsFolder,join(config['FEATURESFOLDER'],goodClass))
  badPath=join(dsFolder,join(config['FEATURESFOLDER'],badClass))
  #
  # Note: a goodFolder should contain the filtered images (various orientation and frequency ) 
  #       of a single sample image. So each line of the training file will be composed by its
  #    MARKER ( Good or Bad ) plus all the pixel values of the filtered images 
  #
  goodFolders=[ join(goodPath,f) for f in os.listdir(goodPath) if isdir(join(goodPath,f)) and f.endswith(config['FILTERED_FOLDER_SUFFIX']) ]
  badFolders= [ join(badPath,f)  for f in os.listdir(badPath)  if isdir(join(badPath,f))  and f.endswith(config['FILTERED_FOLDER_SUFFIX']) ]
  outfpath=join(join(dsFolder,config['TRAINFOLDER']),"%s_%s%s"%(goodClass,badClass,config['FEATURE_FILE_SUFFIX']))
  with open( outfpath , "w") as tf:
    # Open gabor filtered images for each sample and prepare csv row
    for fold in goodFolders:
      goodImgs=[ f for f in os.listdir(fold) if isfile(join(fold,f))]
      goodImgs.sort()
      
      for f in goodImgs:
        print "INFO: Processing '%s'" % join(fold,f)
        tf.write("P")     # POSITIVE
        img = cv.imread( join(fold,f) , cv.CV_LOAD_IMAGE_GRAYSCALE)
        if img is None:
          print "WARN: cannot open image %s, skip" % join(fold,f)
          continue
        for i in xrange (img.shape[1]):
          for j in xrange(img.shape[0]):
            value = img.item(j, i)
            tf.write(",%d"%value)
      
      tf.write("\n")
    
    for fold in badFolders:
      badImgs=[f for f in os.listdir(fold) if isfile(join(fold,f))]
      badImgs.sort()
      
      for f in badImgs:
        print "INFO: Processing '%s'" % join(fold,f)
        tf.write("N")     # NEGATIVE
        img = cv.imread( join(fold,f) ,cv.CV_LOAD_IMAGE_GRAYSCALE)
        if img is None:
          print "WARN: cannot open image %s, skip" % join(fold,f)
          continue
        for i in xrange (img.shape[1]):
          for j in xrange(img.shape[0]):
            value = img.item(j, i)
            tf.write(",%d"%value)
      
      tf.write("\n")
  
  print "INFO: Done"


def dataset_prepTrainFiles( dsFolder, config):
  """
      Prepare training files
  """
  for x in _dataset_multiclass1to1(config):
    print "INFO: prepare gabor trainig file for %s" % x
    dataset_prepTrain1to1Gabor( x, dsFolder, config )


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("datasetFolder",help="Dataset folder")
  args = parser.parse_args()
  config={}
  configFile=join(args.datasetFolder,_DATASET_CONFIG_FILE)
  if not os.path.exists(configFile):
    print "ERR: dataset configuration file '%s' not found" % _DATASET_CONFIG_FILE
    exit(-1)
  print "INFO: Reading configuration file at '%s' " %configFile
  execfile(configFile, config)
  dataset_prepTrainFiles( args.datasetFolder, config)

