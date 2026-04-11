from pdf2docx import Converter 

def convert_pdf_en_word(document_pdf,document_word):
    try:
        convertisseur=Converter(document_pdf)
        convertisseur.convert(document_word,start=0,end=None)
        convertisseur.close()
        print(f"Convertion réussie ! Le fichier {document_word} a bien été enregistré")
    
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Utilisation

doc_pdf="document_pdf.pdf"
doc_word="document_word.docx"

convert_pdf_en_word(doc_pdf,doc_word)

