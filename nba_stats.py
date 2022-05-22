from requests import get

base_url = "https://data.nba.net"
all_json = "/prod/v1/today.json"


def get_links():
    data = get(base_url + all_json).json()
    links = data["links"]
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    data = get(base_url + scoreboard).json()['games']

    for game in data:
        home_team = game['hTeam']
        hteam = home_team['triCode']
        hscore = home_team['score']
        away_team = game['vTeam']
        ateam = away_team['triCode']
        ascore = away_team['score']

        clock = game['clock']
        period = game['period']
        print('------------------------')
        print(f"{hteam} vs {ateam}")
        print(f'{hscore} - {ascore}')
        print(f"{clock}-{period['current']}")


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    data = get(base_url + stats).json()['league']["standard"]['regularSeason']
    teams = data['teams']
    teams = list(filter(lambda x: x['name'] != 'Team', teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    for team in teams:
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f'{ppg["rank"]} {name} {nickname} - {ppg["avg"]}')


get_stats()
get_scoreboard()
