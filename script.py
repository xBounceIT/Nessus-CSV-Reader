import csv
import matplotlib.pyplot as plt

def csvinput():
    while True:
        try:
            csvfile = input("Inserisci il path del file csv: ")
            with open(csvfile, newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                risk = [(row[1]) for row in reader if row[1] != "Risk"]
                size = len(risk)
                low = 0
                mid = 0
                high = 0
                critical = 0
                for value in risk:
                    if value == "Medium":
                        mid += 1
                        continue
                    elif value == "Low":
                        low += 1
                        continue
                    elif value == "High":
                        high += 1
                    elif value == "Critical":
                        critical += 1
                        continue
                low = round((low * 100) / size, 2)
                mid = round((mid * 100) / size, 2)
                high = round((high * 100) / size, 2)
                critical = round((critical * 100) / size, 2)
                results = [low, mid, high, critical]
                return results
        except ValueError:
            print("File non trovato, reinserire: ")

def graph(values):
    labels = ["Low", "Medium", "High", "Critical"]
    plt.pie(values, labels)
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