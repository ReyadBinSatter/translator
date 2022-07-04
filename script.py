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
    print(new_text)
    # #translate
    
    translate = translator.translate(new_text,src='en',dest='ja')
    print(translate.text)
    # font & text in pdf
    pdf.set_font('Arial',size =16)
    pdf.cell(120,20,txt = x , ln=True)
    pdf.set_font('Arial',size =10)
    pdf.cell(120,10,txt = obj['text'], ln=True)

pdf.output('output.pdf')
