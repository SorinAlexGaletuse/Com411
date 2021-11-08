import tui

def list_years(data):
    tui.started()
    year = 9
    years = set()
    for record in data:
        year = data[year]
        years.add(year)
        tui.display_years(years)
    tui.completed()

def run():
    list_years("athlete_events.csv")
run()
