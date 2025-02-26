# Big Data Analysis with PySpark

## Overview
This project involves analyzing **NCEI Global Surface Summary of the Day** weather data using **PySpark** in **Jupyter Notebook**. The goal is to clean, transform, and derive insights from weather variables like temperature, precipitation, and wind speed.

## Technologies Used
- **Anaconda Python** (Jupyter Notebook environment)
- **Apache Spark** (Big Data Processing)
- **PySpark** (Spark's Python API)

---

## Setup Instructions
### 1. Install Anaconda & PySpark
1. Download and install **[Anaconda](https://www.anaconda.com/products/distribution)**.
2. Download **[Apache Spark](https://spark.apache.org/downloads)** (Pre-built for Hadoop 3.5.3 or later).
3. Install **PySpark**:
   ```sh
   pip install pyspark
   ```

### 2. Launch Jupyter Notebook
- Open **Anaconda Navigator** → Launch **Jupyter Notebook**.
- Navigate to the project folder and open **pyspark_analysis.ipynb**.

### 3. Load Weather Data
Download **2015-2024 weather data** for **Cincinnati & Florida** from [NCEI](https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-day) and place them in structured directories:
```
/data
  ├── 2015/
  │   ├── 72429793812.csv  (Cincinnati)
  │   ├── 99495199999.csv  (Florida)
  ├── 2016/
  ├── ...
  ├── 2024/
```

### 4. Run Data Analysis in PySpark
#### Load CSV Data
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Weather Analysis").getOrCreate()
data = spark.read.csv("2015/72429793812.csv", header=True, inferSchema=True)
data.show()
```

#### Find Hottest Day per Year
```python
from pyspark.sql.functions import col, max
data.groupBy("YEAR").agg(max("MAX").alias("HottestTemp")).show()
```

#### Find Coldest March Day
```python
data.filter(col("DATE").like("%-03-%")).orderBy("MIN").limit(1).show()
```

### 5. Save & Submit Results
Submit **two files** named after your email username:
1. **Results File** (e.g., `yourname_results.txt`)
2. **Spark Code Notebook** (e.g., `yourname_Spark.ipynb`)

---

## Conclusion
By following this guide, you will successfully **set up PySpark**, analyze weather data, and derive meaningful insights in **Jupyter Notebook**.

🚀 Happy Analyzing!

