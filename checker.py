import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

classicWallets = list()
rareWallets = list()
ultraRareWallets = list()

classicCount = 0
rareCount = 0
ultraRareCount = 0

discordWebhook = input("Please enter your discord webhook: ")

def saveWallet(wallet, rarity):
    with open(__location__+'/winners.txt', 'a') as f:
        f.write(str(wallet)+" - "+str(rarity)+"\n")
        print("Saved "+str(wallet)+" to file.")

def sendHook(wallet, rarity):
    webhook = DiscordWebhook(url=str(discordWebhook), rate_limit_retry=True)
    embed = DiscordEmbed(title=str(rarity)+" Winner Found!", color=122717, url="https://polygonscan.com/address/"+str(wallet))
    embed.add_embed_field(name="Wallet", value="||"+str(wallet)+"||", inline=False)
    embed.add_embed_field(name="Rarity", value=str(rarity), inline=False)
    if str(rarity) == "Classic":
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/QZW32sOaf249olwK2UOzIeoKA9lQ6gqdEH3BTSzX3K42aJ97yngJGhax7465fP2HUe-flo82heZJRuDa7yvu5QULCiKlue0OUDF6")
    elif str(rarity) == "Rare":
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/2CT2-voZb8OQNDcSgAisJKnF_VvClneAxSdAeEuKSkBCbvD8o_09HqkOZy00ghxBIc_mH9mhdoh3XpRP6O0FZL8AYOT4FetT9Aj07Q")
    elif str(rarity) == "Ultra Rare":
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/mEBM-le8ppE-vkFKH5B7uXfTQBY3Qh5_Yf0mql3XSJ2JmCNtVp7q41O95X_jgFFeTay_fAo8GXcXlm3uOXlCwTIzbZB1e94hlQGE")
    embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/819279757422100491/838377712330211328/giphy.gif",text='Macys Win Checker By Cvnnor#0001')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

with open(__location__+"\classic.txt", "r") as classicList:
    classicList = classicList.readlines()
    for wallet in classicList:
        wallet = str(wallet)
        classicWallets.append(wallet.strip("\n"))

print("Successfully loaded: "+str(len(classicWallets))+" Classic winners")

with open(__location__+"\winnersRare.txt", "r") as rareList:
    rareList = rareList.readlines()
    for wallet in rareList:
        wallet = str(wallet)
        rareWallets.append(wallet.strip("\n"))

print("Successfully loaded: "+str(len(rareWallets))+" Rare winners")

with open(__location__+"\winnersUltraRare.txt", "r") as ultraRare:
    ultraRare = ultraRare.readlines()
    for wallet in ultraRare:
        wallet = str(wallet)
        ultraRareWallets.append(wallet.strip("\n"))

print("Successfully loaded: "+str(len(ultraRareWallets))+" Ultra Rare winners")

with open(__location__+"\myWallets.txt", "r") as userWallets:
    userWallets = userWallets.readlines()
    walletCount = len(userWallets)
    for wallet in userWallets:
        wallet = str(wallet).strip("\n")
        if wallet in classicWallets:
            print("Found Classic Winner: "+str(wallet))
            saveWallet(wallet, "Classic")
            sendHook(wallet, "Classic")
            classicCount += 1
        elif wallet in rareWallets:
            print("Found Rare Winner: "+str(wallet))
            saveWallet(wallet, "Rare")
            sendHook(wallet, "Rare")
            rareCount += 1
        elif wallet in ultraRareWallets:
            print("Found Ultra Rare Winner: "+str(wallet))
            saveWallet(wallet, "Ultra Rare")
            sendHook(wallet, "Ultra Rare")
            ultraRareCount += 1
        else:
            pass
        time.sleep(1)



print("\nSuccessfully checked: "+str(walletCount)+" wallets.\n- Classics: "+str(classicCount)+"\n- Rares: "+str(rareCount)+"\n- Ultra Rares: "+str(ultraRareCount))