from colorama import Fore

LOGO = """
                                               ________  ______  __________ 
                                              / ____/\ \/ / __ )/ ____/ __ \ 
                                             / /      \  / __  / __/ / /_/ /
                                            / /___    / / /_/ / /___/ _, _/ 
                                            \____/   /_/_____/_____/_/ |_|
"""
MENU = f"""
                                            {Fore.CYAN}[{Fore.WHITE}01{Fore.CYAN}] Example       {Fore.CYAN}[{Fore.WHITE}06{Fore.CYAN}] Example
                                            {Fore.CYAN}[{Fore.WHITE}02{Fore.CYAN}] Example       {Fore.CYAN}[{Fore.WHITE}07{Fore.CYAN}] Example
                                            {Fore.CYAN}[{Fore.WHITE}03{Fore.CYAN}] Example       {Fore.CYAN}[{Fore.WHITE}08{Fore.CYAN}] Example
                                            {Fore.CYAN}[{Fore.WHITE}04{Fore.CYAN}] Example       {Fore.CYAN}[{Fore.WHITE}09{Fore.CYAN}] Example
                                            {Fore.CYAN}[{Fore.WHITE}05{Fore.CYAN}] Example       {Fore.CYAN}[{Fore.WHITE}10{Fore.CYAN}] Example
"""

def MainMenu():
    print(Fore.CYAN + LOGO)
    print(MENU)
