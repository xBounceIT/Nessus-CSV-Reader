import csv
import matplotlib.pyplot as plt

def csvinput():
    while True:
        try:
            csvfile = input("Inserisci il path del file csv: ")
            with open(csvfile, newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                next(reader)
                dati = [(row[1], row[2]) for row in reader]
                size = len(dati)
                risklist = [0,0,0,0]
                for value in dati:
                    risk = value[0]
                    host = value[1]
                    :

                #low = int((low * 100) / size)
                #mid = int((mid * 100) / size)
                #high = int((high * 100) / size)
                #critical = int((critical * 100) / size)
                #results = [low, mid, high, critical]
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
