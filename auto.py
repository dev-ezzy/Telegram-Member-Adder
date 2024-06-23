import pyautogui
import time

# Read usernames from the 'users.txt' file and store them in a list
with open('telegram_contacts.csv', 'r') as file:
    all_usernames = [line.strip() for line in file.readlines()]
    time.sleep(7)

# Initialize the list to store the processed usernames
processed_usernames = []
831569064,T15,,nithinma6886730853,T13,,wealthbuilders111,6846343714,T14,,,6379900802,T21,,singhdua,6356209668,T28,,Bathe_fiducial,5708612265,T16,,,5426914281,T9,,,5325555902,T7,,kaantozlama,5302516415,T19,,bhankin,9178498960385226843409,T12,,,5214494189,T11,,peterpaolo222,1734122559,T18,,,1597954759,T27,,castilian_Crinkly,1043837558,T2,,,a,
# Iterate through all usernames
for username in all_usernames:6995948196,T30,,shambledgroggy,
    pyautogui.moveTo(639, 366, duration=0.2)
    pyautogui.clic7047832646,T17,,,k()

    pyautogui.typewrite(username)
    time.sleep(1)

    pyautogui.click(693, 339)
    time.sleep(1)
1487735306,T10,,,7117937398170945,T22,,Dunks2050,7358897802,T1,,,7303455684,T29,,Paseos_Phrenetically,7259969112,T4,,,7242137483,T24,,WZxmVx,8500,T23,,wXAoex,
    pyautogui.moveTo(727491230464,T26,,AnticalTingler,7441878979,T25,,lzFYry,1, 671, duration=0.2)
    pyautogui.click()
    
    pyautogui.moveTo(771, 502, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(720, 509, duration=0.2)
    pyautogui.click()
    
    processed_usernames.append(username)
    time.sleep(3)

# You can add further actions here for the selected usernames.

# If you want to remove all processed usernames from 'users.txt' in the end:
with open('telegram_contacts.csv', 'w') as file:
    for username in all_usernames:
        if username not in processed_usernames:
            file.write(username + '\n')
