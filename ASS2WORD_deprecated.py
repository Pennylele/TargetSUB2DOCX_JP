import sys, os, re, io
from docx import Document

document = Document()

cwd = os.getcwd()

for file in os.listdir(cwd):
    if file.endswith('.ass'):
        #print (file)
        files = file
        if sys.argv[1] in files:
            #print sys.argv[1]
            f = io.open(sys.argv[1], encoding='utf-8', mode='r+')
            #print(f)
            regex = re.compile('(?<=,0,0,0,,)[^\s].*')
            subtitles = regex.findall(f.read())
            #print (subtitles)
            for subtitle in subtitles:
                subtitle = subtitle.replace('\\N', '')
                document.add_paragraph(subtitle)

    document.save(sys.argv[1]+ '.docx')
