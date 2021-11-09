import tui

def list_years(data):
    tui.started("Listing unique years")
    yearline = 9
    years = set()
    for record in data:
        year = record[yearline]
        years.add(year)
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started()
    columwithmedals = 14
    medals = {"Gold":0,"Silver":0,"Bronze":0}
    for record in data:
        medal = record[columwithmedals]
        if medal in ("Gold","Silver","Bronze"):
            medals[medal] += 1
    tui.display_medal_tally(medals)
    tui.completed()

def tally_team_medals(data):
    tui.started()
    columwithmedals = 14
    columofteams = 6
    team_medals = {}
    for record in data:
        team = record[columofteams]
        medals = record[columwithmedals]
        if medals not in ("Gold","Silver","Bronze"):
            continue
        if team in team_medals:
            team_medals[team][medals] += 1
        else:
            team_medals[team] = {"Gold":0,"Silver":0,"Bronze":0}
            team_medals[team][medals] += 1
    tui.display_team_medal_tally(team_medals)
    tui.completed()

#def run():
#    list_years("athlete_events.csv")
#    tally_medals("athlete_events.csv")
#    tally_team_medals("athlete_events.csv")

#run()
