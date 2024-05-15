import numpy as np
import pandas as pd 

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)


def teams():
    teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
    return {"teams":teams}

def teamVteam(team1,team2):
    if team1 in list(set(list(matches['Team1'])+list(matches['Team2']))) and team2 in list(set(list(matches['Team1'])+list(matches['Team2']))):
        df=matches[((matches['Team1']==team1) & (matches['Team2']==team2)) | ((matches['Team1']==team2) & (matches['Team2']==team1))]
        total_matches=df.shape[0]
        team1_win=df['WinningTeam'].value_counts()[team1]
        team2_win=df['WinningTeam'].value_counts()[team2]
        draws= total_matches-(team1_win+team2_win)
        team1_win_perc=team1_win/total_matches
        team2_win_perc=team2_win/total_matches
        return {
            "team1":team1,
            "team2":team2,
            "total matches":total_matches,
            team1:str(team1_win),
            team2:str(team2_win),
            "draws":str(draws),
            "team1 win perc":str(team1_win_perc*100),
            "tean2 win perc":str(team2_win_perc*100)    
        }
    else:
        return {"message":"Invalid Team Names"}
    

def teamStats(team):
    if team in list(set(list(matches['Team1'])+list(matches['Team2']))) :
        teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
        df=matches[(matches['Team1']==team)|(matches['Team2']==team)]
        total_matches=df.shape[0]
        win=df[df['WinningTeam']==team].shape[0]
        opp_win=df[df['WinningTeam']!=team].shape[0]
        draw=total_matches-win-opp_win
        tosswin=df[df['TossWinner']==team].shape[0]
        tossAndMatchWin=df[(df['TossWinner']==team)&(df['WinningTeam']==team)].shape[0]
        superover=df[df['SuperOver']=='Y'].shape[0]
        chaseWin=df[(df['WinningTeam']==team) & (df['WonBy']=='Wickets')].shape[0]
        defendWin=df[(df['WinningTeam']==team) & (df['WonBy']=='Runs')].shape[0]
        superoverWin=df[(df['WinningTeam']==team) & (df['WonBy']=='SuperOver')].shape[0]
        overall={
                "total_matches":str(total_matches),
                    "win":str(win),
                    "opp_win":str(opp_win),
                    "draw":str(draw),
                    "tosswin":str(tosswin),
                    "tossAndMatchWin":str(tossAndMatchWin),
                    "superover":str(superover),
                    "chaseWin":str(chaseWin),
                    "defendWin":str(defendWin),
                    "superoverWin":str(superoverWin)
                }

        opponent=[]
        for oppteam in teams:
            if oppteam==team:
                continue
            else:
                temp_df=df[(df['Team1']==oppteam)|(df['Team2']==oppteam)]
                total_matches=temp_df.shape[0]
                win=temp_df[temp_df['WinningTeam']==team].shape[0]
                opp_win=temp_df[temp_df['WinningTeam']==oppteam].shape[0]
                draw=total_matches-win-opp_win
                tosswin=temp_df[temp_df['TossWinner']==team].shape[0]
                tossAndMatchWin=temp_df[(temp_df['TossWinner']==team)&(temp_df['WinningTeam']==team)].shape[0]
                superover=temp_df[temp_df['SuperOver']=='Y'].shape[0]
                chaseWin=temp_df[(temp_df['WinningTeam']==team) & (temp_df['WonBy']=='Wickets')].shape[0]
                defendWin=temp_df[(temp_df['WinningTeam']==team) & (temp_df['WonBy']=='Runs')].shape[0]
                superoverWin=temp_df[(temp_df['WinningTeam']==team) & (temp_df['WonBy']=='SuperOver')].shape[0]
                opponent.append({oppteam:{
                "total_matches":str(total_matches),
                    "win":str(win),
                    "opp_win":str(opp_win),
                    "draw":str(draw),
                    "tosswin":str(tosswin),
                    "tossAndMatchWin":str(tossAndMatchWin),
                    "superover":str(superover),
                    "chaseWin":str(chaseWin),
                    "defendWin":str(defendWin),
                    "superoverWin":str(superoverWin)
                }})

        return {
             "overall":overall,
             "against":opponent
        }
    else :
         return {"message":"Invalid Team Names"}