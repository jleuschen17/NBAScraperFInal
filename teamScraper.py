import teamRoster
import statScraper
def teamScraper(team, year):
    roster, team_ids = teamRoster(team, year)
    for x in range(len(roster)):
        try:
            if x == 0:
                player = roster[x]
                df = statScraper(player, year, '01', team_ids[team][0])
            else:
                player = roster[x]
                df = df.append(statScraper(player, year, '01', team_ids[team][0]))
        except:
            pass
    return df