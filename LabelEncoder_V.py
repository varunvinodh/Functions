#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# ## Encoder 

# ### LabelEncoder

# In[18]:


from sklearn.preprocessing import LabelEncoder 


######################### LABEL ENCODER #########################
# Creating a Encoder function to save the encoders
def text_to_numbers(df): 
    """
    Encode categorical columns in a DataFrame using LabelEncoder and save the encoders.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data with categorical columns.

    Returns:
    - DataFrame: The updated DataFrame with categorical columns encoded.
    - dict: A dictionary storing label encoders for each encoded column.
    """
    le_dict = dict() 
    col = df.select_dtypes(include=['object']).columns 
    for i in col: 
        print(i)
        le_dict[i] = LabelEncoder() 
        df[i] = le_dict[i].fit_transform(df[i]) 
    return df, le_dict 
    

# Fit Encoder for categorical columns
def re_encode(df,le_dict):
    """
    Re-encode categorical columns in a DataFrame and handle unseen labels.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data with categorical columns.
    - le_dict (Dictionary): A dictionary storing label encoders for various columns in the DataFrame.

    Returns:
    - DataFrame: The updated DataFrame with re-encoded categorical columns and rows with unseen labels removed.
    """
    for i in le_dict.keys():
        try:
            df[i] = le_dict[i].transform(test_df[i])
        except Exception as e:
            print(e)
            df = remove_row_fit(df, le_dict, i)
    return df

# Function to remove rows with unseen labels and fit the encoder
def remove_row_fit(df, le_dict, i):
    """
    Remove rows with unseen labels and re-encode a specific categorical column.

    Parameters:
    df (DataFrame)      : The input DataFrame containing the data with categorical columns.
    le_dict (Dictionary): A dictionary storing label encoders for various columns in the DataFrame.
    i (String)          : Represents the name of a specific column within the DataFrame that you want to process. It is a column name.
    
    Returns:
    - DataFrame: The updated DataFrame with rows containing unseen labels removed and re-encoded values.
    """
    for j in df[i].unique():
        if j in list(le_dict[i].classes_):
            pass
        else:
            print(j, " is an Unseen label in the column ", i)
            df = df[(df[i] != j)].copy()
            df[i] = le_dict[i].transform(df[i])
    return df


def numbers_to_text(df, le_dict): 
    """
    Decode previously encoded categorical columns using label encoders.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data with encoded categorical columns.
    - le_dict (dict): A dictionary storing label encoders for each encoded column.

    Returns:
    - DataFrame: The updated DataFrame with categorical columns decoded to their original values.
    """
    for i in le_dict.keys(): 
        df[i] = le_dict[i].inverse_transform(df[i]) 
    return df


# In[19]:





# In[ ]:




