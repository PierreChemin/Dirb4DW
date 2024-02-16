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
                    print(fullURL, "before request")
                    #request = session.get(fullURL)
                    subprocess.run(['curl', '--socks5-hostname', 'localhost:9150', fullURL])
                    print("after request")
                    if '200' in str(request) or '301' in str(request):
                        fullURL += "\n"
                        print("ok")

    return 0

"""    with open(url2test,"r", encoding='utf-8') as f1:
        with open(wordlist, "r", encoding='utf-8') as f2:
            for url in f1:
                url = url.strip()
                print(url)
                for page in f2:
                    page = page.strip()  
                    fullURL = purgeBack(url + '/' + page)
                    print(fullURL)
                    request = session.get(fullURL)
                    if '200' in str(request) or '301' in str(request):
                        fullURL += "\n"
                        with open(report, "a+", encoding='utf-8') as f3:
                            f3.write(fullURL)  """
                    


if __name__ == "__main__":
    main()