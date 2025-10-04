import requests
from astroquery.simbad import Simbad
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astroplan import Observer, FixedTarget
from astroplan.observer import TargetAlwaysUpWarning, TargetNeverUpWarning


def main():
    object = input("Hello Observer! What would you like to observe today?\n")
    location = input("Enter your location: ")

    long, lat = get_API(location)
    if long == None or lat == None:
        print("That is not a valid location.")
        return 0

    get_observability(object, long, lat)



def get_observability(object, long, lat):

    # query the object using simbad
    result_table = Simbad.query_object(object)

    object_ra = result_table['ra'].data[0]
    object_dec = result_table['dec'].data[0]

    user_location = EarthLocation(lon=long, lat=lat)
    observer_location = Observer(location = user_location)



# gets the user location (longitude and latitude)
def get_API(location):
    geocode_url = r"https://geocoding-api.open-meteo.com/v1/search?name=Baltimore&count=10&language=en&format=json"
    params = {"name: ": location}

    response = requests.get(geocode_url, params=params)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        result = data["results"][0]
        return result["longitude"], result["latitude"]
    else:
        return None, None



if __name__ == "__main__":
    main()