import json
import argparse
from urllib import request
from pprint import pprint
from obrazek import *


class Mapper(object):


    def __init__(self, address):
        self.address = address
        self.json_data = self.get_json_data()

    def get_json_data(self):
        address_with_spaces_replaced = self.address.replace(' ', '%20')
        with request.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={},%20pl&sensor=false".format(address_with_spaces_replaced)) as url:
            return json.loads(url.read().decode())

    def get_coordinates(self):
        '''
        Returns lattitude and longitude in form of 2 element tuple, every element is a float.
        Like:
            51.5, 23.5
        '''
        return self.json_data['results'][0]['geometry']['location']['lat'], self.json_data['results'][0]['geometry']['location']['lng']



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", help='printing urls', required=True)
    args = parser.parse_args()
    genmap = Mapper(args.address)
    lat, lng = genmap.get_coordinates()
    x,y = get_point_on_map(lng, lat)
    draw_point_on_image(x, y)


if __name__ == '__main__':
    main()


