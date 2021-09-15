import teamFinder
import statScraper
def playerScraper(name, team, year):
    name = name.split()
    name.append('1001')
    teams, team_ids = teamFinder(year)
    df = statScraper(name, year, '01', team, team_ids)
    return df