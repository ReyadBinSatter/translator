import json
from googletrans import Translator
from fpdf import FPDF


#read json file
jsonfile = open('json_file.json','r')
jsondata = jsonfile.read()

#parse data
obj = json.loads(jsondata)

list = obj['languages']


# #create pdf
pdf = FPDF()

# #add page
pdf.add_page()

translator = Translator()
new_text = str(obj['text'])
for x in list:
    print(x)

    x = str(x)

    #translate
    
    translate = translator.translate(new_text,src='en',dest=x).text
    print(translate)
    # font & text in pdf
    #pdf.add_font(uni=True)
    pdf.set_font('helvetica',size =16)
    pdf.cell(120,20,txt = x , ln=True)
    pdf.set_font('helvetica',size =10)
    pdf.cell(120,10,txt = translate, ln=True)

pdf.output('output.pdf')
