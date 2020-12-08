#!/usr/bin/env python

import openpyxl

book = openpyxl.load_workbook('sheets.xlsx')

print(book.sheetnames)

active_sheet = book.active
print(type(active_sheet))

sheet = book["March"]
print(sheet.title)