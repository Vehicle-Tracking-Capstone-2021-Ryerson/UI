import requests
"""
These are functions to help make requests to our local data server running alongside the superscript
"""

SERVER_URL = "http://127.0.0.1:5000/"


def getDataFromEndpoint(endpoint):
    return requests.get(SERVER_URL+endpoint)


"""
Function for getting last GPS point

returns a GPS object:
    {"lat": latitude (double), "lon": longitude (double), "street": street (string), "speed": speed (double), "time": datetime.now()}
"""


def getLastGPSPoint():
    r = getDataFromEndpoint("getLastGPS")
    gpsDict = r.json()
    return gpsDict


"""
Function for getting last blindspot data point

pos -> String
    "F" - Front
    "L" - Left
    "B" - Back
    "R" - Right

returns a blindspot object
    {"data": distance in centimeters (int), "time": datetime.now()}
"""


def getLastBlindspot(pos):
    r = getDataFromEndpoint("getLastBlindspot/"+pos)
    blindspotDict = r.json()
    return blindspotDict


"""
Function for getting last OBD data point

returns an OBD object:

    {"rpm": rpm (int), "speed": speed (int), "throttle": throttle (int), "airTemp": airTemp (double), "fuel": fuelLevel (double), "time": datetime.now()}
"""


def getLastOBD():
    r = getDataFromEndpoint("getLastOBD")
    obdDict = r.json()
    return obdDict
