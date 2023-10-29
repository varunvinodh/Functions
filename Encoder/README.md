# Categorical Data Encoding for Machine Learning:
This repository contains a Python script for managing categorical data in preparation for machine learning tasks. It includes functions for encoding categorical data using LabelEncoder, decoding the encoded data, and handling unseen labels in the data. These functions help ensure that categorical data is properly processed and encoded for machine learning models.

## Key Features:

**text_to_numbers:** Encode categorical columns using LabelEncoder and save the encoders for later use.

**re_encode:** Re-encode categorical columns, handling unseen labels and maintaining consistency.

**remove_row_fit:** Remove rows with unseen labels in a specific categorical column and re-encode the data.

**numbers_to_text:** Decode previously encoded categorical columns to their original values.

## Usage:
You can use these functions to preprocess and manage categorical data in your machine learning projects. They simplify the procedure of storing encoder files for individual datasets, allowing you to reuse them in the future. The script is designed to make it easier to work with categorical data, especially when dealing with unseen labels and encoding consistency.

## For more understanding reffer to the docstrings for detailed understanding on each function.
 
