import csv
import matplotlib.pyplot as plt

def csvinput():
    while True:
        try:
            csvfile = input("Inserisci il path del file csv: ")
            with open(csvfile, newline="") as csvfile:
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
                    low = int((low * 100) / lowtotal)                                               # Determina la percentuale in basse a tutte le low
                    mid = int((mid * 100) / midtotal)                                               # Determina la percentuale in basse a tutte le medium
                    high = int((high * 100) / hightotal)                                            # Determina la percentuale in basse a tutte le high
                    critical = int((critical * 100) / criticaltotal)                                # Determina la percentuale in basse a tutte le critical
                    print(host, "Low:", low, "Medium", mid, "High", high, "Critical", critical)              
                results = [low, mid, high, critical]
                return results
        except ValueError:
            print("File non trovato, reinserire: ")

def graph(values):
    labels = ["Low", "Medium", "High", "Critical"]
    plt.pie(values, labels=labels)
    plt.title("Rapporto severity rilevate")
    plt.legend(bbox_to_anchor=(1.05,1.0), loc="upper left")
    plt.savefig("torta.png")
    return 0

def main():
    values = csvinput()
    graph(values)
    return 0

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit(f"\nScript interrotto dall'utente")
