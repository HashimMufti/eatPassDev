# eatPassDev-CLI runs from here
import config
import requests
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def findAllRestaurants():
    # Find all restauraunts in area according to all services
    pass


def findZomataoRestaurants():
    # Find all restaraunts in area according to Zomato
    pass


def findGoogleLocation(location='test'):
    log.debug("Location: " + location)
    response = requests.get(config.googleAutoCompleteURL,
                            params={"input": location,
                                    "key": config.googleApiKey})
    log.debug("Response URL: " + response.url)
    return(response)


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
