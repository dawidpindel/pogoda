from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES = ['Warszawa','Gdańsk']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows =[
    ['Miasto','Godzina_pomiaru', 'Temperatura']
    ]
    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura']
                ])
    table=AsciiTable(rows)
    print(table.table)
                
if __name__ == '__main__':
    print('Pogodynka 2023')
    main()
