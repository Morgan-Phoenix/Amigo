import requests, os

def get_alltime_proxies(no:int):
    url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        proxies = []
        os.remove('proxy.json')
    for i in range(no):
        proxies.append(proxy[i])
    return proxies

def get_http_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    return proxy

def get_socks4_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    return proxy

def get_socks5_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    return proxy
    