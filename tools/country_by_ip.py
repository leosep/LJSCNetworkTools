import requests

def country_by_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    print(f"IP: {data['ip']}")
    print(f"Country: {data['country']}")
    print(f"Region: {data['region']}")
    print(f"City: {data['city']}")
    print(f"Location: {data['loc']}")
