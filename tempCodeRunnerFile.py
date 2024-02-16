def connect2Tor():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150',
                       'https': 'socks5h://127.0.0.1:9150'}
    return session