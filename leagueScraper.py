import leagueRosters
import statScraper
def leagueScraper(year):
    rosters, team_ids = leagueRosters(year)
    y = 0
    for team in rosters:
        for x in range(len(rosters[team])):
            try:
                if x == 0 and y == 0:
                    player = rosters[team][x]
                    df = statScraper(player, year, '01', team, team_ids)
                else:
                    player = rosters[team][x]
                    df = df.append(statScraper(player, year, '01', team, team_ids))
            except:
                pass
        print(team, 'successfully scraped')
        y+=1
    return df