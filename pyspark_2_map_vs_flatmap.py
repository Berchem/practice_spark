from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('App')
sc = SparkContext(conf=conf)

# create a string of list and an RDD
lst = ['coffee pandas', 'happy pandas', 'happiest pandas party']
tokenize = sc.parallelize(lst)

# map transformation & action
rdd_map = tokenize.map(lambda ele: ele.split(' '))
print 'Map:\n', ', '.join(map(str, rdd_map.collect()))

# flat map transformation & action
rdd_flatmap = tokenize.flatMap(lambda ele: ele.split(' '))
print 'flatMap:\n', ', '.join(map(str, rdd_flatmap.collect()))
