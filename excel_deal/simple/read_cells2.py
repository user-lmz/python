import openpyxl

book = openpyxl.load_workbook('appending.xlsx')

sheet = book.active
cells = sheet['A1': 'C6']

for c1, c2, c3 in cells:
    print("{0:8} {1:8} {2:8}".format(c1.value, c2.value, c3.value))