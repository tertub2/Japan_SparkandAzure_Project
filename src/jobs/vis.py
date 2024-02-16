from pyspark.sql import SparkSession

spark = SparkSession.Builder.appName('End to end processing').getOrCreate()

df = spark.read.csv('input/visa_number_in_japan', header=True, inferSchema=True)

new_column_names= [col_name_replace(' ',"")