# Japan Spark and Azure Project: Azure Data Engineering Project 🎌

Project with end-to-end data processing and visualization of [visa numbers in Japan](https://github.com/tertub2/Japan_SparkandAzure_Project/tree/master/src/input) using PySpark and Plotly. The tools used were spark clusters that were set up within a Docker container on Azure.

## 📚 Table of Contents

The table of contents aims to show the stages of the project along with some details and features present in the project

- [System Architecture](#-architecture)

- [Setup](#-setup)

- [EDA](#-eda)

- [Transformations](#-transformations)

- [Results](#-results)



## ⛓️ Architecture
![Project Architecture Scheme](https://github.com/tertub2/Japan_SparkandAzure_Project/blob/master/architecture.png)


## 🛠️ Setup
- Azure: Active account in azure (needed to create a VM)
- Docker: The Spark master-worker architecture has been deployed within a Docker container hosted on Azure.
- Python (Libraries): Pyspark, Fuzzywuzzy, Pycountry_convert, Pycountry and Plotly Express.
- Linux: VM with linux (Ubuntu) used.

  
## ⛩️ EDA
- Exploratory Data Analysis (EDA) and Cleaning: This section involves analyzing the dataset to identify errors, null values, and insights, as well as tendencies that may need to be addressed before proceeding with transformations. It serves as a crucial step in understanding the data and preparing it for further analysis. This secton was made in this [notebook](https://github.com/tertub2/Japan_SparkandAzure_Project/blob/master/src/jobs/EDA%20-%20Applications%20In%20Japan.ipynb).
  

## 📈 Transformations
- System Architecture: The Spark master-worker architecture is set up in a Docker container on Azure.
- Data Ingestion: The script ingests the CSV file containing the visa numbers in Japan.
- Data Cleaning: The script standardizes column names, drops null columns, and corrects country names using fuzzy matching.
- Data Transformation: The data is further enriched by adding continent information for each country.
- Data Visualization: The cleaned and transformed data is visualized using Plotly Express to provide insights into visa trends in Japan.
- The notebook for this step may be seen [here](https://github.com/tertub2/Japan_SparkandAzure_Project/blob/master/src/jobs/vis.py).

## ✅ Results 
The project successfully achieved its focus on Data Engineering, leveraging all the pre-selected tools. As for the analysis results, several key findings stand out and deserve highlighting:
#### - Between 2010 and 2017, a noticeable trend emerged among the top 10 countries with more visa issued in Japan: a predominant presence of Asian nations, with China, the Philippines, and Indonesia securing the top three spots. China leads by a significant margin with 14 million views, followed by 950 million from the Philippines and 840 million from Indonesia. Additionally, it is noteworthy that many of these top-ranking countries are geographically proximate to Japan. This proximity suggests several factors potentially influencing this trend, such as logistical convenience and accessibility, possibly driven by factors like more affordable airfare options.
#### - For the numbers across continents, it's clear that Asia takes the lead with impressive 18 million issuances, while Europe follows behind with around 512 thousand. South America comes in next with 278 thousand, and Africa isn't far off with about 145 thousand. Bringing up the rear, we've got North America with around 40 thousand and Oceania with roughly 39 thousand.
#### - In this scenario of the top 10 Countries Japanese Marry Outside of Japan, China, the Philippines, and Brazil emerge as the top three contenders. Brazil's appearance in the top ranks is particularly noteworthy, as it has not been a frequent presence in the previous analyses of the top 10. This unexpected inclusion adds an element of surprise to the findings.
