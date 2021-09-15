import requests
from bs4 import BeautifulSoup

def teamFinder(year):
    team_id = 101
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('table', {'class': 'stats_table sortable', 'data-cols-to-freeze': ',2', 'id': 'per_game-team'})
    teams = []
    ids = {}
    trs = table.find_all('tr')
    x = 0
    for tr in trs[1:]:
        #print(tr.prettify())
        try:
            td = tr.find('td', {'data-stat': 'team', 'class': 'left'})
            a_tag = td.find('a')
            team = a_tag.get_text()
            teams.append(team)
            link = a_tag.attrs['href']
            link = list(link)
            acronym = link[7] + link[8] + link[9]
            ids[teams[x]] = []
            ids[teams[x]].append(acronym)
            x+=1
        except:
            pass
    for x in range(len(teams)):
        ids[teams[x]].append(team_id)
        team_id+=1
    return teams, ids

