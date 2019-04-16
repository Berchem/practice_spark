from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('App')
sc = SparkContext(conf=conf)

# create a string of list
lst = ['coffee pandas', 'happy pandas', 'happiest pandas party']

# create an RDD
tokenize = sc.parallelize(lst)

# filter transformation
find_hap = tokenize.filter(lambda ele: 'hap' in ele)

# action
print ', '.join(map(str, find_hap.collect()))
