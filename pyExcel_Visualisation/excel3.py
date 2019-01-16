import xlsxwriter

workbook = xlsxwriter.Workbook('book3.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A8', 'Test data')

workbook.close()
