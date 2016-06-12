import csv
import numpy

def load_and_print_csv(filename):
    raw_data = open(filename, 'rb') # rb represents 'read-only binary stream'
    reader = csv.reader(raw_data, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    x = list(reader)
    x.reverse() # The attributes are at the end of the list.
    attributes = x.pop() # Because python lists can only pop the front, list needed to be reversed.
    data = numpy.array(x) # numpy arrays are more efficent than regular python arrays
    print ''
    print '========================', filename, '========================'
    print 'attributes:', attributes
    print data
    print ''

def main():
    load_and_print_csv('student-mat-adjusted.csv') # the attributes from 'student-mat.csv' weren't quoted
    load_and_print_csv('student-por-adjusted.csv') # "     ...         " 'student-por.csv' "    ...     "

if __name__ == '__main__':
    main()
