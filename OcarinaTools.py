from pystyle import Colors, Colorate, Center
from colorama import Fore, Back, Style
import colorama
import subprocess


def ping_ip(ip_address):
    try:
        result = subprocess.run(['ping', ip_address], capture_output=True, text=True, timeout=10)
        print(Colorate.Horizontal(Colors.blue_to_red, f"\n{'=' * 60}\nPINGING {ip_address}\n{'=' * 60}"))
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print(Colorate.Horizontal(Colors.blue_to_red, "Timeout expired. No response received."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.blue_to_red, f"An error occurred: {e}"))


ascii_art = '''

 ▄██████▄   ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄      ▄████████         ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
███    ███ ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄   ███    ███     ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
███    ███ ███    █▀    ███    ███   ███    ███ ███▌ ███   ███   ███    ███        ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
███    ███ ███          ███    ███  ▄███▄▄▄▄██▀ ███▌ ███   ███   ███    ███         ███   ▀ ███    ███ ███    ███ ███         ███        
███    ███ ███        ▀███████████ ▀▀███▀▀▀▀▀   ███▌ ███   ███ ▀███████████         ███     ███    ███ ███    ███ ███       ▀███████████ 
███    ███ ███    █▄    ███    ███ ▀███████████ ███  ███   ███   ███    ███         ███     ███    ███ ███    ███ ███                ███ 
███    ███ ███    ███   ███    ███   ███    ███ ███  ███   ███   ███    ███         ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
 ▀██████▀  ████████▀    ███    █▀    ███    ███ █▀    ▀█   █▀    ███    █▀         ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                                     ███    ███                                                                   ▀                      

                                 --------------------[Ocarina Tools]--------------------
                                      01) Ping IP                  06) SOON                      
                                      02) IP Information           07) SOON                                                  
                                      03) SOON                     08) SOON                    
                                      04) SOON                     09) SOON
                                      05) SOON                     20) SOON

'''

colored_ascii = Colorate.Horizontal(Colors.blue_to_purple, ascii_art)
print(Center.XCenter(colored_ascii))

while True:
    option = input(Colorate.Horizontal(Colors.blue_to_purple, "\nEnter your choice: "))
    if option == "01":
         ip_address = input(Colorate.Horizontal(Colors.blue_to_red, "Enter IP address to ping: "))
         ping_ip(ip_address)  

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                           