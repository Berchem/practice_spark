from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('App')
sc = SparkContext(conf=conf)
