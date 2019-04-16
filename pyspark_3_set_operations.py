from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('App')
sc = SparkContext(conf=conf)

# create two RDD
rdd1 = sc.parallelize(['coffee', 'pandas', 'happy', 'happiest', 'party'])
rdd2 = sc.parallelize(['coffee', 'pandas', 'kitty'])

# rdd.distinct()
rdd_distinct = rdd1.distinct()
print 'Distinct:\n', ', '.join(map(str, rdd_distinct.collect()))

# rdd.union()
rdd_union = rdd1.union(rdd2)
print 'Union:\n', ', '.join(map(str, rdd_union.collect()))

# rdd.intersection()
rdd_intersection = rdd1.intersection(rdd2)
print 'Intersection:\n', ', '.join(map(str, rdd_intersection.collect()))

# rdd.subtract()
rdd_subtract = rdd1.subtract(rdd2)
print 'Subtract:\n', ', '.join(map(str, rdd_subtract.collect()))

# rdd.cartesian()
rdd_cartesian = rdd1.cartesian(rdd2)
print 'Cartesian:\n', ', '.join(map(str, rdd_cartesian.collect()))
