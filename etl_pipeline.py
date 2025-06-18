import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder \
    .appName("ETL - Credit Card Fraud Detection") \
    .getOrCreate()

# Load data (replace with S3 path in real case)
df = spark.read.csv("data/credit_card_transactions.csv", header=True, inferSchema=True)

# Basic cleaning
df_clean = df.dropna() \
             .withColumn("Amount", col("Amount").cast("float")) \
             .withColumn("Time", col("Time").cast("int")) \
             .withColumn("Class", col("Class").cast("int"))  # 'Class' is the label (0: legit, 1: fraud)

# Save cleaned data (for model training)
df_clean.write.mode("overwrite").csv("data/cleaned_transactions.csv", header=True)

print("ETL job completed successfully.")
