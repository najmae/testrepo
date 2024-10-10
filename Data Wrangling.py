{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "prev_pub_hash": "90ac80ca41fde58b95f02cc0cfc0a0f2ed3115615ffe1bdfdfc10fd5ffeef9a4"
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "<p style=\"text-align:center\">\n    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01\" target=\"_blank\">\n    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"400\" alt=\"Skills Network Logo\"  />\n    </a>\n</p>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# **Data Wrangling Lab**\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Estimated time needed: **45 to 60** minutes\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this assignment you will be performing data wrangling.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## Objectives\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this lab you will perform the following:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "-   Identify duplicate values in the dataset.\n\n-   Remove duplicate values from the dataset.\n\n-   Identify missing values in the dataset.\n\n-   Impute the missing values in the dataset.\n\n-   Normalize data in the dataset.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## Hands on Lab\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Import pandas module.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "import pandas as pd",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stderr",
          "text": "<ipython-input-1-7dd3504c366f>:1: DeprecationWarning: \nPyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),\n(to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)\nbut was not found to be installed on your system.\nIf this would cause problems for you,\nplease provide us feedback at https://github.com/pandas-dev/pandas/issues/54466\n        \n  import pandas as pd\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 1
    },
    {
      "cell_type": "markdown",
      "source": "Load the dataset into a dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>Read Data</h2>\n<p>\nWe utilize the <code>pandas.read_csv()</code> function for reading CSV files. However, in this version of the lab, which operates on JupyterLite, the dataset needs to be downloaded to the interface using the provided code below.\n</p>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The functions below will download the dataset into your browser:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from pyodide.http import pyfetch\n\nasync def download(url, filename):\n    response = await pyfetch(url)\n    if response.status == 200:\n        with open(filename, \"wb\") as f:\n            f.write(await response.bytes())",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 2
    },
    {
      "cell_type": "code",
      "source": "file_path = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv\"",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "To obtain the dataset, utilize the download() function as defined above:  \n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "await download(file_path, \"m1_survey_data.csv\")\nfile_name=\"m1_survey_data.csv\"",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "Utilize the Pandas method read_csv() to load the data into a dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df = pd.read_csv(file_name)",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "> Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface.While working on the downloaded version of this notebook on their local machines(Jupyter Anaconda), the learners can simply **skip the steps above,** and simply use the URL directly in the `pandas.read_csv()` function. You can uncomment and run the statements in the cell below.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#df = pd.read_csv(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv\")",
      "metadata": {},
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "markdown",
      "source": "## Finding duplicates\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this section you will identify duplicate values in the dataset.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": " Find how many duplicate rows exist in the dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n\n# Check for duplicate rows\nimport pandas as pd\nfrom pyodide.http import pyfetch\nasync def download(url, filename):\n    response = await pyfetch(url)\n    if response.status == 200:\n        with open(filename, \"wb\") as f:\n            f.write(await response.bytes())\nfile_path = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv\"\nawait download(file_path, \"m1_survey_data.csv\")\nfile_name=\"m1_survey_data.csv\"\ndf = pd.read_csv(file_name)\nduplicate_rows = df.duplicated()\n# Sum up the duplicates\nnum_duplicates = duplicate_rows.sum()\nprint(f\"Number of duplicate rows: {num_duplicates}\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of duplicate rows: 154\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 14
    },
    {
      "cell_type": "code",
      "source": "#After removing the duplicate rows, how many blank rows are there under the column EdLevel?\n# Drop duplicate rows\ndf.drop_duplicates(inplace=True)\n\n# Check for blank rows in the column 'EdLevel'\nblank_edlevel_rows = df['EdLevel'].isna().sum()\nblank_edlevel_rows",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 36,
          "output_type": "execute_result",
          "data": {
            "text/plain": "112"
          },
          "metadata": {}
        }
      ],
      "execution_count": 36
    },
    {
      "cell_type": "code",
      "source": "#After removing the duplicate rows, how many rows are missing under the column Country?\n# Check for missing rows in the column 'Country'\nmissing_country_rows = df['Country'].isna().sum()\nmissing_country_rows",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 38,
          "output_type": "execute_result",
          "data": {
            "text/plain": "0"
          },
          "metadata": {}
        }
      ],
      "execution_count": 38
    },
    {
      "cell_type": "markdown",
      "source": "## Removing duplicates\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Remove the duplicate rows from the dataframe.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Remove duplicates\ndf = df.drop_duplicates()\n\n# Verify if duplicates are removed\nprint(f\"Number of rows after removing duplicates: {len(df)}\")\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of rows after removing duplicates: 11398\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 15
    },
    {
      "cell_type": "markdown",
      "source": "Verify if duplicates were actually dropped.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Verify no duplicates remain\nduplicate_rows_after = df.duplicated().sum()\nprint(f\"Number of duplicate rows after removal: {duplicate_rows_after}\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of duplicate rows after removal: 0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 16
    },
    {
      "cell_type": "markdown",
      "source": "## Finding Missing values\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Find the missing values for all columns.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Check for missing values\nmissing_values = df.isnull().sum()\nprint(missing_values)\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Respondent        0\nMainBranch        0\nHobbyist          0\nOpenSourcer       0\nOpenSource       81\n               ... \nSexuality       542\nEthnicity       675\nDependents      140\nSurveyLength     19\nSurveyEase       14\nLength: 85, dtype: int64\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 17
    },
    {
      "cell_type": "markdown",
      "source": "Find out how many rows are missing in the column 'WorkLoc'\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Count missing values in 'WorkLoc' column\nmissing_workloc = df['WorkLoc'].isnull().sum()\nprint(f\"Number of missing values in WorkLoc: {missing_workloc}\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of missing values in WorkLoc: 32\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 18
    },
    {
      "cell_type": "code",
      "source": "# After removing the duplicate rows, how many rows are there in the dataset?\ndf.drop_duplicates(inplace=True)\nnum_rows_after_removal = df.shape[0]\nnum_rows_after_removal\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 32,
          "output_type": "execute_result",
          "data": {
            "text/plain": "11398"
          },
          "metadata": {}
        }
      ],
      "execution_count": 32
    },
    {
      "cell_type": "code",
      "source": "#After removing the duplicate rows, how many unique rows are there in the column 'Respondent'?\nnum_unique_respondents = df['Respondent'].nunique()\nnum_unique_respondents\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 34,
          "output_type": "execute_result",
          "data": {
            "text/plain": "11398"
          },
          "metadata": {}
        }
      ],
      "execution_count": 34
    },
    {
      "cell_type": "markdown",
      "source": "## Imputing missing values\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Find the  value counts for the column WorkLoc.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Value counts for 'WorkLoc'\nworkloc_counts = df['WorkLoc'].value_counts()\nprint(workloc_counts)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "WorkLoc\nOffice                                            6806\nHome                                              3589\nOther place, such as a coworking space or cafe     971\nName: count, dtype: int64\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 19
    },
    {
      "cell_type": "markdown",
      "source": "Identify the value that is most frequent (majority) in the WorkLoc column.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#make a note of the majority value here, for future reference\n#\n# Find the most frequent value in 'WorkLoc'\nmost_frequent_workloc = df['WorkLoc'].value_counts().idxmax()\nprint(f\"The most frequent value in WorkLoc: {most_frequent_workloc}\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "The most frequent value in WorkLoc: Office\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 20
    },
    {
      "cell_type": "markdown",
      "source": "Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Replace missing values in 'WorkLoc' with the most frequent value (without inplace)\ndf['WorkLoc'] = df['WorkLoc'].fillna(most_frequent_workloc)\n# Check if there are still any missing values in 'WorkLoc'\nprint(df['WorkLoc'].isnull().sum())\n\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 29
    },
    {
      "cell_type": "markdown",
      "source": "After imputation there should ideally not be any empty rows in the WorkLoc column.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Verify if imputing was successful.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n\n# Verify if missing values were filled\nmissing_workloc_after = df['WorkLoc'].isnull().sum()\nprint(f\"Number of missing values in WorkLoc after imputation: {missing_workloc_after}\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of missing values in WorkLoc after imputation: 0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 22
    },
    {
      "cell_type": "markdown",
      "source": "## Normalizing data\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "There are two columns in the dataset that talk about compensation.\n\nOne is \"CompFreq\". This column shows how often a developer is paid (Yearly, Monthly, Weekly).\n\nThe other is \"CompTotal\". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her \"CompFreq\". \n\nThis makes it difficult to compare the total compensation of the developers.\n\nIn this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.\n\nOnce this column is ready, it makes comparison of salaries easy.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "List out the various categories in the column 'CompFreq'\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Check unique values in 'CompFreq'\ncompfreq_categories = df['CompFreq'].unique()\nprint(compfreq_categories)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "['Yearly' 'Monthly' 'Weekly' nan]\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 23
    },
    {
      "cell_type": "markdown",
      "source": "Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Double click to see the **Hint**.\n\n<!--\n\nUse the below logic to arrive at the values for the column NormalizedAnnualCompensation.\n\nIf the CompFreq is Yearly then use the exising value in CompTotal\nIf the CompFreq is Monthly then multiply the value in CompTotal with 12 (months in an year)\nIf the CompFreq is Weekly then multiply the value in CompTotal with 52 (weeks in an year)\n\n-->\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# your code goes here\n# Normalize compensation\ndef normalize_compensation(row):\n    if row['CompFreq'] == 'Yearly':\n        return row['CompTotal']\n    elif row['CompFreq'] == 'Monthly':\n        return row['CompTotal'] * 12\n    elif row['CompFreq'] == 'Weekly':\n        return row['CompTotal'] * 52\n    else:\n        return None\n\n# Apply the normalization function and create new column\ndf['NormalizedAnnualCompensation'] = df.apply(normalize_compensation, axis=1)\n\n# Display the updated dataframe\ndf[['CompFreq', 'CompTotal', 'NormalizedAnnualCompensation']].head()\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 24,
          "output_type": "execute_result",
          "data": {
            "text/plain": "  CompFreq  CompTotal  NormalizedAnnualCompensation\n0   Yearly    61000.0                       61000.0\n1   Yearly   138000.0                      138000.0\n2   Yearly    90000.0                       90000.0\n3  Monthly    29000.0                      348000.0\n4   Yearly    90000.0                       90000.0",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>CompFreq</th>\n      <th>CompTotal</th>\n      <th>NormalizedAnnualCompensation</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Yearly</td>\n      <td>61000.0</td>\n      <td>61000.0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Yearly</td>\n      <td>138000.0</td>\n      <td>138000.0</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Yearly</td>\n      <td>90000.0</td>\n      <td>90000.0</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Monthly</td>\n      <td>29000.0</td>\n      <td>348000.0</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Yearly</td>\n      <td>90000.0</td>\n      <td>90000.0</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 24
    },
    {
      "cell_type": "code",
      "source": "#How many unique values are there in the CompFreq column?\n# Count unique values in the 'CompFreq' column\nunique_comp_freq = df['CompFreq'].nunique()\nprint(\"Number of unique values in 'CompFreq' column:\", unique_comp_freq)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of unique values in 'CompFreq' column: 3\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 44
    },
    {
      "cell_type": "code",
      "source": "#After removing the duplicate rows, how many respondents are being paid yearly?\n# Count respondents being paid yearly\nyearly_paid_respondents = df[df['CompFreq'] == 'Yearly'].shape[0]\nprint(\"Number of respondents being paid yearly:\", yearly_paid_respondents)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of respondents being paid yearly: 6073\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 45
    },
    {
      "cell_type": "code",
      "source": "#What is the median NormalizedAnnualCompensation?\n# Calculate the median of the 'NormalizedAnnualCompensation' column\nmedian_normalized_annual_compensation = df['NormalizedAnnualCompensation'].median()\nprint(\"Median NormalizedAnnualCompensation:\", median_normalized_annual_compensation)\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Median NormalizedAnnualCompensation: 100000.0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 46
    },
    {
      "cell_type": "code",
      "source": "# What is the majority category under the column Employment?\n# Find the most frequent category in the 'Employment' column\nmajority_employment = df['Employment'].value_counts().idxmax()\nmajority_employment\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 40,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Employed full-time'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 40
    },
    {
      "cell_type": "code",
      "source": "#Under the column UndergradMajor, which category has the minimum number of rows?\n# Find the category with the minimum number of rows in the 'UndergradMajor' column\nminimum_undergrad_major = df['UndergradMajor'].value_counts().idxmin()\nminimum_undergrad_major\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 41,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'A health science (ex. nursing, pharmacy, radiology)'"
          },
          "metadata": {}
        }
      ],
      "execution_count": 41
    },
    {
      "cell_type": "code",
      "source": "#The column ConvertedComp contains the annual compensation of the survey respondents. What is the best approach to impute the missing values in this column?\n# Find the median value of 'ConvertedComp'\nmedian_converted_comp = df['ConvertedComp'].median()\n\n# Fill missing values in 'ConvertedComp' using the median without chained assignment\ndf['ConvertedComp'] = df['ConvertedComp'].fillna(median_converted_comp)\n\n# Verify if the missing values are filled\nprint(\"Number of missing values in 'ConvertedComp':\", df['ConvertedComp'].isnull().sum())\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Number of missing values in 'ConvertedComp': 0\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 43
    },
    {
      "cell_type": "markdown",
      "source": "## Authors\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Ramesh Sannareddy\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "### Other Contributors\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Rav Ahuja\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": " Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<!--## Change Log\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<!--| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |\n| ----------------- | ------- | ----------------- | ---------------------------------- |\n| 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |--!>\n",
      "metadata": {}
    }
  ]
}