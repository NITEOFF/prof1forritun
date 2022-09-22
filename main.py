# 22.09.22 Artjom Pushkar

#Verkefni 1
# Verkefni spyr notandann hvað hann heitir og hæð hans i metrum. Síðan á forritið að skrifa út nafn og hversu marga sentimetra vantar i 2 metra
print("\n")
nafn = input("Hvað er nafnið þitt? = ")
haed = float(input("Hvað ert þú hár í metrum? = "))

if haed < 2: 
    haedid = (2 - haed) * 100 
    print ("Goðan daginn " + nafn , ", þig vantar - " , round(haedid, 1) , " sentimetra upp í að verða tveggja metra há(r).""\n") 

elif haed > 2: 
    print("Þú er orðinn hærri tveggja metra.""\n") 
    
else: 
    print("Villa""\n") 


#Verkefni 2
#Forrit tekur stigafjölda i körfubolta, og ut frá þvi hve morg stig þær notandinn kemur öðruvisi svar
stig = int(input("Hversu mörg stig? - "))

if stig > 0 or stig < 40:
    print("Úpps þetta hefur ekki endað vel.""\n")
    
elif stig > 40 or stig < 70:
    print("Þetta hefur gengið vel.""\n")
    
elif stig > 70 or stig < 100:
    print("Geggjað vel gert.""\n")

elif stig < 0 or stig > 100:
    print("Kjaftæði er þetta - þú þarft að vanda innsláttinn.""\n")


#Verkefni 3
#Forrit bíður um 3 tölur  siðar dregur út siðustu tölu
tala1 = int(input("Skrifaðu fyrstu tölu - "))
tala2 = int(input("Skrifaðu aðra tölu - "))
tala3 = int(input("Skrifaðu þriðju tölu - "))

tala4 = (tala1 * tala2) - tala3
print(f"({tala1} + {tala2} - {tala3} = {tala4})""\n")

#Verkefni 4
#Heiltöludeiling
kronur = int(input("Fjöldi króna = "))

sedl10000 = kronur//10000
kronur -= sedl10000 * 10000
print("10.000 Seðlar = " + str(sedl10000))

sedl1000 = kronur//1000
kronur -= sedl1000 * 1000
print("1.000 Seðlar = " + str(sedl1000))

sedl100 = kronur//100
kronur -= sedl100 * 100
print("100 Seðlar = " + str(sedl100))

kronr = kronur
print("Krónur = " + str(kronr))
