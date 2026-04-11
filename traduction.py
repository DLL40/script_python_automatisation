from deep_translator import GoogleTranslator

def traduire_texte(texte,source='auto',cible=''):
    try:
        traducteur=GoogleTranslator(source=source, target=cible)
        resultat_traduction=traducteur.translate(texte)
        return resultat_traduction
    except Exception as e:
        return f"Une erreur est survenue lors de la traduction : {e}"

# Application

texte_a_traduire=input("Entrez le texte à traduire : ")
print("\n" + "-"*120)
print("Veuillez renseigner le code langue : en = anglais, fr = français, es = espagnol, de = allemand, it = italien, ...")
print("-"*120 + "\n")
select_langue=input("Traduire en : ") 

traduction=traduire_texte(texte_a_traduire,cible=select_langue)

print("\n" + "-"*120)
print(f"Texte à traduire : {texte_a_traduire}")
print(f"Traduction : {traduction}")
print("-"*120)
