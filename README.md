# book-recommender-(This is a WIP)

<div align="center">
<img src=https://raw.githubusercontent.com/GrejSegura/book-recommender/master/img/books.jpg>
</div>

data was taken from http://www2.informatik.uni-freiburg.de/~cziegler/BX/  
data download link - http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip


NOTE:
After saving the data in 1_data_prep.ipynb, save the csv files to the hive table. From there the pre-processing proceeds using pyspark.
1. save the data first in a hdfs folder , i.e, /tmp/data/clean_ratings.csv:  
    `hdfs dfs -mkdir /tmp/data/`  
    `hdfs dfs -put /local-file-location-of-clean-ratings.csv/ /tmp/data/`  
2. create the table in hive:  
    `CREATE EXTERNAL TABLE IF NOT EXISTS testdb.ratings`  
    `(id INT, ISBN STRING, rating INT)`  
    `ROW FORMAT DELIMITED`  
    `FIELDS TERMINATED BY ','`  
    `STORED AS TEXTFILE`  
    `LOCATION 'hdfs://hadoop.host:8020/tmp/data/';`
