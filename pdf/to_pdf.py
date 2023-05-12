import nbconvert.exporters.pdf as pdf
import sys

name = sys.argv[1] if len(sys.argv) == 2 else 'book.tex'
with open(name, 'r',  encoding="iso-8859-1") as f:
    filedata = f.read()
newdata = filedata.replace('\chapter{Preface}', '\chapter*{Preface}')

with open(name, 'w', encoding="iso-8859-1") as f:
    f.write(newdata)
p = pdf.PDFExporter()
p.run_latex(name)

