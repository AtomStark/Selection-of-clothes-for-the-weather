from BD import create_tshirts, get_Сlothes
import postgresql

#create_tshirts("wi-fi", "gray")

db = postgresql.open('pq://postgres:postgres@localhost:5432/selectedDB')

def select_outerwear(temperature):
    if temperature > 16:
        outerwear = "Можно не одевать верхнюю одежду"
    elif temperature < 16 and temperature > 13:
        outerwear = "Можно одеть мантию"
    elif temperature < 13 and temperature > 1:
        outerwear = "Можно одеть плащь"
    else:
        outerwear = "Стоить одеть куртку"
    return outerwear
