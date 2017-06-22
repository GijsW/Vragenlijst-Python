#utf8 implementeren, zodat we trema's kunnen gebruiken.
# -*- coding: utf-8 -*-
#Tijd functie implementeren, zodat we een sleep kunnen toevoegen.
import time
import datetime

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

#Bestand openen met de huidige tijd zodat we hier in weg kunnen schrijven
f = open(filename + ".txt","w")

#man = "test"

#Introductie
print("Beste student. Wij zijn Joost, Yaël, Floor en Selia en wij volgen de opleiding toegepaste psychologie aan het Saxion.")
print("")
time.sleep(1)
print("Voor het vak STEM (science, technology, engineering and mathmatics) willen wij onderzoek doen naar de samenwerking van eerstejaars toegepaste psychologie studenten, omdat er slechte ervaringen mee waren bij de leerlingen uit leerjaar 2016-2017.")
time.sleep(1)
print("Het doel van deze vragenlijst is om te zien hoe jullie de samenwerking in het eerste jaar van toegepaste psychologie hebben ervaren en, wanneer nodig, hier mogelijk met oplossingen voor te komen. Hierbij vragen wij om jullie hulp door deze vragenlijst in te vullen.")
time.sleep(1)
print("Je gaat nu een vragenlijst invullen over samenwerken, zoals je dit hebt ervaren in je eerste jaar als toegepaste psychologie student. De thema’s die aan bod komen zijn autonomie, tijdsdruk en hiërarchie. Je kunt telkens maar één antwoord kiezen.")
time.sleep(1)
print("Alle gegevens worden anoniem verwerkt. Heb je nog vragen n.a.v. deze vragenlijst of het onderzoek? Contact opnemen kan door ons te mailen: samenwerken@hotmail.com.")
print("")
time.sleep(1)
print("Wij danken jullie bij voorbaat voor jullie deelname.")
print("")
time.sleep(2)

#Algemene vragen
f.write("Algemene vragen" + "\n")
leeftijd = str(input("Wat is je leeftijd? (15 t/m 24): "))
f.write(leeftijd + "\n")
geslacht = str(input("Wat is je geslacht? (Man/vrouw): "))
f.write(geslacht + "\n")
provincie = str(input("In welke provincie woon je?: "))
f.write(provincie + "\n")
studie = str(input("Wat studeerde je voor je aan TP begon?: "))
f.write(studie + "\n")

print("")
print("")
print("")
print("Nu volgen de vragen over tijdsdruk.")
time.sleep(1)
tijdsdruk = str(input("Heb je weleens samengewerkt met én zonder tijdsdruk? (Ja/Nee): "))

if tijdsdruk == "ja" or tijdsdruk == "Ja":
    print("")
    print("Vragenlijst A")
    time.sleep(1)
    a1 = str(input("Vind je het fijner om met of zonder tijdsdruk te werken?: "))	
    a2 = str(input("Presteer je beter met of zonder tijdsdruk?: "))
    a3 = str(input("In welk verband verliepen de samenwerkingen beter, met of zonder tijdsdruk?: "))
	
elif tijdsdruk == "nee" or tijdsdruk == "Nee":
    print("")
    print("Vragenlijst B")
    time.sleep(1)
    b1 = str(input("Heb je weleens met/zonder tijdsdruk samengewerkt?: "))
    b2 = str(input("Lijkt het je fijner met/zonder tijdsdruk te werken?: "))
    b3 = str(input("Verliep de samenwerking goed met/zonder tijdsdruk?: "))
    
#Als er een typfout wordt gemaakt, zal dit worden aangegeven en wordt het programma gesloten.
else:
    print("U heeft een verkeerd antwoord gegeven, start het programma opnieuw op.")
    time.sleep(5)
    raise SystemExit
	
if tijdsdruk == "ja" or tijdsdruk == "Ja":
	f.write("\n" + "Vragenlijst A" + "\n")
	f.write(a1 + "\n")
	f.write(a2 + "\n")
	f.write(a3 + "\n")
	
elif tijdsdruk == "nee" or tijdsdruk == "Nee":
	f.write("\n" + "Vragenlijst B" + "\n")
	f.write(b1 + "\n")
	f.write(b2 + "\n")
	f.write(b3 + "\n")
	

    
print("")
print("")
print("")
print("Nu volgen de vragen over autonomie.")
time.sleep(1)
autonomie = str(input("Hoe heb jij je eigen autonomie ervaren tijdens je laatste samenwerking? (Goed/slecht): "))

if autonomie == "goed" or autonomie == "Goed":
    print("")
    print("Vragenlijst C")
    time.sleep(1)
    c1 = str(input("Heb je het idee dat het werk wat je met je groep moest verrichten sneller verliep?: ")) 
    c2 = str(input("Heb je het idee dat je, je kennis voldoende hebt kunnen tonen?: ")) 
    c3  = str(input("Heb je het idee dat je, je kennis hebt verbreed?: ")) 
    c4 = str(input("Heb je het idee doordat je zelf een grote autonomie had dat je je mening beter uit durfde te spreken, en conflicten in de groep eerder aan ging?: ")) 
    c5 = str(input("Heb je het idee dat doordat jij minder afhankelijk was, taken eerder op je groepsgenoten af schoof?: ")) 
    
elif autonomie == "slecht" or autonomie == "Slecht":
    print("")
    print("Vragenlijst D")
    time.sleep(1)
    d1 = str(input("Heb je het idee dat het werk wat je met je groep moest verrichten trager verliep?: "))
    d2 = str(input("Heb je het idee dat je, je kennis onvoldoende hebt kunnen tonen?: "))
    d3 = str(input("Heb je het gevoel dat je, je kennis onvoldoende hebt kunnen verbreden?: "))
    d4 = str(input("Heb je het idee dat je door je geringe autonomie, conflicten eerder uit de weg ging?: "))
    d5 = str(input("Heb je het idee dat je doordat jij afhankelijk was van je groepsgenoten, taken eerder op je nam?: "))

#Als er een typfout wordt gemaakt, zal dit worden aangegeven en wordt het programma gesloten.
else:
    print("U heeft een verkeerd antwoord gegeven, start het programma opnieuw op.")
    time.sleep(5)
    raise SystemExit
	
if autonomie == "goed" or autonomie == "Goed":
	f.write("\n" + "Vragenlijst C" + "\n")
	f.write(c1 + "\n")
	f.write(c2 + "\n")
	f.write(c3 + "\n")
	f.write(c4 + "\n")
	f.write(c5 + "\n")
	
elif autonomie == "slecht" or autonomie == "Slecht":
	f.write("\n" + "Vragenlijst D" + "\n")
	f.write(d1 + "\n")
	f.write(d2 + "\n")
	f.write(d3 + "\n")
	f.write(d4 + "\n")
	f.write(d5 + "\n")
    
print("")
print("")
print("")
print("Nu volgen de vragen over hiërarchie.")
time.sleep(1)
hierarchie = str(input("Heb je weleens te maken gehad met hiërarchie tijdens een samenwerking?: "))

if hierarchie == "ja" or hierarchie == "Ja":
    print("")
    print("Vragenlijst E")
    time.sleep(1)
    e1 = str(input("Waar stond jij in de hiërarchie? (Hoog/midden/laag): "))
    e2 = str(input("Vond jij dit positief voor de samenwerking?: "))
    e3 = str(input("Heb je liever dat er sprake is van hiërarchie tijdens de samenwerking of dat iedereen gelijk is?: "))
    
elif hierarchie == "nee" or hierarchie == "Nee":
    print("")
    print("Vragenlijst F")
    time.sleep(1)
    f1 = str(input("Vond je het positief voor de samenwerking dat iedereen gelijk was?: "))
    f2 = str(input("Zou je een keer een samenwerking willen hebben waar sprake is van hiërarchie?: "))
    
#Als er een typfout wordt gemaakt, zal dit worden aangegeven en wordt het programma gesloten.
else:
    print("U heeft een verkeerd antwoord gegeven, start het programma opnieuw op.")
    time.sleep(5)
    raise SystemExit
	
if hierarchie == "ja" or hierarchie == "Ja":
	f.write("\n" + "Vragenlijst E" + "\n")
	f.write(e1 + "\n")
	f.write(e2 + "\n")
	f.write(e3 + "\n")
	
elif hierarchie == "nee" or hierarchie == "Nee":
	f.write("\n" + "Vragenlijst F" + "\n")
	f.write(f1 + "\n")
	f.write(f2 + "\n")

opmerkingen = str(input("Heeft u nog vragen en/of opmerkingen?: "))
f.write("\n" + "Opmerkingen " + "\n" + opmerkingen)

print("")
print("Hartelijk dank voor het invullen van de vragenlijst.")
time.sleep(1)
print("")
print("Het programma wordt vanzelf afgesloten.")
time.sleep(5)

f.close()