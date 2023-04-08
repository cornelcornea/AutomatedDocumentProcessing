from tabula import read_pdf
from tabulate import tabulate
# PDF file to extract tables form 
file = "sample-invoice.pdf"

# extract all tables in the PDF file 
# reads table form pdf file 

df = read_pdf(file, pages="all") #address of pdf file 
print(tabulate(df[0]))
print(tabulate(df[1]))