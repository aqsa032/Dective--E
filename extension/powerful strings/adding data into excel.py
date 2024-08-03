

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
data = (
("Product","cost","selling price"),
("laptop","$60","&70"),
("watch","$10","&711"),
)
for i in data:
    ws.append(i)
wb.save("output.xlsx")
