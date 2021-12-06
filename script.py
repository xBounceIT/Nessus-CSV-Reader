import csv

def main():
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
                print(f"Basse: {low}%\n")
                print(f"Medie: {mid}%\n")
                print(f"Alte: {high}%\n")
                print(f"Critiche: {critical}%")
                break
        except ValueError:
            print("File non trovato, reinserire: ")
    return 0

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit(f"\nScript interrotto dall'utente")