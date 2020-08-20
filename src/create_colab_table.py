'''
The clean_ratings.csv data should be saved to the hive table first before running this
'''

from pyspark.sql import HiveContext
from pyspark.sql import SparkSession, SQLContext

spark = SparkSession.builder \
    .master("yarn") \
    .appName("book-recommender") \
    .config("hive.metastore.warehouse.dir", "/warehouse/tablespace/managed/hive") \
    .config("hive.metastore.warehouse.external.dir", "/warehouse/tablespace/external/hive") \
    .config("spark.sql.pivotMaxValues", "300000") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql('use testdb') # this is the database where the data was saved in hive
ratings = spark.sql('select * from ratings')
ratings = ratings.filter(ratings['isbn']!='ISBN')
ratings = ratings.groupBy("isbn").pivot("id").sum("rating")
ratings.write.format("orc").mode("overwrite").saveAsTable("testdb.ratings_colab")
ratings.show()
