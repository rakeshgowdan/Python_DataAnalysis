import csv
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

#CSV is a simple file format used to store tabular data, such as a spreadsheet or database
#Comma-separated Values
