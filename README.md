# Japan Spark and Azure Project: Azure Data Engineering Project 🎌

Project with end-to-end data processing and visualization of visa numbers in Japan using PySpark and Plotly. The tools used were spark clusters that were set up within a Docker container on Azure.

## 📚 Table of Contents

The table of contents aims to show the stages of the project along with some details and features present in the project

- [System Architecture](#-architecture)

- [Setup](#-setup)

- [Usage](#python)

- [Transformations](#-transformations)

- [System Architecture](#python)

- [System Architecture](#python)

## ⛓️ Architecture
![Project Architecture Scheme](https://github.com/tertub2/Japan_SparkandAzure_Project/blob/master/architecture.png)


## 🛠️ Setup
- Azure: Active account in azure (needed to create a VM)
- Docker: The Spark master-worker architecture has been deployed within a Docker container hosted on Azure.
- Python (Libraries): Pyspark, Fuzzywuzzy, Pycountry_convert, Pycountry and Plotly Express.
- Linux: VM with linux (Ubuntu) used.

📈 Transformations
System Architecture: The Spark master-worker architecture is set up in a Docker container on Azure.
Data Ingestion: The script ingests the CSV file containing the visa numbers in Japan.
Data Cleaning: The script standardizes column names, drops null columns, and corrects country names using fuzzy matching.
Data Transformation: The data is further enriched by adding continent information for each country.
Data Visualization: The cleaned and transformed data is visualized using Plotly Express to provide insights into visa trends in Japan.
[Output](https://github.com/tertub2/Japan_SparkandAzure_Project/tree/master/src/output)
