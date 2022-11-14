from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import row_number, desc, col
import pyspark.sql.functions as F
from pyspark.sql.window import Window

def read_data_to_df():
    db_properties = {}
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

    sc = SparkContext.getOrCreate()
    sqlContext = SQLContext(sc)

    df_read = sqlContext.read.format("jdbc")\
        .option("url", db_properties['url'])\
        .option("dbtable", db_properties['table'])\
        .option("user", db_properties['username'])\
        .option("password", db_properties['password'])\
        .option("Driver", db_properties['driver'])\
        .load()

    # df_read.show(1, vertical=True)
    return df_read

def x_clubs_with_highest_players_ending_in_2023(df, x):
  print(
      f'What are the {x} clubs that have the highest number of players with contracts ending in 2023?')
  df.where((df.year == 2022) & (df.club_contract_valid_until == 2023)).groupBy(
      'club_name').count().orderBy('count', ascending=False).show(x)

def y_clubs_with_highest_average_players_older_27(df, y):
  print(
      f'List the {y} clubs with highest average number of players that are older than 27 years across all years')
  df.where((df.age > 27) & (df.club_name != 'null')).groupBy(
      'club_name').count().withColumn('average', col('count') / 8).orderBy('average', ascending=False).show(y)

def most_frequent_nation_position_each_year(df):
  print('What is the most frequent position for each nation in each year?')
  grouped = df.where(df.nation_position != 'null').groupby(
      'nation_position', 'year').count()
  window = Window.partitionBy("year").orderBy(desc("count"))
  grouped.withColumn('rank', row_number().over(window)
                     ).where(col('rank') == 1).show()

def analyze_data(x, y):
    df = read_data_to_df()
    x_clubs_with_highest_players_ending_in_2023(df, x)
    y_clubs_with_highest_average_players_older_27(df, y)
    most_frequent_nation_position_each_year(df)

print("What are the X clubs that have the highest number of players with contracts ending in 2023?")
x = int(input("Enter X value:")) or 1
print("List the Y clubs with highest average number of players that are older than 27 years across all years")
y = int(input("Enter Y value:")) or 1
analyze_data(x, y)