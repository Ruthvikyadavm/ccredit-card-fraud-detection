# 🏦 Credit Card Fraud Detection Pipeline

This project demonstrates a full end-to-end data pipeline for detecting fraudulent credit card transactions using machine learning and cloud-based technologies.

## 📌 Objective

To process transactional data, build a fraud detection model, and automate the workflow using AWS and PySpark.

## 🧰 Technologies Used

- Python, Pandas, PySpark
- AWS S3, AWS Glue, Amazon Redshift
- Apache Airflow
- Scikit-learn
- Power BI (for visualization)

## ⚙️ Pipeline Overview

1. **Data Ingestion**: Simulated credit card transaction data is pulled from an API and stored in AWS S3.
2. **ETL Processing**: PySpark cleans and aggregates the data using AWS Glue jobs.
3. **Model Training**: Random Forest classifier is used to predict fraud.
4. **Automation**: Apache Airflow schedules hourly runs.
5. **Analytics**: Results are loaded into Redshift and visualized in Power BI dashboards.

## 📁 Project Structure
credit-card-fraud-detection/
├── data/ # Sample datasets
├── etl_pipeline.py # Data cleaning and transformation script
├── model_training.py # ML model script
├── airflow_dag.py # DAG script for scheduling
├── requirements.txt # List of dependencies
└── README.md # Project overview

## 📊 Results

- Achieved **92% accuracy** in fraud prediction using the Random Forest model.
- Automated the entire pipeline using Apache Airflow with hourly DAG runs.
- Created a Power BI dashboard to visualize fraud transaction trends and flagged activities.
