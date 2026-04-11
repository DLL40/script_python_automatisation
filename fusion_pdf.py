import PyPDF2

def fusionner_pdfs(liste_fichiers, nom_sortie):

    fusionneur = PyPDF2.PdfMerger()

    try: 
        for pdf in liste_fichiers :
            print(f"Ajout de : {pdf}")
            fusionneur.append(pdf)

        fusionneur.write(nom_sortie)
        fusionneur.close()
        print(f"\nFusion réussie ! Le fichier {nom_sortie} a bien été créé")

    except Exception as e :
       print(f"Echec de la fusion des documents : {e}")

# Application

"""
-Créer un dossier dédié (ex: Fusion_PDF) contenant ce script ainsi que les fichiers.pdf à fusionner
-Nommer les documents à fusionner "document1.pdf" pour le premier et "document2.pdf" pour le second, ...
-Le fichier pdf fusionner sera nommer "document_final.pdf"
"""

fichier_a_fusionner = ["document1.pdf", "document2.pdf"]
fusionner_pdfs(fichier_a_fusionner, "document_final.pdf")




