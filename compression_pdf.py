from PyPDF2 import PdfReader, PdfWriter

def compresseur_pdf(document_initial, document_final) :
    reader = PdfReader(document_initial)
    writer = PdfWriter()

    for page in reader.pages :
        writer.add_page(page)

    for page in writer.pages : 
        page.compress_content_streams()

    with open(document_final, "wb") as f :
        writer.write(f)

    print(f"Le fichier compressé {document_final} a bien été sauvegardé")

# Application
"""
-Créer un dossier dédié (ex: Compression_PDF) contenant ce script ainsi que le fichier.pdf à compresser
-Nommer le document à compresser "document_a_compresser.pdf" 
-Le fichier pdf compressé sera nommer "document_reduit.pdf"
"""

compresseur_pdf("document_a_compresser.pdf", "document_reduit.pdf")
