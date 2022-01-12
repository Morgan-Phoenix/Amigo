import requests, os
import urllib.request
import urllib.error
import sys

def get_bad_proxy(proxy:list):   
    total_proxies = len(proxy)
    checked_proxy = 0
    print("checking...")
    for e,i in enumerate(proxy):
        sys.stdout.write("\r{0}".format(f"currently checking {i}"))
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': i})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req=urllib.request.Request('http://www.google.com') 
            sock=urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            proxy.pop(e)
        except Exception:
            proxy.pop(e)
        sys.stdout.flush()
        checked_proxy+=1
        if checked_proxy== int((25*total_proxies)/100):
            print("\n","checked 25% proxies")
            print("checking Further")
        if checked_proxy== int((50*total_proxies)/100):
            print("\n","checked 50% proxies")
            print("checking Further")
        if checked_proxy== int((75*total_proxies)/100):
            print("\n","checked 75% proxies")
            print("checking Further")
    return proxy

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
    proxies = get_bad_proxy(proxies)
    return proxies

def get_http_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    proxy = get_bad_proxy(proxy)
    return proxy

def get_socks4_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    proxy = get_bad_proxy(proxy)
    return proxy

def get_socks5_proxies():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
    r = requests.get(url, allow_redirects=True)
    open('proxy.json', 'wb').write(r.content)
    with open('proxy.json','r') as f:
        proxy = f.read().split('\n')
        os.remove('proxy.json')
    proxy = get_bad_proxy(proxy)
    return proxy