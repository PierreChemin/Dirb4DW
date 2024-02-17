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
    report = "/Users/pierrechemin/Desktop/Cyllene/darkScan/reports/reportDark.txt"
    clear_file(report)

    print("-------------- commencement du dirD --------------")
    with open(url2test,"r", encoding='utf-8') as f1:
        for url in f1:
            url = url.strip() 
            with open(wordlist, "r", encoding='utf-8') as f2: 
                for page in f2:
                    page = page.strip()  
                    fullURL = purgeBack(url + '/' + page)
                    request = session.get(fullURL)
                    if ('200' in str(request) or '301' in str(request)) :
                        with open(report, 'a+', encoding='utf-8') as f3:
                            fullURL = fullURL + '\n'
                            f3.write(fullURL)

    print("-------------- fin du dirD --------------")
    return 0

if __name__ == "__main__":
    main()