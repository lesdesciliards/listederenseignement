""" fiche de renseignement """

nom=input("Quele est votre nom ?")
prenom=input(" Quelle est votre prenom ?")
naissance=input(" entrer votre date de naissance ?")
print(" Quel est votre sex : M pour masculin et F pour feminin")
sex=""
while not sex=="M" or sex=="F":
    sex=input(" entrer votre sex")
    try:
         print("veuller recommencer")
    except:
        print("veuiller enter votre sex")
profession=input("Quelle est votre profession?")
pays_origine=input("Quelle est votre pays d'origine? ")
tel=input("Votre numero de telephone")
email=input("Votre email")
date=input("Entrer la date")
heure=input("Entrer l'heure")

print("\t> nom            : "+nom)
print("\t> prenom         : "+prenom)
print("\t> sex            : "+sex)
print("\t> profesion      : "+profession)
print("\t> pays d'origine : "+pays_origine)
print("\t> telephone      : "+tel)
print("\t> email          : "+email)
print("\t> date et heure  : "+date +" à "+heure)
print("")
print("")

print("                     fait à lomé le "+date)


