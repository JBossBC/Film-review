import findspark
import pyspark
from pyspark.streaming import StreamingContext

findspark.init()
conf = pyspark.SparkConf()
conf.setAppName("streaming")
conf.setMaster("local[2]")
SparkSession = pyspark.sql.SparkSession.builder.appName("movieRate").master("local[2]").getOrCreate()
SparkStreaming = StreamingContext(SparkSession.sparkContext, 5)

def GetSparkSession():
    return SparkSession


def GetSparkStreaming():
    return SparkStreaming
