import subprocess
import requests

def connect2Tor():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150',
                       'https': 'socks5h://127.0.0.1:9150'}
    return session

def purgeBack(string):
    return string.replace("\n", "")

def clear_file(filename):
    with open(filename, "w", encoding='utf-8') as file:
        file.truncate(0)

def main():

    session = connect2Tor()
    #Récupération de la wordlist, des urls et de l'output
    wordlist = "wordlists/small.txt"
    url2test = "wordlists/url2test.txt"
    report = "report/report.txt"
    clear_file(report)

    with open(url2test,"r", encoding='utf-8') as f1:
        for url in f1:
            url = url.strip() 
            with open(wordlist, "r", encoding='utf-8') as f2: 
                for page in f2:
                    page = page.strip()  
                    fullURL = purgeBack(url + '/' + page)
                    print(fullURL)
                    #faire un try ici pour pas que ça s'arrête
                    """request = session.get(fullURL)
                    if '200' or '301' or '404' in request :
                        with open(report, 'a+', encoding='utf-8') as f3:
                            f3.write(fullURL)
                    return 0"""

    return 0

if __name__ == "__main__":
    main()