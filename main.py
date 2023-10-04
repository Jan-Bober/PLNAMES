import pandas as pd
data = pd.read_csv("7-_WYKAZ_IMION_MĘSKICH_WG_POLA_IMIĘ_PIERWSZE_WYSTĘPUJĄCYCH_W_REJESTRZE_PESEL_Z_UWZGLĘDNIENIEM_IMION_OSÓB_ZMARŁYCH.csv")

data = data.iloc[0:, 0]
dlugosc_wszystkich = 0
najkrotsze = ["KJHBSAKJDBAKSJDBHJABHKJBHJKSABJHKBJKHABjkhasbjbjsjedbbhsejfd"]
najdluzsze = [""]
ilosc_imion = 0

for i in data:
    dlugosc_wszystkich += len(i)

    if len(i) > len(najdluzsze[0]):
        najdluzsze = [i]

    elif len(i) == len(najdluzsze[0]):
        najdluzsze.append(i)

    if len(i) < len(najkrotsze[0]):
        najkrotsze = [i]

    elif len(i) == len(najkrotsze[0]):
        najkrotsze.append(i)


print(f'Najdluzdze imiona to:{najdluzsze}')
print(f'Najkrotsze imiona to:{najkrotsze}')
print(f'Srednia dlugosc wynosi{dlugosc_wszystkich/len(data)}')