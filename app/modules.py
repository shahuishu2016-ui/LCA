import requests
import bs4
import json
import pandas as pd
import re

def get_slug():
    url = "https://cricheroes.com/"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7",
        "priority": "u=0, i",
        "referer": "https://www.google.com/",
        "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
    }
    response = requests.request("GET", url, headers=headers)
    soup = bs4.BeautifulSoup(response.content,'html.parser')
    slug = json.loads(soup.find_all('script')[-1].text)['buildId']
    return slug

def get_team_members(slug,team_id,team_name,cookies):
    team_name = team_name.lower().replace(' ','-')
    # url = "https://cricheroes.com/_next/data/su67viR6uXe4l_EAsPwBq/team-profile/7680305/lucky-cricket-aca/members.json"
    url = f"https://cricheroes.com/_next/data/{slug}/team-profile/{team_id}/{team_name}/members.json"
    querystring = {"teamId":team_id,"teamName":team_name,"tabName":"members"}
    payload = ""
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cookie": cookies,
        "priority": "u=1, i",
        # "referer": "https://cricheroes.com/tournament/1117955/u-14-sangli-district-trophy-2024/teams",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-nextjs-data": "1"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_profile_matches(slug,player_id,player_name,cookies):
    # url = "https://cricheroes.com/_next/data/su67viR6uXe4l_EAsPwBq/player-profile/4624319/shahu-patil/matches.json"
    url = f"https://cricheroes.com/_next/data/{slug}/player-profile/{player_id}/{player_name}/matches.json"
    querystring = {"playerId":player_id,"playerName":player_name,"tabName":"matches"}
    payload = ""
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cookie": cookies,
        "priority": "u=1, i",
        # "referer": "https://cricheroes.com/team-profile/7680305/lucky-cricket-aca/members",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-nextjs-data": "1"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_scorecard(slug,match_id,teamNames,cookies):
    # url = "https://cricheroes.com/_next/data/su67viR6uXe4l_EAsPwBq/scorecard/14354358/individual/shivneri-vs-lucky-cricket-aca/scorecard.json"
    url = f"https://cricheroes.com/_next/data/{slug}/scorecard/{match_id}/individual/{teamNames}/scorecard.json"
    querystring = {"matchId":match_id,"tournamentName":"individual","teamNames":teamNames,"tab":"scorecard"}
    payload = ""
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cookie": cookies,
        "priority": "u=1, i",
        "referer": f"https://cricheroes.com/scorecard/{match_id}/individual/{teamNames}",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-nextjs-data": "1"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_matches(player_id,matches,authorization="95976690-c7ff-11ef-be6d-07346494aad3",uuid_="cde2e79eebeab037bb35192e3aae00a9"):
    url = f"https://cricheroes.in/api/v1/player/get-player-match/{player_id}"
    querystring = {"pagesize":f"{matches+5}"}
    payload = ""
    headers = {
        "cookie": "connect.sid=s%253A0QAP6wj1l3l6Q1JFnU9ntSnWZMOfI19a.38cSrson3XvzDANZQGiFcEjbLNTK4umXh20QMkPB538",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "api-key": "cr!CkH3r0s",
        "authorization": authorization,
        "device-type": "Chrome: 131.0.0.0",
        "origin": "https://cricheroes.com",
        "priority": "u=1, i",
        "referer": "https://cricheroes.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "udid": uuid_,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_out_details(out):
    out_by = ''
    out_ = ''
    out = out.lower()
    if 'not out' in out:
        out_ = 'Not Out'
    elif 'retired' in out:
        out_ = 'Retired'
    elif 'hit wkt' in out:
        out = 'Hit Wkt'
    elif 'run out' in out:
        out_ = 'Run Out'
    elif out.split()[0] == 'b':
        out_ = 'Bowled'
        out_by = out.split('b')[1].strip()
    elif out.split()[0] == 'c':
        out_ = 'Catch Out'
        out_by = out.split('b')[1].strip()
    elif out.split()[0] == 'st':
        out_ = 'Stumping'
        out_by = out.split('b')[1].strip()
    elif out.split()[0] == 'lbw':
        out_ = 'LBW'
        out_by = out.split('b')[1].strip()
    return out_.title(),out_by.title()


def get_batting_bowing_data(match,get_batting=True,get_bowling=True):
    date_ = match['match_start_time'].split('T')[0]
    ground_id = match['ground_id']
    match_id = match['match_id']
    team_a = match['team_a']
    team_b = match['team_b']
    ground_name = match['ground_name']
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    # team_b_id = match['team_b_id']
    # team_a_id = match['team_a_id']
    winning_team_id = match['winning_team_id']
    toss_won = match['toss_details'].split('won')[0].strip()
    winning_team = match['match_summary']['summary'].split('won')[0].strip()
    teams = [team_a,team_b]
    for team in teams:
        if teamName != team:
            opponent = team
    teamNames = team_a.replace(' ','-').lower() + "-vs-" + team_b.replace(' ','-').lower()
    scores = get_scorecard(slug,match_id,teamNames,cookies)
    overs_,balls_,maidens_,runs_,wickets_,fours_,sixes_,wide_,noball_,extra_type_run_wide,extra_type_run_noball,extra_run,bonus_run,economy_rate,inning = '','','','','','','','','','','','','','',''
    runs,balls,minutes,fours,sixes,st_rate,out_,out_by = '','','','','','','',''
    try:
        for sc in scores['pageProps']['scorecard']:
            played = False
            if get_batting:
                for batter in sc['batting']:
                    if batter['player_id'] == int(player_id):
                        try:
                            runs = batter['runs']
                        except:
                            pass
                        try:
                            balls = batter['balls']
                        except:
                            pass
                        try:
                            minutes = batter['minutes']
                        except:
                            pass
                        try:
                            fours = batter['4s']
                        except:
                            pass
                        try:
                            sixes = batter['6s']
                        except:
                            pass
                        try:
                            st_rate = batter['SR']
                        except:
                            pass
                        try:
                            out = batter['how_to_out']
                        except:
                            pass
                        try:
                            out_,out_by = get_out_details(out)
                        except:
                            pass
                        played = True
                        df1 = pd.DataFrame({
                            "Player_id":[player_id],
                            "Player_name":[player_name],
                            "Date":[date_],
                            "Match_id":[match_id],
                            "Groung_id":[ground_id],
                            "Venue":[ground_name],
                            "Opponent":[opponent],
                            "Toss":[toss_won],
                            "Winner":[winning_team],
                            "Runs":[runs],
                            "Balls":[balls],
                            "Minutes_played":[minutes],
                            "Foures":[fours],
                            "Sixes":[sixes],
                            "Strike_rate":[st_rate],
                            "Out":[out_],
                            "Out_by":[out_by],
                        })
                        # batting_df = pd.concat([batting_df,df1],ignore_index=True)
                        break
            if not played:
                if get_bowling:
                    for bowler in sc['bowling']:
                        if bowler['player_id'] == int(player_id):
                            try:
                                overs_ = bowler['overs']
                            except:
                                pass
                            try:
                                balls_ = bowler['balls']
                            except:
                                pass
                            try:
                                maidens_ = bowler['maidens']
                            except:
                                pass
                            try:
                                runs_ = bowler['runs']
                            except:
                                pass
                            try:
                                wickets_ = bowler['wickets']
                            except:
                                pass
                            try:
                                fours_ = bowler['4s']
                            except:
                                pass
                            try:
                                sixes_ = bowler['6s']
                            except:
                                pass
                            try:
                                wide_ = bowler['wide']
                            except:
                                pass
                            try:
                                noball_ = bowler['noball']
                            except:
                                pass
                            try:
                                extra_type_run_wide = bowler['extra_type_run_wide']
                            except:
                                pass
                            try:
                                extra_type_run_noball = bowler['extra_type_run_noball']
                            except:
                                pass
                            try:
                                extra_run = bowler['extra_run']
                            except:
                                pass
                            try:
                                bonus_run = bowler['bonus_run']
                            except:
                                pass
                            try:
                                economy_rate = bowler['economy_rate']
                            except:
                                pass
                            try:
                                inning = bowler['inning']
                            except:
                                pass
                            df2 = pd.DataFrame({
                                "Player_id":[player_id],
                                "Player_name":[player_name],
                                "Date":[date_],
                                "Match_id":[match_id],
                                "Inning":[inning],
                                "Groung_id":[ground_id],
                                "Venue":[ground_name],
                                "Opponent":[opponent],
                                "Toss":[toss_won],
                                "Winner":[winning_team],
                                "Overs":[overs_],
                                "Runs":[runs_],
                                "Maidens":[maidens_],
                                "Wickets":[wickets_],
                                "Fours":[fours_],
                                "Sixes":[sixes_],
                                "Wides":[wide_],
                                "No_balls":[noball_],
                                "Extra_type_run_wide":[extra_type_run_wide],
                                "Extra_type_run_noball":[extra_type_run_noball],
                                "Extra_run":[extra_run],
                                "Bonus_runs":[bonus_run],
                                'Economy_rate':[economy_rate]
                            })
                            # bowling_df = pd.concat([bowling_df,df2],ignore_index=True)
                            break
    except:
        pass
    return df1,df2

def get_cookies():
    url = "https://cricheroes.in/api/v1/player/get-player-filter-new/4624319"
    payload = ""
    headers = {
        "cookie": "connect.sid=s%253Aucm3Ff0eBx1XSFzRtC-CrLx2BUfXV40d.3SL%252Bffu7cmQic%252FAZcPy7WdrxFgaklsHwj40rnp0CN0w",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "api-key": "cr!CkH3r0s",
        "authorization": "95976690-c7ff-11ef-be6d-07346494aad3",
        "device-type": "Chrome: 131.0.0.0",
        "if-none-match": 'W/"953-uGRLBCOZS7YRNZkwgOXiFg"',
        "origin": "https://cricheroes.com",
        "priority": "u=1, i",
        "referer": "https://cricheroes.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "udid": "cde2e79eebeab037bb35192e3aae00a9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    cookies = response.cookies.get('connect.sid')
    return cookies

def get_player_id(name,teamId,teamName,cookies):
    slug = get_slug()
    print(slug)
    print(name)
    resp = get_team_members(slug,teamId,teamName,cookies)
    results = {}
    for player in resp['pageProps']['members']['data']['members']:
        if name.lower() in player['name'].lower():
            name_ = " ".join([i.strip() for i in player['name'].split()])
            print(name_)
            results[name_] = player['player_id']
    return results

def extract_cricket_stats(text):
    clean = re.sub(r"<.*?>", "", text)
    patterns = {
        "turns": r"With\s+(\d+)\s+turns",
        "top_score": r"top score of\s+(\d+)",
        "average": r"average of\s+([\d.]+)",
        "strike_rate": r"strike rate of\s+([\d.]+)",
        "sixes": r"(\d+)\s+sixes",
        "fours": r"(\d+)\s+fours",
        "overs": r"bowled\s+([\d.]+)\s+overs",
        "wickets": r"taking\s+(\d+)\s+wickets",
        "economy": r"economy rate of\s+([\d.]+)"
    }
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, clean)
        extracted[key] = match.group(1) if match else None
    return extracted

#############  matches and player profile
if __name__ == '__main__':
    slug = get_slug()
    player_id = '4624319'
    player_name = 'shahu-patil'
    teamName = 'Lucky Cricket Aca'
    teamId = '7680305'
    cookies = get_cookies()
    pls = get_player_id('shahu')
    player_name = 'shahu patil'
    player_id = pls[player_name]
    # resp = get_team_members(slug,teamId,teamName,cookies)
    resp = get_profile_matches(slug,player_id,player_name,cookies)
    player_data = resp['pageProps']['playerInfo']['data']
    city = player_data['city_name']
    bowling_style = player_data.get('bowling_style')
    batting_hand = player_data.get('batting_hand')
    batter_category = player_data.get('batter_category')
    bowler_category = player_data.get('bowler_category')
    playing_role = player_data.get('playing_role')
    dob = player_data.get('dob')
    total_matches = player_data.get('total_matches')
    total_wickets = player_data.get('total_wickets')
    total_runs = player_data.get('total_runs')

    resp = get_matches(player_id,total_matches)
    matches = resp['data']
    bowling_df = pd.DataFrame()
    batting_df = pd.DataFrame()
    get_batting = True
    get_bowling = True
    for match in matches:
        if match['status'] == 'past':
            df1,df2 = get_batting_bowing_data(match,get_batting=get_batting,get_bowling=get_bowling)
            if get_batting:
                batting_df = pd.concat([batting_df,df1],ignore_index=True)
            if get_bowling:
                bowling_df = pd.concat([bowling_df,df2],ignore_index=True)
    batting_df.to_excel(f"batting.xlsx",index=False)
    bowling_df.to_excel(f"bowling.xlsx",index=False)