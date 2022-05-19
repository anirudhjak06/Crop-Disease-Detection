# Crop-Disease-Detection
## A Deep Learning Project 

## Introduction
- Agricultural production rate plays a vital role in the economic
development of a country.
- The identification of plant diseases at an early stage is crucial for global health and wellbeing. So, controlling on the diseased leaves
during the growing stages of crops is a crucial step.
- Moreover, increasing crop production is essential to areas where food is scarce.
- Loss of crops from plant diseases would result in
reduction of income for crop producers, higher
prices for consumers and significant economic impact.
- The access to disease-control methods is limited
which results in annual losses of 30 to 50
percent for major crops in various countries. 
- Hence, detection of crop diseases is very crucial for economic development.

## Problem Motivation
- Agriculture is a very important sector of the Indian
economy.
- The share of agriculture in GDP increased to 20.2 per cent
in 2020-21 from 18.4 per cent in 2019-20.
- So, for the identification and detection of plant diseases,
human raters are employed.
- This process is very time consuming and expensive and
sometimes may lead to poorly identify the crop disease.
- Thus, continuous monitoring must be done which is a repetitive
process which involves large group of experts costing very high
when dealing with large farms.
- Therefore, this motivated us to automate the process and
perform evaluation metrics, based on a deep learning classifier.

## Problem Statement
- Detect the crop diseases.
- Differentiate between various crop
diseases for a particular plant and then
for many various plants.
- Using object detection algorithms to find
the diseased area in the crop on the basis
of the features such as color, wilt, leaf
spots, unusual size of the leaf.
- Choosing appropriate neural network for
classification. 

## Objective
1. Our Main Objective is that given the images of a specific crop, it
should classify it as a healthy crop or the disease it may be
infected with.
2. We intend to use deep convolutional neural networks (D-CNN)
and some concepts of image processing to reach our goal of
identifying the disease of a plant using color, leaf spots, etc.
3. Also, if time permits, we are also planning to develop a web based
application so that it can be used widely by large number of
people to determine crop diseases.

For more details about the project, please refer to [**"Crop Disease Detection PPT.pdf"**][1].

[1]: https://github.com/anirudhjak06/Crop-Disease-Detection/blob/main/Crop%20Disease%20Detection%20PPT.pdf "Title"

## Dataset Description
The dataset has different types of diseases for tomato leaves. There are 10 classes present which is shown below.

- Here goes the list:
  - Tomatomosaicvirus
  - Target_Spot
  - Bacterial_spot
  - TomatoYellowLeafCurlVirus
  - Late_blight
  - Leaf_Mold
  - Early_blight
  - Spidermites Two-spottedspider_mite
  - Tomato___healthy
  - Septorialeafspot

- The total number of images present are :
  - 10000 images for training data
  - 1000 images for validation data

- The data set contains the top 10 classes of diseases which are
highly occured on tomato plant.
- The images had taken with different angles, with different
backgrounds, and in different lighting conditions with an image size is 255 X 255 pixels.

For more details about the dataset, please refer the [**"Dataset"**][2].

[2]: https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf "Title"

## Models Implemented

We have implemented 3 models successfully on tomato plant.
1. CNN (with 3 different variants)
2. INCEPTION-v3
3. VGG-16

## Group Members

<pre>
Anirudh Jakhotia  - S20190010007
Khushi Pathak     - S20190010091
V.Naveen Kumar    - S20190010192
</pre>
