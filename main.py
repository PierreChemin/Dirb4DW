import requests
import subprocess
import dirD

def connect2Tor():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9150',
                       'https': 'socks5h://127.0.0.1:9150'}
    return session

def test2Connect():
    #Windows version
    output = subprocess.run(['powershell', '-command', "Test-NetConnection -ComputerName localhost -Port 9150"], capture_output=True, text=True)
    if "TcpTestSucceeded : True" in output.stdout:
        print("connecté à TOR")
    else :
        print("pas connecté à TOR - ARRET -")
        return 0

def main():

    if test2Connect() == 0 : return 0
    dirD.main()

    return 0

if __name__ == "__main__":
    main()