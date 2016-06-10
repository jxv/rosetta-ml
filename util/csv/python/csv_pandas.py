import pandas

def describe_csv(filename):
  data = pandas.read_csv(filename) # Creates a pandas.DataFrame
  print '====================', filename, '========================'
  # somehow dataframe auto splits the category names and rows of data
  print data.describe() # properties of this data frame


def main():
  describe_csv('student-mat-adjusted.csv')
  describe_csv('student-por-adjusted.csv')

if __name__ == '__main__':
  main()
