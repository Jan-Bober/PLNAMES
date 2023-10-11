import pandas as pd
data = pd.read_csv("7-_WYKAZ_IMION_MĘSKICH_WG_POLA_IMIĘ_PIERWSZE_WYSTĘPUJĄCYCH_W_REJESTRZE_PESEL_Z_UWZGLĘDNIENIEM_IMION_OSÓB_ZMARŁYCH.csv")

data = data.iloc[0:, 0]
print(data)
length_of_all = 0
shortest = ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]
longest = [""]

for i in data:
    length_of_all += len(i)

    if len(i) > len(longest[0]):
        longest = [i]

    elif len(i) == len(longest[0]):
        longest.append(i)

    if len(i) < len(shortest[0]):
        shortest = [i]

    elif len(i) == len(shortest[0]):
        shortest.append(i)


print(f'Najdluzdze imiona to:{longest}')
print(f'Najkrotsze imiona to:{shortest}')
print(f'Srednia dlugosc wynosi{length_of_all/len(data)}')
