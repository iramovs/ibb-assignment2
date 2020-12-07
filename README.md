# ABB Assignment 2 - Ear Detection Using Cascade Classifiers
- Author: Iztok Ramovš

## Requirements (tested on following versions)
- Python 3.8.5
- OpenCV 4.4.0
- Numpy 1.19.4

## Instructions for running the project
```bash
# Run one evaluation of model on AWE database
# detector_ear_haar_pretrained.py <scaleFactor> <minNeighbors> <modelNumber>
# results are given in following format:
# <info about current evaluation>:
# [<IoU>, <Precision>, <Recall>]
# [<IoU Stdev>, <Precision Stdev>, <Recall Stdev>]
python detector_ear_haar_pretrained.py 1.05 5 0

# Run script for evaluating different parameters and models and save into a file
./run_different_models_params.sh > results.txt

# Preprocess train images from AWE database for cascade training,
# images are saved to ibb-assignment2/cascade_training/positive_images/
python preprocess_train.py
```