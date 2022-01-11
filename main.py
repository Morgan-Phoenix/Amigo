import requests
from get_proxy import get_alltime_proxies

def proxy_connection(url:str,num:int):
    '''
    url --> the url to request
    num --> the number of proxies to use
    '''
    session = requests.Session()
    session.proxies = get_alltime_proxies(num)
    res = session.get(url)
    