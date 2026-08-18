from datetime import date

dagens_datum = str(date.today())

personens_födelsedag = input("Vad är din födelsedag? (yyyy-mm-dd) \n")

if personens_födelsedag == dagens_datum:
    print("Grattis!!!")