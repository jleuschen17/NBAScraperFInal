import teamFinder
import statScraper
def playerScraper(name, team, year):
    name = name.split()
    name.append('1001')
    teams, ids = teamFinder(year)
    team_id = ids[team][0]
    df = statScraper(name, year, '01', team_id)
    return df