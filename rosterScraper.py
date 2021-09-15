import requests
from bs4 import BeautifulSoup
import unidecode
import re
def rosterScraper(TeamID, year, id_number):
    url = f"https://www.basketball-reference.com/teams/{TeamID}/{year}.html"
    result = requests.get(url)
    try:
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        table = soup.find('table', {'class': 'sortable'})
        names = []
        trs = table.find_all('tr')
        rows = []
        for tr in trs:
            try:
                td = tr.find('td', {'data-stat': 'player'})
                a_tag = td.find('a')
                name = a_tag.get_text()
                name = unidecode.unidecode(name)
                name = re.sub(r'[^\w\s]','',name)
                names.append(name)
            except:
                pass
        for x in range(len(names)):
            names[x] = names[x].split()
            names[x].append(id_number)
            id_number += 1
        print(TeamID,"roster successfully parsed")
        return names
    except:
        return False