#Writing to a XLS file using pyexcel
from pyexcel_xls import save_data
data= {"sheet 1":[[1,2,3],[4,5,6]] }
save_data("book1.xls",data)
