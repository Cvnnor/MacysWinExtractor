## Macy's Win Checker
- A quick python script to check a large amount of wallets and the Macy's NFT they have won.

# How to use:
- Install python 3.9.10 with PIP
- Once installed run the command ```pip install discord_webhook```
- Once installed, add all of the winning wallets to the ```myWallets.txt``` directly from the csv on new lines.
- Now run the script, put your discord webhook as prompted. (this may get rate limited depending on how many you have but it saves to a file anyway)

# Potential Errors:
- PIP not recognised, it probably was not ticked when installing python, run the installer again and make sure to tick INSTALL PIP in the optional settings.
- Python not being recognised, it may not be picking up python when opening the script. Try to open CMD and type ```cd C:\YOURDIRECTORY``` once here type ```python3 checker.py``` if this still does not work double check your python installation by typing ```python``` in cmd. It should return your python version if installed correctly.
