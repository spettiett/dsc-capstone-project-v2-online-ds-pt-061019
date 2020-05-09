
<IMG SRC="TOC_Image_Heading.png" ALT="Capstone Project">

## Final Project Submission

* __Student name:__ Sharonda Pettiett-Warner
* __Student pace:__ part time - PT_0610
* __Scheduled project review date/time:__ April 24, 2020
* __Instructor name:__ Eli Thomas

## Project Description
This project walks you through several data science concepts and tools to help you gain more insights on important features used to predict hotel booking demand.

## The Dataset

This data set contains a single file which compares various booking information between two hotels: a city hotel and a resort hotel.  This data set includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things.

> __Feature Description__

<IMG SRC="TOC_Image_FeatDesc.png" ALT="Feature Description">

## Acknowledgements

- The hotel booking dataset from a kernel in Kaggle.
- The data is originally from the article Hotel Booking Demand Datasets, written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.


# How to Navigate Jupyter Notebooks for Capstone Review

> __Order of Navigation:__
- __Part I   :__ Jupyter Notebook: __Capstone_EDA.ipynb__
- __Part II  :__ Jupyter Notebook: __Capstone_Hypothesis Testing.ipynb__
- __Part III :__ Jupyter Notebook: __Capstone_ML_Model - (Baseline and FeatEngr).ipynb__
- __Part IV  :__ Jupyter Notebook: __Capstone_ML_Model (Final Prediction).ipynb__
- __Part V   :__ Jupyter Notebook: __Capstone_Model_Prediction_Using_Tkinter.ipynb__(Demo)
- __Part VI  :__ Jupyter Notebook: __Capstone_Time Series.ipynb__
- __Part VII :__ Jupyter Notebook: __Capstone_Plotly_Graphs.ipynb__
- __Part VIII:__ Jupyter Notebook: __Capstone_ML_Model(LazyPredict).ipynb__

# Learning Concepts and Tools

__Data Science Concepts Used:__
- Machine Learning (ML)
- Hypothesis Testing
- Time Series
- Data Visualization
- Data Cleaning
- Data Exploration
- Feature Engineering

__Tools Used:__
- Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
- Plotly's Python graphing library makes interactive, publication-quality graphs.
- pickle — Python object serialization.

__Machine Learning Models Used:__
- GaussianNB
- LogisticRegression 
- LinearDiscriminantAnalysis
- KNeighborsClassifier
- DecisionTreeClassifier
- RandomForestClassifier
- AdaBoostClassifier
- GradientBoostingClassifier
- XGBClassifier
- LazyPredict Classifier

# Capstone Overview

## Project Motivation
> As a person who loves to travel I was very curious to see if I could use my new found skills in data science to solve "one of my biggest annoyances" - __hotel overbooking__.  But, first I would need to understand some of the drivers that create this unpleasant experience for customers, like myself. So, this project will walk you through several data science concepts and tools to help you gain more insights on important features used to predict hotel booking demand.

## Problem Statement
- Reservations for resorts and hotels in __Lisbon, Portugal__ are experiencing __37%__ cancellations.

<IMG SRC="./PPT_IMG/target_distribution_percnt.png" ALT="Target Percent">

## Business Value
> Equipped with more insightful information about __where, when, and why__ these cancellations are happening, a hotel’s revenue manager can make better informed decisions and improve overbooking strategies and cancellation policies.

__Questions to answer from the data:__

- Where do the guests come from?
- How much do guests pay for a room per night?
- Which are the most busy month?
- Bookings by market segment
- How many bookings were canceled?
- Which month have the highest number of cancelations?
- Which hotel has more cancelations?
- Any difference in lead time?
- Any difference in market segments?
- How about distribution channels?
- How about Month, Day, and Week Number?

<IMG SRC="./PPT_IMG/TOC_Image_PRT-1.png" ALT="TOC_Image_PRT">

## Hypothesis Testing

Hypothesis testing is a strong and very important statistical tool that enable us to test conventional knowledge using sample data. Most parametric testing assume normality, but thanks to the central limit theorem, it is possible to bypass this assumption with large enough samples. Moreover, a variation of the two sample t-test called __Welch’s t-test__ enables us to compare two sample means with unequal variances, which are the tests used to perform this study.

> This test was performed to answer the following question:
- __Does booking far in advance increases the probability of cancellation?__ 

__Lead time__ is a feature in the dataset that significantly contributes to canceled reservations. Booking a reservation 7 days or more in advance increases the probability for a canceled reservation. 

__Cancellation Percentage:__ 0-6 days = 2.5 % more than 30 days  85%.

## Machine Learning Modeling
To tackle the uncertainty arising from booking cancellations, we reviewed the data from booking information for a city hotel and a resort hotel which included information such as,  when the booking was made; length of stay; the number of adults children, and/or babies and the number of available parking spaces, among other things.  Then, I used machine learning algorithms to develop booking cancellation prediction models for the hotels. 

<IMG SRC="./PPT_IMG/TOC_Image_MLModels.png" ALT="TOC_Image_MLModels">

> __Best Model__ 

__Random Forest Classification__ have the “highest” scoring metrics:

- __Test Accuracy Score: 0.877677  |   Train Accuracy Score: 0.939452__
- __Accuracy Score:__ 0.8776766335158249   
- __Precision Score:__ 0.8693262411347518  
- __roc_auc_score:__ 0.8656552631067826 

> __Most Predictive Features__

From our analysis, we concluded that the most useful features for prediction were the following features (Top 15):

- lead_time                        0.116716
- deposit_type_Non Refund          0.108665
- country_PRT                      0.080293
- adr                              0.078294
- total_of_special_requests        0.069174
- arrival_date_day_of_month        0.056989
- agent                            0.051549
- arrival_date_week_number         0.048732
- stays_in_week_nights             0.037315
- previous_cancellations           0.030105
- stays_in_weekend_nights          0.025514
- arrival_date_year                0.024081
- required_car_parking_spaces      0.020868
- market_segment_Online TA         0.020407
- customer_type_Transient          0.019232

## Demonstration - Model Prediction (GUI)
To simulate a real production environment using of the models Random Forest Classifier, I built a Graphical User Interface (GUI) using Python - Tkinker to capture user input related to hotel booking key features to perform a prediction as either Booked or Canceled along with the prediction probability. Having an application, such as this, could help to enable hoteliers to decrease the number of cancellations, thus, increasing confidence in demand-management decisions. 


<IMG SRC="./PPT_IMG/TOC_Image_GUI.png" ALT="TOC_Image_GUI">

## Time Series
> Another key component, was to improvement the forecast accuracy. So, a time series model was built to help predict number of cancellations in the future.

__SARIMAX(2,2,1)x(1, 1, 0, 52)__ yields the "lowest" __AIC value of 422.779__. Therefore, we considered this to be optimal option out of all the models we have considered and the "p-values" __(P>|z|) 0.000 < .05__.

__Real vs Predicted values along with confidence interval__

<IMG SRC="./PPT_IMG/TOC_Image_TimeSeries-1.png" ALT="TOC_Image_TimeSeries-1">

__Model Evaluation Scores__
- Mean squared error: 211.47669613545847
- Mean absolute error: 11.843198228847259
- RMSE: 14.542238346810937

__Performing Predictons in the future__

<IMG SRC="./PPT_IMG/TOC_Image_TimeSeries-2.png" ALT="TOC_Image_TimeSeries-2">

- RMSE value ≥0.5 reflects the poor ability of the model to accurately predict the data, in this case RMSE: 14.54 from One-step Ahead Forecasting.
- This time series has low-volume count data (less than 3 years of data); having MORE data could greatly improve the forecasting.

# Capstone Conclusions

> By exposing cancellation drivers, machine learning models can help hoteliers to better understand booking cancellation patterns and enable the adjustment of a hotel’s cancellation policies and overbooking tactics according to the characteristics of its bookings.
Moreover, this work shows that if hotel managers had access to an application (GUI) then they could act on bookings with high cancellation probability and contain the associated revenue losses.  Leading to other benefits, such as, improve overbooking/cancellation policies, and have more assertive pricing and staffing allocation strategies.

<IMG SRC="./TOC_Image_Thankyou.png" ALT="TOC_Image_Thankyou">
