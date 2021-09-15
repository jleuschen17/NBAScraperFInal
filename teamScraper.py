import teamRoster
import statScraper
def teamScraper(team, year):
    roster, team_ids = teamRoster(team, year)
    for x in range(len(roster)):
        try:
            if x == 0:
                player = roster[x]
                df = statScraper(player, year, '01', team, team_ids)
            else:
                player = roster[x]
                df2 = statScraper(player, year, '01', team, team_ids)
                df = df.append(df2)
        except:
            pass
    return df