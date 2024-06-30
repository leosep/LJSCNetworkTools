import requests

def proxy_checker(proxy):
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
        if response.status_code == 200:
            print("Proxy is working")
        else:
            print("Proxy is not working")
    except requests.RequestException:
        print("Proxy is not working")
