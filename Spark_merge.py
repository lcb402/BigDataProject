from __future__ import print_function
import sys
from pyspark import SparkContext   
  
def sort_list(a_list):
    """
    Sorts a_list of values and returns it
    """
    a_list.sort()
    return a_list
        
def toCSVLine(data):
    """
    Joins elements of the data with commas
    """
    return ','.join(str(d) for d in data)
        
   
#Read data files
weather = ("weather.txt")
collisions = ("collisions_2015.txt")

#Create SparkContext 
sc = SparkContext("local", appName="Collisions_weather")
   
#Create RDD objects   
collisions_data = sc.textFile(collisions).cache()
weather_data = sc.textFile(weather).cache()

#Take a Cartesian product of two tables
#Filter out rows where the date of collision doesn't equal the date of the weather record
#Filter out rows where the collision happened before the weather record 
#Group data by the time of collision (where keys: time of collision, values: weather records)
#Sort weather records for each group 
#For each group select the most recent weather record, drop the rest
data = collisions_data.cartesian(weather_data) \
.filter(lambda x: x[0][:10] == x[1][:10]) \
.filter(lambda x: x[0][:19] >= x[1][:19]) \
.groupByKey().mapValues(list) \
.map(lambda x: (x[0], sort_list(x[1])[-1]))
    
#Combine lines is csv format 
lines = data.map(toCSVLine)

#Save result as csv file
lines.saveAsTextFile('result.csv')
   
#Stop Spark
sc.stop()
