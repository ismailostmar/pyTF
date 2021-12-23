from flask import Flask, render_template, request
import json
import pymongo

client = pymongo.MongoClient("mongodb+srv://ismailab:ur45apz3WVWff8uE@ismailcluster.1puht.mongodb.net/Lab2Python?retryWrites=true&w=majority")
db = client.Lab2Python


app = Flask(__name__)
#filename = 'covid16112020.json'


@app.route('/', methods=['GET'])
def index():
    return (render_template('index.html'))


@app.route('/', methods=['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']
    # print(country1,country2,country3)

    casesCountry1 = getCases(country1)
    casesCountry2 = getCases(country2)
    casesCountry3 = getCases(country3)
    print(casesCountry1)

    deathsCountry1 = getDeaths(country1)
    deathsCountry2 = getDeaths(country2)
    deathsCountry3 = getDeaths(country3)
    print(deathsCountry1)

    datelabels = getDates(country1)
    print(datelabels)

    return render_template('index.html', dateLabels=datelabels, country1=country1, country2=country2, country3=country3,
                           casesCountry1=casesCountry1, casesCountry2=casesCountry2, casesCountry3=casesCountry3, deathsCountry1=deathsCountry1 , deathsCountry2=deathsCountry2, deathsCountry3=deathsCountry3)

def getCases(country):
    caseList=[]
    for rec in db.CovidData.find({"countryterritoryCode": country}):
        caseList.append(int(rec["cases"]))
    return (list(reversed(caseList)))

def getDeaths(country):
    deathsList =[]
    for rec in db.CovidData.find({"countryterritoryCode": country}):
        deathsList.append(int(rec["deaths"]))
    return (list(reversed(deathsList)))

def getDates(country):
    dateRepList =[]
    for rec in db.CovidData.find({"countryterritoryCode": country}):
        dateRepList.append(rec["dateRep"])
    return (list(reversed(dateRepList)))


if __name__ == '__main__':
    app.run(debug=True)
