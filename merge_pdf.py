import PyPDF2
import sys

inputs = sys.argv[1:]

# python main.py python.pdf python2.pdf tilt.pdf
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('pdf_merge.pdf')


pdf_combiner(inputs)
