import json
import codecs
import requests
import operator
from math import cos, asin, sqrt

# with open('gpd.json', encoding="UTF-8") as json_data:
#     d = json.load(json_data)
#     print(d)
#     print('|')

dictD = json.loads(codecs.open('gpdmini.json', 'r', 'utf-8-sig').read())


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...


print(dictD["global_power_plant_database"][0]["name"])


# json_df = pd.read_json('gpd.json',encoding='UTF-8')


def findClose(inLat, inLong):
    distanceDict = {}
    # keep array of top N values
    # calculate the distance from each value in array
    # check if distance is less than the top in the array. 
    # if less, then put it in (keep array of index values)

    # THANK SALVADOR DALI ON https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula

    for plant in dictD["global_power_plant_database"]:
        plantDistance = distance(inLat,inLong,float(plant["latitude"]),float(plant["longitude"]))
        distanceDict[dictD["global_power_plant_database"].index(plant)] = abs(plantDistance)
        #print(plantDistance)
        if len(distanceDict) > 3:
                drop = max(distanceDict,key=distanceDict.get)
                distanceDict.pop(drop)

    print(distanceDict)
    # These are the three closest. 

    #Now get and format their data        


# for plant in dictD["global_power_plant_database"]:
#         print(plant["latitude"])
#         print(plant["longitude"])

    outfile = {}

    outfile["data"] = [dictD["global_power_plant_database"][int(list(distanceDict.keys())[0])],dictD["global_power_plant_database"][int(list(distanceDict.keys())[1])],dictD["global_power_plant_database"][int(list(distanceDict.keys())[2])]]

    r = requests.get('127.0.0.1:3000')
    r.json(outfile)

    print(json.dumps(outfile))







findClose(52.987010,10.751980)