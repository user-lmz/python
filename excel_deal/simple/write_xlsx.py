import time

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
sheet["C1"] = time.strftime("%x")

workbook.save(filename="hello_world.xlsx")
