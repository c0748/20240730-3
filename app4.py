import openpyxl



# 新規のファイルを作成

wb = openpyxl.Workbook()

ws = wb.active

cell = ws["A1"]
cell.value = "A1"

print(f"セルA１の値は{cell.value}です")

wb.save("files/new_wb3.xlsx")