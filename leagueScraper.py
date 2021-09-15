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
                    print(player)
                    df = statScraper(player, year, '01', team_ids[team][0])
                else:
                    player = rosters[team][x]
                    df = df.append(statScraper(player, year, '01', team_ids[team][0]))
            except:
                pass
        y+=1
    return df