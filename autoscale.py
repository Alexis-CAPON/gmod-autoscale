with open("your_file.txt", "r") as fichier1, open("your_output_file.txt", "w") as fichier2:
    for ligne in fichier1:
        if ":SetSize" in ligne:
            start = ligne.find(":SetSize")
            valeurs = ligne[start+9:-2]
            virgule = valeurs.find(",")
            leftvalue = valeurs[0:virgule]
            rightvalue = valeurs[virgule+1:]
            
            #CALCUL
            leftvalue = float(leftvalue) / 1920
            rightvalue = float(rightvalue) / 1080
            
            fichier2.write(ligne[:start]+ ":SetSize(" + str(leftvalue) + "*width," + str(rightvalue) + "*height)\n")
        
        elif ":AlignLeft" in ligne:
            start = ligne.find(":AlignLeft")
            valeurs = ligne[start+11:-2]

            
            #CALCUL
            if valeurs.isnumeric():
                value = float(valeurs) / 1920
            
                fichier2.write(ligne[:start]+ ":AlignLeft(" + str(value) + "*width)\n")
            else:
                fichier2.write(ligne)
        elif ":AlignRight" in ligne:
            start = ligne.find(":AlignRight")
            valeurs = ligne[start+12:-2]

            
            #CALCUL
            value = float(valeurs) / 1920
            
            fichier2.write(ligne[:start]+ ":AlignRight(" + str(value) + "*width)\n")
            
        
        elif ":AlignBottom" in ligne:
            start = ligne.find(":AlignBottom")
            valeurs = ligne[start+13:-2]

            
            #CALCUL
            if valeurs.isnumeric():
                value = float(valeurs) / 1080
            
                fichier2.write(ligne[:start]+ ":AlignBottom(" + str(value) + "*height)\n")
            else:
                fichier2.write(ligne)    
        
        elif ":AlignTop" in ligne:
            start = ligne.find(":AlignTop")
            valeurs = ligne[start+10:-2]

            
            #CALCUL
            if valeurs.isnumeric():
                value = float(valeurs) / 1080
            
                fichier2.write(ligne[:start]+ ":AlignTop(" + str(value) + "*height)\n")
            else:
                fichier2.write(ligne)    
        
        else:
            fichier2.write(ligne)