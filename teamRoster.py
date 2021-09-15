from teamFinder import teamFinder
from rosterScraper import rosterScraper
def teamRoster(team, year):
    roster = []
    id_number = 1001
    teams, team_ids = teamFinder(year)
    roster = rosterScraper(team_ids[team][0], year, id_number)
    return roster, team_ids