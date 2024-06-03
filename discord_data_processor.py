import json
import datetime

print("Make sure to put this file inside the unzipped package folder!\n")
with open("messages/index.json", "r") as f:
    dmlist = {}
    serverlist = {}
    groupchatlist = {}
    index = json.load(f)
    for id, channel in index.items():
        if "in" in channel.split(" "):
            server = " ".join(channel.split(" ")[channel.split(" ").index("in")+1:])
            serverchannel = " ".join(channel.split(" ")[:channel.split(" ").index("in")])
            if server not in serverlist.keys():
                serverlist[server] = {}
            serverlist[server][serverchannel] = id
        elif channel[:14] == "Direct Message":
            dmlist[channel[19:]] = id
        else:
            groupchatlist[channel] = id


channeltype = input("[0] Server \n[1] Direct message \n[2] Groupchat\n \nWhat type of channel: ")
print("\n" * 5)

messagepath = ""
channelpicked = ""

if channeltype == "0":
    choices = {}
    for number, server in enumerate(serverlist.keys()):
        choices[str(number)] = server
    

    print("\n".join([f"[{number}] {server}" for number, server in choices.items()]))
    serverchoice = choices[input("\n Which server: ")]
    print("\n" * 5)


    serverchannelchoices = {}
    for number, serverchannel in enumerate(serverlist[serverchoice].keys()):
        serverchannelchoices[str(number)] = serverchannel
    print("\n".join([f"[{number}] {channel}" for number, channel in serverchannelchoices.items()]))
    channelchoice = serverchannelchoices[input("\n Which channel: ")]

    channelpicked = f"SERVER_{serverchoice}_{channelchoice}"
    messagepath = f"messages/c{serverlist[serverchoice][channelchoice]}/messages.json"


elif channeltype == "1":
    choices = {}
    for number, dm in enumerate(dmlist.keys()):
        choices[str(number)] = dm
    print("\n".join([f"[{number}] {dm}" for number, dm in choices.items()]))
    dmchoice = choices[input("\n Which DM: ")]
    print(dmchoice)
    channelpicked = f"DM_{(dmchoice.split("#")[0])[1:]}"
    messagepath = f"messages/c{dmlist[dmchoice]}/messages.json"


elif channeltype == "2":
    choices = {}
    for number, groupchat in enumerate(groupchatlist.keys()):
        choices[str(number)] = groupchat
    print("\n".join([f"[{number}] {groupchat}" for number, groupchat in choices.items()]))
    groupchatchoice = choices[input("\n Which groupchat: ")]
    channelpicked = f"GROUPCHAT_{groupchatchoice}"
    messagepath = f"messages/c{groupchatlist[groupchatchoice]}/messages.json"


with open (messagepath, "r", encoding='utf-8') as f:
    messages = json.load(f)

processed_path = f"{channelpicked}_{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt"

with open(processed_path, "w", encoding='utf-8') as f:
    for message in messages:
        try:
            f.write(f"{message["Contents"]}\n")
        except:
            pass

print(f"Done!, you can find your file at {processed_path}")

