from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import lit
import os

from pyspark import SparkContext

file_list = [f'data/{f}' for f in os.listdir('data')]
print(file_list)
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("GenericAppName") \
    .getOrCreate()
df = spark.read.csv(file_list[0], header=True, inferSchema=True)
year = int('20' + file_list[0].split('_')[-1].split('.')[0])
df = df.withColumn('year', lit(year))
for file_path in file_list[1:]:
    cur_df = spark.read.csv(file_path, header=True, inferSchema=True)
    year = int('20' + file_path.split('_')[-1].split('.')[0])
    cur_df = cur_df.withColumn('year', lit(year))
    df = df.unionByName(cur_df)

db_properties = {}
# update your db username
# "postgres" by default
username = input('Enter your username:') or 'postgres'
db_properties['username'] = username
# update your db password
password = input('Enter your password:')
if password == None:
    raise ValueError('please put your password')
db_properties['password'] = password
# make sure you got the right port number here
db_properties['url'] = "jdbc:postgresql://localhost:5432/postgres"
# make sure you had the Postgres JAR file in the right location
db_properties['driver'] = "org.postgresql.Driver"
db_properties['table'] = "fifa"

df.write.format("jdbc")\
    .mode("overwrite")\
    .option("url", db_properties['url'])\
    .option("dbtable", db_properties['table'])\
    .option("user", db_properties['username'])\
    .option("password", db_properties['password'])\
    .option("Driver", db_properties['driver'])\
    .save()

# sc = SparkContext.getOrCreate()
# sqlContext = SQLContext(sc)

# df_read = sqlContext.read.format("jdbc")\
#     .option("url", db_properties['url'])\
#     .option("dbtable", db_properties['table'])\
#     .option("user", db_properties['username'])\
#     .option("password", db_properties['password'])\
#     .option("Driver", db_properties['driver'])\
#     .load()

# df_read.show(1, vertical=True)
