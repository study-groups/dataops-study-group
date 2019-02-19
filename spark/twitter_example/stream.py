from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row,SQLContext, SparkSession
import sys
import requests
import json

TCP_REMOTE_HOST = "data_server" #or whatever you named the docker container of the server
TCP_PORT = 9009 #must also be specified in the server file

# create spark configuration
conf = SparkConf()
conf.setAppName("TwitterStreamApp")

# create spark context with the above configuration
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# create the Streaming Context from the above spark context with interval
#size 2 seconds
ssc = StreamingContext(sc, 2)

# setting a checkpoint to allow RDD recovery
ssc.checkpoint("cps")

# read data from port 9009
dataStream = ssc.socketTextStream(TCP_REMOTE_HOST, TCP_PORT)


def getSparkSessionInstance(sparkConf):
    if ("sparkSessionSingletonInstance" not in globals()):
        globals()["sparkSessionSingletonInstance"] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()["sparkSessionSingletonInstance"]

def showrdd(time, rdd):
    try:
        # Get spark sql singleton context from the current context
        spark = getSparkSessionInstance(rdd.context.getConf())
        print("creating row rdd")
        row_rdd = rdd.map(lambda w: Row(frst=w))
        #create df
        print("creating df")
        df = spark.createDataFrame(row_rdd)
        print("Showing df")
        df.show(2, truncate=False)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f"Error: {e}")


# split each tweet into words
twts = dataStream.foreachRDD(showrdd)

# start the streaming computation
ssc.start()

# wait for the streaming to finish
ssc.awaitTermination()
