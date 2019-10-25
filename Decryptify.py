#!/usr/bin/python3
# generator for hackhebox invite code
# exmple: python hackthebox.py 
import base64
from os import system
RED = '\033[31m'
END = '\033[0m'
art = RED \
    + """                                                                                                                                                                                                

    )                                                        (                                                
 ( /(                )   *   )    )          (               )\ )                                 )           
 )\())    )       ( /( ` )  /( ( /(    (   ( )\          )  (()/(     (      (    (            ( /(      (    
((_)\  ( /(   (   )\()) ( )(_)))\())  ))\  )((_)  (   ( /(   /(_))   ))\  (  )(   )\ )  `  )   )\()) (   )(   
 _((_) )(_))  )\ ((_)\ (_(_())((_)\  /((_)((_)_   )\  )\()) (_))_   /((_) )\(()\ (()/(  /(/(  (_))/  )\ (()\  
| || |((_)_  ((_)| |(_)|_   _|| |(_)(_))   | _ ) ((_)((_)\   |   \ (_))  ((_)((_) )(_))((_)_\ | |_  ((_) ((_) 
| __ |/ _` |/ _| | / /   | |  | ' \ / -_)  | _ \/ _ \\ \ /   | |) |/ -_)/ _|| '_|| || || '_ \)|  _|/ _ \| '_| 
|_||_|\__,_|\__| |_\_\   |_|  |_||_|\___|  |___/\___//_\_\   |___/ \___|\__||_|   \_, || .__/  \__|\___/|_|   
                                                                                  |__/ |_|                    

                             [++] Decryptify is Hackthebox Invite code Decryptor [++]    
                                    Coded By: Ankit Dobhal                                
                                    Let's Begin To hack..!            
-------------------------------------------------------------------------------
""" \
    + END
print(art)

def invite():
    print("\nBase64 Encrypted code:\n")
    # curl command
    pcurl = "curl -XPOST https://www.hackthebox.eu/api/invite/generate"
    # os module to excute system command(curl)
    print(system(pcurl))
    code = input("\nEnter your base64 code:\n")
    print('\nNow Decrypting...\n')
    # base64 module to decrypt base64 encrypted code
    base = base64.b64decode(code + '=' * (-len(code)%4))
    print('This is your hackthebox invite code : ',base)
invite()
