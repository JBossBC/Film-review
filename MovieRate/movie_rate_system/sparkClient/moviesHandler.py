

"""init the movie file """
import json

import movie_rate_system.sparkClient.sparkApplication as sparkUtil

movieFile = "movie_rate_system/resource/movies.csv"
# movieFile = "../resource/movies.csv"
ratingsFile = "movie_rate_system/resource/ratings.csv"
# ratingsFile = "../resource/ratings.csv"
"""movieTableSchema"""
movieTableName = {"movieId", "title", "genres"}
tagsFile =  "movie_rate_system/resource/tags.csv"
movieDF = sparkUtil.GetSparkSession().read.csv(movieFile, header=True)
ratingsDF = sparkUtil.GetSparkSession().read.csv(ratingsFile, header=True)
tagsFile = sparkUtil.GetSparkSession().read.csv(tagsFile, header=True)
# movieRateStream = sparkUtil.SparkStreaming.textFileStream(movieFile)
def consumerData(line):
    if not line.isEmpty():
        print(line.collect())



def initSockerStreaming():
    socketStream = sparkUtil.SparkStreaming.socketTextStream("localhost", 8888)

def handlerMovieFile():
    global movieDF
    movieDF = sparkUtil.GetSparkSession().read.csv(movieFile, header=True)


# find add movies
def queryMovies():
    return movieDF.limit(10).toJSON().collect()


# query movies by title ,support  fuzzy query
def queryMoviesByTitle(params: str):
    return movieDF.filter(movieDF.title.like('{}%'.format(params))).toJSON().collect()


def getMovieTags(params: str):
    return tagsFile.filter(tagsFile.movieId == params).limit(10).toJSON().collect()


"""query movies by geners """


def queryMoviesByGenres(params: str):
    return movieDF.filter(movieDF.genres.contains(params)).collect()


def realTimeDiscussStreaming():
    fileStream = sparkUtil.SparkStreaming.textFileStream(movieFile)
    fileStream.flatMap(lambda x: x.split(",")).pprint()


"""need the movieId"""
def averageRate(params: str):
    valueList = ratingsDF.filter(ratingsDF.movieId == params).select(ratingsDF.rating).collect()
    sum = 0
    for temp in valueList:
        tempDict = temp.asDict(True)
        sum += float(tempDict["rating"])
    return round(sum/len(valueList),1)
