# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:42:22 2018

"""

import pandas as pd
import numpy as np

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
# Print only the data in the head specified.
print(df.head(10))
print(df.dtypes)

#build new data frames
int_df = df.select_dtypes(include=['int64']).copy()
print(int_df.head()) #default head size 5


#build new data frame with object

obj_df = df.select_dtypes(include=['object']).copy()
print(obj_df.head(10))
#filtering nan rows,  there are a couple of null 
#values in the data that we need to clean up.
#Axis 0 will act on all the ROWS in each COLUMN
#Axis 1 will act on all the COLUMNS in each ROW
print(obj_df[obj_df.isnull().any(axis=1)])

print(obj_df["num_cylinders"].value_counts())

#find and replace

cleanup_nums = {"num_doors":     {"four": 4, "two": 2},
                "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8,
                                  "two": 2, "twelve": 12, "three":3 }}
obj_df.replace(cleanup_nums, inplace=True)
print(obj_df["num_cylinders"].value_counts())

#label encoding and preprocessing

from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
obj_df["make_code"] = lb_make.fit_transform(obj_df["make"])
print(obj_df[["make", "make_code"]].head(11))
