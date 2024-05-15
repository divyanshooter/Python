from flask import Flask,jsonify,request
import ipl

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to IPL API Services"

@app.route("/api/teams")
def teamNames():
    teams=ipl.teams()
    return jsonify(teams)

@app.route("/api/teamVteam")
def teamVsteam():
    team1=request.args.get("team1")
    team2=request.args.get("team2")
    return jsonify(ipl.teamVteam(team1,team2))

@app.route("/api/teamStats")
def teamStats():
    team=request.args.get("team")
    return jsonify(ipl.teamStats(team))


app.run(debug=True)