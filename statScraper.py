import urlConvertor
import requests
from bs4 import BeautifulSoup
import pandas as pd

def statScraper(name, year, playerindex, team_id):
    index = int(playerindex)
    for x in range(2):
        url, advanced = urlConvertor(name, year, playerindex, x)
        print(url)
        try:
            result = requests.get(url)
            print(result.status_code)
            src = result.content
            soup = BeautifulSoup(src, 'lxml')
            table = soup.find('table', {'class': 'row_summable'})
            trs = table.find_all('tr')
            rows = []
            for tr in trs:
                tds = tr.find_all('td')
                row = [td.text.replace('\n', '').strip() for td in tds]
                rows.append(row)
            if x == 0:
                columns = ['G', 'Date', 'Age', 'Tm', 'Location', 'Opp',
                           'GS', 'Active', 'MP', 'FG', 'FGA', 'FG%',
                           '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB',
                           'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
                           'PTS', 'GmSc', '+/-']
                df = pd.DataFrame(rows, columns=columns)
                df = df[df['Tm'] == team_id]
                if len(df) == 0:
                    index += 1
                    newindex = '0' + str(index)
                    statScraper(name, year, newindex, team_id)
                result.close()
                df['PlayerID'] = name[2]
            elif x == 1:
                columns = ['G', 'Date', 'Age', 'Tm', 'Location', 'Opp', 'GS',
                           'Active', 'MP', 'TS%', 'eFG%', 'ORB%', 'DRB%',
                           'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%',
                           'USG%', 'ORtg', 'DRtg', 'GmSc', 'BPM']
                df2 = pd.DataFrame(rows, columns=columns)
                df2 = df2[df2['Tm'] == team_id]
                if len(df2) == 0:
                    index += 1
                    newindex = '0' + str(index)
                    statScraper(name, year, newindex, team_id)
                result.close()
                df2 = df2.drop(df2.columns[[0, 2, 3, 4, 5, 6, 7, 8, -2]], axis=1)
        except:
            print('Error Scraping' ,index)
            index+=1
            if index > 4:
                print('Stat scraping failed for:', name[0], name[1])
                print(url)
                return None
            newindex = '0' + str(index)
            statScraper(name, year, newindex, team_id)
    statdf = pd.merge(df, df2,how='outer', on='Date')
    statdf.insert(0, 'Name', name[1] + ', ' + name[0])
    print('Successfully Scraped:', name[0], name[1])
    return statdf