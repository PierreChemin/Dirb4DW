import requests
import subprocess
import dirD

def connect2Tor():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150',
                    'https': 'socks5h://127.0.0.1:9150'}
    return session

session = connect2Tor()
siteO = "http://xmrhfasfg5suueegrnc4gsgyi2tyclcy5oz7f5drnrodmdtob6t2ioyd.onion/"
siteN = "https://youtube.com"

"""print("test avec les sites normaux : ")
print("site 1.1")
session.get(siteN)
print("site 1.2")
subprocess.run(['curl', '--socks5-hostname', 'localhost:9150', siteN]).stdout
print("done 1")"""

print("test avec les sites onion")
print("site 2.1")
request1 = session.get(siteO)
print("request 1 : ", request1)
request = session.get(siteN)
print("request 2 : \n", request)
"""print("site 2.2")
request2 = subprocess.run(['curl', '--socks5-hostname', 'localhost:9150', siteO], capture_output=True, encoding='utf-8')"""
"""
print("request 2 : \n", request2)"""
print("done")