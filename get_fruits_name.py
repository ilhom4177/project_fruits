import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    fruits = []
    for row in fruits:
        fruits.append(row['name'])
    return fruits
f = open('fruits.csv','r')
x = f.read()
print(get_frutis_name('x'))
    