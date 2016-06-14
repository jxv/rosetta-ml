import pandas
import csv
import numpy
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression

def parse_date(s):
    month, day, year = s.split('/')
    return float(month) * 30 + float(day)

def parse_time(s):
    hours, minutes, seconds = s.split('.')
    return float(hours) * 60 ** 2 + float(minutes) * 60 + float(seconds)

def parse_decimal_comma(s):
    vals = s.split(',');
    if len(vals) == 1:
        return float(vals[0])
    if len(vals) == 2:
        return float(vals[0]) + float(vals[1]) / (10. * len(vals[1]))

def main():
    # https://archive.ics.uci.edu/ml/datasets/Air+Quality
    types = {
        'PT08.S1(CO)': numpy.float32,
        'NMHC(GT)': numpy.float32,
        'PT08.S2(NMHC)': numpy.float32,
        'NOx(GT)': numpy.float32,
        'PT08.S3(NOx)': numpy.float32,
        'NO2(GT)': numpy.float32,
        'PT08.S4(NO2)': numpy.float32,
        'PT08.S5(O3)': numpy.float32,
    }
    converters = {
        'Date': parse_date,
        'Time': parse_time, 
        'CO(GT)': parse_decimal_comma, 
        'NMHC(GT)': parse_decimal_comma,
        'C6H6(GT)': parse_decimal_comma,
        'T': parse_decimal_comma,
        'RH': parse_decimal_comma,
        'AH': parse_decimal_comma,
    }
    dataframe = pandas.read_csv('AirQualityUCI.csv', delimiter=';', quoting=csv.QUOTE_NONE, dtype=types, converters=converters)
   
    # The two right most columns are unused
    array = dataframe.values[:,0:15]
    X = array[:,0:14]
    Y = array[:,14]

    num_folds = 10
    num_instances = len(X)
    seed = 7
    kfold = cross_validation.KFold(n=num_instances, n_folds=num_folds, random_state=seed)
    model = LinearRegression()
    scoring = 'mean_squared_error'
    results = cross_validation.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    print results.mean()

if __name__ == '__main__':
    main()
