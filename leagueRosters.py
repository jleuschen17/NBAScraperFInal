import teamFinder
import rosterScraper
def leagueRosters(year):
    teamrosters = {}
    id_number = 1001
    teams, team_ids = teamFinder(year)
    for team in teams:
        teamrosters[team] = rosterScraper(team_ids[team][0], year, id_number)
        id_number+=len(teamrosters[team])
    return teamrosters, team_ids