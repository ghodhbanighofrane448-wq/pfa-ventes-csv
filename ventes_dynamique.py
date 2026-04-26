import matplotlib.pyplot as plt 
import pandas as pd

#implementer la lecture dynamique de fichier csv
nom_fichier=input("taper le nom du fichier csv ")
df=pd.read_csv(nom_fichier)
print("Fichier chargé avec succès")


#question2:nouvelle colonne CA_brut
df['CA_Brut'] = df['Prix'] * df['Quantite']

#question3:nouvelle colonne CA_net
df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)

#pour voir les colonnes ajoutées 
print(df)

#question4 :TVA=CAnet*20/100
df['TVA'] = df['CA_Net'] * 0.20

#verification 
print(df)

#question 5 :le CA total  
total = df['CA_Net'].sum() 

print("le chiffre d'affaire total de l'entreprise ", total)

#question 6:ID
id_max_benefice = df['ID'][df['CA_Net'].idxmax()]

print("le id avec le plus gros benefice ", id_max_benefice)

#question 7:export
df.to_csv("resultats_final.csv", index=False)

# Bonus : graphique CA Net par produit
plt.bar(df['ID'], df['CA_Net'])  

plt.xlabel("ID du produit")       
plt.ylabel("CA Net")              
plt.title("CA Net par produit")   

plt.show()
