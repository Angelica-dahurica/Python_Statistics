print 'hello'
from scipy.stats import norm
from scipy.stats import chi2
import numpy as np
import csv
import urllib


csv_reader = csv.reader(urllib.urlopen('http://py.mooctest.net:8081/dataset/population/population_old.csv'))
for row in csv_reader:
	print row