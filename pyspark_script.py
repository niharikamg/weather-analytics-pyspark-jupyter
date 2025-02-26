from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max, avg, stddev, expr

spark = SparkSession.builder.appName("Weather Analysis").getOrCreate()

# Load CSV Data
data = spark.read.csv("2015/72429793812.csv", header=True, inferSchema=True)

# Count Rows
print("Row Count:", data.count())

# Find Hottest Day Per Year
hottest_days = data.groupBy("YEAR").agg(max("MAX").alias("HottestTemp"))
hottest_days.show()

# Find Coldest March Day
coldest_march = data.filter(col("DATE").like("%-03-%")).orderBy("MIN").limit(1)
coldest_march.show()

# Find Year with Most Precipitation
precipitation = data.groupBy("YEAR").agg({"PRCP": "avg"}).orderBy("avg(PRCP)", ascending=False)
precipitation.show()
