import PyPDF2

# Use rb instead of r because you need to read in binary
with open('python.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
