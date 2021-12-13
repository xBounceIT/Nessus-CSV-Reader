import csv, datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pymsgbox

date = datetime.datetime.now()
date = date.strftime("%d-%m-%Y")

def csvinput():
    filepath = filedialog.askopenfilename(title="Carica file csv")
    with open(filepath, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")                                         # Legge il file in input utilizzando il punto e virgola con delimiter
        next(reader)                                                                        # Salta la prima riga corrispondente ai nomi valori
        dati = [(row[1], row[2]) for row in reader]                                         # Dal file in input immagazzina i valori di ogni riga colonna 1,2
        low, mid, high, critical = 0,0,0,0                                                  # Contatori per host
        lowtotal, midtotal, hightotal, criticaltotal = 0,0,0,0                              # Contatori totale
        hosts = []                                                                          # Lista hosts
        for value in dati:                                                                  # Per ogni riga
            risk = value[0]                                                                 
            hosts.append(value[1])                                                          # Prendi l'host e mettilo nella lista
            if risk == "Low":
                lowtotal += 1
                continue
            elif risk == "Medium":
                midtotal += 1
                continue
            elif risk == "High":
                hightotal += 1
                continue
            elif risk == "Critical":
                criticaltotal += 1
                continue
        hosts = dict.fromkeys(hosts)                                                        # Per evitare doppi, crea un dizionario
        for host in hosts:                                                                  # Per ogni host    
            low = dati.count(("Low", host))                                                 # Conta le low
            mid = dati.count(("Medium", host))                                              # Conta le medium
            high = dati.count(("High", host))                                               # Conta le high
            critical = dati.count(("Critical", host))                                       # Conta le critical
            low = round(((low * 100) / lowtotal), 2)                                               # Determina la percentuale in basse a tutte le low
            mid = round(((mid * 100) / midtotal), 2)                                               # Determina la percentuale in basse a tutte le medium
            high = round(((high * 100) / hightotal), 2)                                            # Determina la percentuale in basse a tutte le high
            critical = round(((critical * 100) / criticaltotal), 2)                                # Determina la percentuale in basse a tutte le critical
            with open(f"Report_Severity_{date}.txt", "a") as result:
                result.write("\n-----------------------------------------------------------------\n")
                result.write("|                         ")
                result.write(str(host))
                result.write("                          |")
                result.write("\n-----------------------------------------------------------------\n")
                result.write("Low: ")
                result.write(str(low))
                result.write("%")
                result.write(" | Medium: ")
                result.write(str(mid))
                result.write("%")
                result.write(" | High: ")
                result.write(str(high))
                result.write("%")
                result.write(" | Critical: ")
                result.write(str(critical))
                result.write("%")
                result.write("\n-----------------------------------------------------------------\n")
        result.close()
        total = [lowtotal, midtotal, hightotal, criticaltotal]
        return total

def graph(values):
    labels = ["Low", "Medium", "High", "Critical"]
    plt.pie(values, labels=labels)
    plt.title(date)
    plt.legend(bbox_to_anchor=(1.05,1.0), loc="upper left")
    plt.savefig(f"Grafico_Severity_{date}")
    return 0

def main():
    values = csvinput()
    graph(values)
    pymsgbox.alert('Report e grafici creati correttamente', 'Esecuzione corretta')
    return 0

if __name__ == "__main__":
  try:
    main()
  except:
    pymsgbox.alert("Errore, termino", "Crash")
    exit
