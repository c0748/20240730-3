import openpyxl
wb = openpyxl.Workbook()

ws = wb.active

cell = ws["A1"]
print(cell)
