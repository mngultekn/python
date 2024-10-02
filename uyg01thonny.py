import pytube

link = input('Enter Youtube URl')
yt = pytube.Youtube(link)
yt.streams.first(). download()
print('Download' , link)

from fpdf import FPDF
pdf = PDF()
görseli pdfe dönüştürme
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
    pdf.output("yourfile.pdf", "F")