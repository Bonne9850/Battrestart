# Kommunens befolkning

# Vid början av 2022 var invånarantalet 26 000
# Antalet födda och avlidna under ett år uppskattas vara 0.7% resp. 0.6%
# Antalet inflyttade och utflyttade uppskattas 300 resp. 325 per år

year = int(
    input("Vilket år vill du veta invånarantalet? Ange ett årtal efter 2022: ")
)

diff = year - 2022
population = 26000

for i in range(diff):
    born = population * 0.007
    dead = population * 0.006
    population = population + born - dead - 25 # 325 utflyttande minus 300 inflyttande = -25

# Avrundar till närmsta heltal vid utskrift
print(f"År {year} beräknas invånarantalet vara {round(population)} st.")