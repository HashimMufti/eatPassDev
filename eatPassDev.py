# eatPassDev-CLI runs from here
import config
import requests
import json


def findAllRestaurants():
    # Find all restauraunts in area according to all services
    pass


def findZomataoRestaurants():
    # Find all restaraunts in area according to Zomato
    pass


def findGoogleLocation(location='test'):
    respone = requests.get(config.googleAutoCompleteURL,
                           params={"input": location,
                                   "key": config.googleApiKey})
    return(respone.json())


def findGoogleRestaurants():
    # Find all restaurants in area according to Google
    pass


def findCurrentRestaurants():
    # Find if they are currently on the platform
    pass


def findHistoricalRestaurants():
    # Find if they have left the platform
    pass


def findEverRestaurants():
    # Find if they have ever been on the platform
    pass
