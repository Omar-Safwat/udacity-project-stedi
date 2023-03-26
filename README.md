# Project motivation
In this project, I build a data lakehouse solution for sensor data that trains a machine learning model.


The **STEDI** Team has developed a hardware **STEDI** Step Trainer that:
* Trains the user to do a **STEDI** balance exercise.
* Has sensors on the device that collect data to train a machine-learning algorithm to detect steps.
* Has a companion mobile app that collects customer data and interacts with the device sensors.

The Step Trainer is a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions. The **STEDI** team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.


Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

# Project Summary
The goal is to extract the data produced by the **STEDI** Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model. 

 
Using AWS Glue, AWS S3, Python, and Spark, create or generate Python scripts to build a lakehouse solution in AWS that satisfies the requirements set by **STEDI** data scientists.

## Project Requirements
The Data Science team has done some preliminary data analysis and determined that the Accelerometer Records each match one of the Customer Records. They would to create 2 AWS Glue Jobs that do the following:

1. Sanitize the Customer data from the Website (Landing Zone) and only store the Customer Records who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called **customer_trusted**.
2. Sanitize the Accelerometer data from the Mobile App (Landing Zone) - and only store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called **accelerometer_trusted**.

The Data Scientists later have discovered a data quality issue with the Customer Data. The serial number should be a unique identifier for the STEDI Step Trainer they purchased. However, there was a defect in the fulfillment website, and it used the same 30 serial numbers over and over again for millions of customers. Most customers have not received their Step Trainers yet, but those who have, are submitting Step Trainer data over the IoT network (Landing Zone). The data from the Step Trainer Records has the correct serial numbers.

To solve this problem we need to write a Glue job that does the following:

1. Sanitize the Customer data (Trusted Zone) and create a Glue Table (Curated Zone) that only includes customers who have accelerometer data and have agreed to share their data for research called customers_curated.

Finally, you need to create two Glue Studio jobs that do the following tasks:
1. Read the Step Trainer IoT data stream (S3) and populate a Trusted Zone Glue Table called **step_trainer_trusted** that contains the Step Trainer Records data for customers who have accelerometer data and have agreed to share their data for research (**customers_curated**).
2. Create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and make a glue table called **machine_learning_curated**.

# Project Data
**STEDI** has three JSON data sources to use from the Step Trainer. You can [download the data](https://video.udacity-data.com/topher/2022/June/62be2ed5_stedihumanbalanceanalyticsdata/stedihumanbalanceanalyticsdata.zip) from here or you can extract it from their respective public S3 bucket locations.

## 1. Customer Records
contains the following fields:
* serialnumber
* sharewithpublicasofdate
* birthday
* registrationdate
* sharewithresearchasofdate
* customername
* email
* lastupdatedate
* phone
* sharewithfriendsasofdate

## 2. Step Trainer Records (data from the motion sensor):
contains the following fields:
* sensorReadingTime
* serialNumber
* distanceFromObject

## 3. Accelerometer Records (from the mobile app):
contains the following fields:
* timeStamp
* serialNumber
* x
* y
* z