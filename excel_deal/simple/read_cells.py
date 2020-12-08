import openpyxl

book = openpyxl.load_workbook('hello_world.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['B1']
a3 = sheet.cell(row=1, column=3)

print(a1.value)
print(a2.value)
print(a3.value)