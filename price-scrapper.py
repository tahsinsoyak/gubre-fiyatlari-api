import pandas as pd
from bs4 import BeautifulSoup
import requests


def _scrape_data():
    url = 'https://www.endetayli.com/gubre-fiyatlari/'
    response = requests.get(url)

    gubre_ismi = []
    gubre_fiyati = []

    html_content = response.content
    html_content_string = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    tables = soup.findAll('table')

    for oneeach in tables[1:]:
        for row in oneeach.findAll('tr'):
            columns = row.findAll('td')
            if(columns != []):
                gubre_ismi.append(columns[0].text.strip())
                gubre_fiyati.append(columns[1].text.strip())
                
    df = pd.DataFrame({'Gübre İsimleri': gubre_ismi,
                        'Gübre Fiyatları': gubre_fiyati
                        })
    return df



def _kaydet():
    df = _scrape_data()
    result = df.to_json(orient="records")
    with open(f"src/gubrefiyatlari.json","w") as file:
        file.write(result)


if __name__ == "__main__":
    _kaydet()