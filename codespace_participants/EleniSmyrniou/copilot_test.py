import csv

# new function that reads the data from the csv file
def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

if __name__ == '__main__':
    # read the data from the csv file
    data = read_data('codespace_participants/EleniSmyrniou/data.csv')
    # print the data
    print(data)