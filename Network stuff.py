import requests

base = '/maps/api/geocode/json'

def geocode(address):
    parameters = {'address':address, 'sensor': 'false'}
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer=response.json()
    print(answer)
    input()
    print(answer['results'][0]['geometry']['location'])

if __name__=="__main__":
    address = '1 Seahawk Dr, North East, MD'
    geocode(address)

