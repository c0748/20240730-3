import openpyxl
wb = openpyxl.Workbook()

ws = wb.active

cell = ws["A1"]

cell.value = "A1"

print(f"A１セルの値は{cell.value}です")

