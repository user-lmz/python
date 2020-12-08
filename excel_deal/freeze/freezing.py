#!/usr/bin/env python

from openpyxl import Workbook
from openpyxl.styles import Alignment

book = Workbook()
sheet = book.active

sheet.freeze_panes = 'C3'

book.save('freezing.xlsx')