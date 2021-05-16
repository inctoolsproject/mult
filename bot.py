# -*- coding: utf-8 -*-
from linepy import *
####################################################
from liff.ttypes import *
####################################################
from akad.ttypes import *
####################################################
from datetime import datetime, timedelta
####################################################
from bs4 import BeautifulSoup
####################################################
from humanfriendly import format_timespan, format_size, format_number, format_length
####################################################
from threading import Thread
####################################################
from io import StringIO
####################################################
import multiprocessing
####################################################
from urllib.parse import urlencode
####################################################
from random import randint
####################################################
from time import sleep
####################################################
import matplotlib.pyplot as plt
####################################################
import pandas as pd
####################################################
from gtts import gTTS
####################################################
from googletrans import Translator
####################################################
from Naked.toolshed.shell import execute_js
####################################################
import platform, shutil, socket, time, random, sys, json, codecs, threading, threadpool, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse, timeit, atexit, youtube_dl, pafy, pytz, asyncio, humanize, traceback, ssl, psutil, uvloop
####################################################
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
####################################################
os.system('clear')
####################################################
print("""
████████╗███████╗███████╗████████╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   █████╗  ███████╗   ██║       ██████╔╝██║   ██║   ██║   
   ██║   ██╔══╝  ╚════██║   ██║       ██╔══██╗██║   ██║   ██║   
   ██║   ███████╗███████║   ██║       ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚══════╝╚══════╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ⋙ YTER Test Bot ⚠ Use it at your own risk ⚠
┃ ⋙ It is not recommended to use on the released platform
┃ ⋙ You may no longer be able to use your account normally
┃ ⋙ 「Creator」
┃ ⋙ Create By Light Technology Team
┃ ⋙ Creator : NJL
┃ ⋙ 「Version」
┃ ⋙ Version : 0
┃ ⋙ Last update time : 2021/04/03 (UTC+08)
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
####################################################
cl = LINE("soriyak962@naymeo.com","rahmagila123")
####################################################
clMID = cl.profile.mid
oepoll = OEPoll(cl)
set = {
    "owner": ["u8b9d115e85202db06eb798e8c1b40ae9", "u9be8862cb884bde356d0e41fb6850514"],
    "ccmd": {
        "liffurl": [".liffurl"],
        "time": [".time"],
        "date": [".date"],
        "lasttag": [".lasttag"],
        "logout": [".logout"],
        "oplist": [".oplist"],
        "restart": [".restart"],
        "status": [".status"],
        "findoa": [".findoa"],
        "ttag": [".ttag"],
        "stag": [".stag"],
        "ltag": [".ltag"]
    },
    "lastt": {},
    "aprol": 1
}
set2 = {
    "jg": True,
    "lj": False,
    "lg": True,
    "lr": False,
    "apro": False,
    "protect": True,
    "getmid": False,
    "flwrm": False,
    "debugall": True
}
test = {
    "debug": ["c846fec69c4f52feb32f00cf8970a95bc"],
    "debugbd": "rbd07ffb48c082bab980cfd02be9e3837",
    "2": True
}
if clMID not in set["owner"]:
    set["owner"].append(clMID)
print("Login Success")

def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False


def allowLiff(ChannelId='1655527991'):
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': cl.authToken,
        'X-Line-Application': cl.server.APP_NAME,
        'X-Line-ChannelId': ChannelId,
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)


def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1655527991-3Lbo8OkW', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages": [data]}
    requests.post(url, headers=headers, data=json.dumps(data))


def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type in [5]:
            cl.findAndAddContactsByMid(op.param1)
            cl.sendMention(op.param1, f"thank @! Join me as a friend!\nBot Mid: {clMID}\nYour Mid: {op.param1}", [op.param1])
        elif op.type in [13, 124]:
            if clMID in op.param3:
                if set2["jg"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    group = cl.getGroup(op.param1)
                    cl.sendMention(op.param1, f"Join success\n[Group name] {str(group.name)}\n[Number] {str(len(group.members))}people\n[GID] {str(group.id)}\n[Invr] @!", [op.param2])
            else:
                cl.sendMention(op.param1, "ya @! group inv @!", [op.param2, op.param3])
        elif op.type in [15,128]:
            cl.sendMention(op.param1, "bye @! group out", [op.param2])
        elif op.type in [17,130]:
            cl.sendMention(op.param1, "hi @! group join", [op.param2])
        elif op.type in [19,133]:
            cl.sendMention(op.param1, "oh @! group kick @!", [op.param2, op.param3])
        elif op.type in [22]:
            if clMID in op.param3:
                room = cl.getRoom(op.param1)
                cl.sendMention(op.param1, f"Join success\n[Number] {str(len(room.contacts))}people\n[RID] {str(room.mid)}\n[Invr] @!", [op.param2])
                if set2["lr"]:
                    cl.leaveRoom(op.param1)
            else:
                cl.sendMention(op.param1, "hi @! room join inv by @!", [op.param3, op.param2])
        elif op.type in [24]:
            cl.sendMention(op.param1, "bye @! room out", [op.param2])
        elif op.type in [25, 26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if text is None:
                cmd = ""
            else:
                cmd = text.lower()
            if set2["getmid"] == True:
                if 'u' in cmd:
                    mids_re = re.compile("u[a-z0-9]{32}")
                    mids = mids_re.findall(cmd)
                    targets = []
                    for l in mids:
                        if l not in targets:
                            if ismid(l):
                                targets.append(l)
                    for target in targets:
                        cl.sendContact(to, target)
            if 'MENTION' in msg.contentMetadata.keys() != None:
                mentionees = ast.literal_eval(
                    msg.contentMetadata['MENTION'])['MENTIONEES']
                for mention in mentionees:
                    if clMID in mention["M"]:
                        set["lastt"]["msgid"] = msg_id
                        set["lastt"]["mid"] = sender
                        set["lastt"]["to"] = to
                        set["lastt"]["time"] = datetime.now(tz=pytz.timezone(
                            "Asia/Jakarta")).strftime('%Y/%m/%d %H:%M:%S')
            if set2["lj"] == True:
                if "/ti/g/" in text:
                    link_re = re.compile(
                        '(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        try:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(
                                group.id, ticket_id)
                            cl.relatedMessage(to, "Join success\n[Group name]{}\n[Number]{}人\n[Group URL ID]{}\n[GID]{}".format(
                                str(group.name), str(len(group.members)), str(ticket_id), str(group.id)), msg_id)
                        except Exception as e:
                            if str(e.reason) == "request blocked":
                                cl.relatedMessage(to, "Current account regulation", msg_id)
                            elif "Ticket not found" in str(e.reason):
                                cl.relatedMessage(to, "This URL has been invalidated", msg_id)
                            elif "Prevented join by group ticket" in str(e.reason):
                                cl.relatedMessage(to, "The group does not open the URL to join", msg_id)
                            else:
                                cl.relatedMessage(to, "Income\n"+str(e), msg_id)
                        time.sleep(0.5)
            if msg.contentType == 6:
                timeNow = datetime.now(tz=pytz.timezone("Asia/Jakarta")).strftime('%Y/%m/%d %H:%M:%S')
                b = msg.contentMetadata['GC_EVT_TYPE']
                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                if c == 'AUDIO' and b == "S":
                    arg = "Start call"
                    arg += "\nTypes of: voice"
                    arg += "\nInitiator: @!"
                    arg += f"\nStart time: {timeNow}"
                    cl.replyMention(msg_id, to, arg, [sender])
                if c == 'VIDEO' and b == "S":
                    arg = "Start call"
                    arg += "\nTypes of: Video"
                    arg += "\nInitiator: @!"
                    arg += f"\nStart time: {timeNow}"
                    cl.replyMention(msg_id, to, arg, [sender])
                if c == 'LIVE' and b == "S":
                    arg = "Start call"
                    arg += "\nTypes of: LIVE"
                    arg += "\nInitiator: @!"
                    arg += f"\nStart time: {timeNow}"
                    cl.replyMention(msg_id, to, arg, [sender])
                else:
                    mills = int(msg.contentMetadata["DURATION"])
                    seconds = (mills / 1000) % 60
                    if c == "AUDIO" and b == "E":
                        arg = "End talk"
                        arg += "\nTypes of: voice"
                        arg += "\nInitiator: @!"
                        arg += f"\nEnd Time: {timeNow}"
                        arg += f"\nduration: {seconds} 秒"
                        cl.replyMention(msg_id, to, arg, [sender])
                    if c == "VIDEO" and b == "E":
                        arg = "End talk"
                        arg += "\nTypes of: Video"
                        arg += "\nInitiator: @!"
                        arg += f"\nEnd Time: {timeNow}"
                        arg += f"\nduration: {seconds} 秒"
                        cl.replyMention(msg_id, to, arg, [sender])
                    if c == "LIVE" and b == "E":
                        arg = "End talk"
                        arg += "\nTypes of: LIVE"
                        arg += "\nInitiator: @!"
                        arg += f"\nEnd Time: {timeNow}"
                        arg += f"\nduration: {seconds} second"
                        cl.replyMention(msg_id, to, arg, [sender])
            if sender in set["owner"]:
                if cmd in ['help', 'allcmd', 'cmds', '幫助', '指令表', '指令']:
                    ret_ = "[General instruction]"
                    for a in set['ccmd']:
                        ret_ += "\n{}(key:{})".format(set['ccmd'][a], a)
                    ret_ += "\n\n[Other instructions]\n[Retrieve message]\nun:number\n[Permission adjustment]\nop:(@/mid)s\n[Switch function method]\nset:function name\n[Customary command method]\n+)ccmd:key:cmd\n-)dcmd:cmd"
                    cl.relatedMessage(to, ret_, msg_id)
                elif cmd == 'test1':
                    uda = cl.getContact(sender)
                    if uda.pictureStatus is None:
                        uda0 = "not"
                        uda1 = "https://upload.cc/i1/2021/02/11/b0PkA1.png"
                    else:
                        uda0 = "Already"
                        uda1 = "https://obs.line-scdn.net/" + uda.pictureStatus
                    if uda.videoProfile is None:
                        uda2 = "not"
                    else:
                        uda2 = "Already"
                    if uda.musicProfile is None:
                        uda3 = "not"
                    else:
                        uda3 = "Already"
                    if uda.createdTime == 0:
                        uda4 = "not"
                        uda5 = "No friends have already added"
                    else:
                        uda4 = "Already"
                        uda5 = time.strftime(
                            "%Y/%m/%d %H:%M:%S", time.localtime(int(uda.createdTime) / 1000))
                    if uda.favoriteTime == 0:
                        uda6 = "not"
                        uda7 = "Have not joined"
                    else:
                        uda6 = "Already"
                        uda7 = time.strftime(
                            "%Y/%m/%d %H:%M:%S", time.localtime(int(uda.favoriteTime) / 1000))
                    if sender in set["owner"]:
                        uda8 = "Have"
                        uda9 = "Not"
                    else:
                        uda8 = "No"
                        uda9 = "Yes"
                    gidsl = []
                    for id in cl.getGroupIdsJoined():
                        if sender in [contact.mid for contact in cl.getGroup(id).members]:
                            gidsl.append(id)
                    uda10 = str(len(gidsl))
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {
                            "type": "carousel",
                            "contents": [
                                {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/60dAA9r.jpg",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "3:5",
                                                "gravity": "top"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                                    {
                                                                        "type": "image",
                                                                        "url": "{}".format(uda1),
                                                                        "size": "full",
                                                                        "aspectMode": "cover"
                                                                    }
                                                                ],
                                                                "width": "100px",
                                                                "height": "100px",
                                                                "cornerRadius": "100px"
                                                            }
                                                        ],
                                                        "width": "100%",
                                                        "justifyContent": "center"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "separator",
                                                                "margin": "lg",
                                                                "color": "#2894FF"
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "User information-Basic",
                                                                "size": "xl",
                                                                "color": "#ffffff",
                                                                "weight": "bold",
                                                                "align": "center",
                                                                "margin": "md"
                                                            },
                                                            {
                                                                "type": "separator",
                                                                "margin": "sm",
                                                                "color": "#2894FF"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "name",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "　{}".format(uda.displayName),
                                                                        "wrap": True
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "name",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "　{}".format(uda.displayNameOverridden),
                                                                        "wrap": True
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Signature number",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}".format(str(len(uda.statusMessage))),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Static head sticker",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Mount".format(uda0),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Dynamic head stickers",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Mount".format(uda2),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Background music state",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Mount".format(uda3),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            }
                                                        ],
                                                        "margin": "lg"
                                                    }
                                                ],
                                                "position": "absolute",
                                                "offsetBottom": "0px",
                                                                "offsetStart": "0px",
                                                                "offsetEnd": "0px",
                                                                "backgroundColor": "#BEBEBEaa",
                                                                "paddingAll": "20px",
                                                                "paddingTop": "18px",
                                                                "offsetTop": "0px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "filler"
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "baseline",
                                                                "contents": [
                                                                    {
                                                                        "type": "filler"
                                                                    },
                                                                    {
                                                                        "type": "icon",
                                                                        "url": "https://i.ibb.co/0Jc95vm/3032276.png"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Friend directly",
                                                                        "color": "#FF0000",
                                                                        "flex": 0,
                                                                        "offsetTop": "-2px",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "filler"
                                                                    }
                                                                ],
                                                                "spacing": "sm"
                                                            },
                                                            {
                                                                "type": "filler"
                                                            }
                                                        ],
                                                        "borderWidth": "1px",
                                                        "cornerRadius": "4px",
                                                                        "spacing": "sm",
                                                                        "borderColor": "#2894FF",
                                                                        "margin": "xxl",
                                                                        "height": "40px",
                                                                        "backgroundColor": "#9D9D9Daa",
                                                                        "action": {
                                                                            "type": "uri",
                                                                            "uri": "line://nv/profilePopup/mid={}".format(sender)
                                                        }
                                                    }
                                                ],
                                                "position": "absolute",
                                                "offsetBottom": "0px",
                                                                "paddingAll": "20px",
                                                                "offsetStart": "0px",
                                                                "offsetEnd": "0px"
                                            }
                                        ],
                                        "paddingAll": "0px"
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.imgur.com/oscMAJd.jpg",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "3:5",
                                                "gravity": "top"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "separator",
                                                                "margin": "lg",
                                                                "color": "#2894FF"
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "User information-Advancement",
                                                                "size": "xl",
                                                                "color": "#ffffff",
                                                                "weight": "bold",
                                                                "align": "center",
                                                                "margin": "md"
                                                            },
                                                            {
                                                                "type": "separator",
                                                                "margin": "sm",
                                                                "color": "#2894FF"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Friend status",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Join".format(uda4),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Join your friends",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}".format(uda5)
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Favorite state",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Join".format(uda6),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Join the favorite time",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}".format(uda7)
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Authority status",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Authority".format(uda8),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Black single status",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}Black single".format(uda9),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "type": "box",
                                                                "layout": "horizontal",
                                                                "contents": [
                                                                    {
                                                                        "type": "text",
                                                                        "text": "Common group quantity",
                                                                        "weight": "bold"
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "{}".format(uda10),
                                                                        "align": "end"
                                                                    }
                                                                ]
                                                            }
                                                        ],
                                                        "margin": "lg"
                                                    }
                                                ],
                                                "position": "absolute",
                                                "offsetBottom": "0px",
                                                                "offsetStart": "0px",
                                                                "offsetEnd": "0px",
                                                                "backgroundColor": "#BEBEBEaa",
                                                                "paddingAll": "20px",
                                                                "paddingTop": "18px",
                                                                "offsetTop": "0px"
                                            }
                                        ],
                                        "paddingAll": "0px"
                                    }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, dat)
                elif cmd == 'test2':
                    if test["2"] == True:
                        urii = "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg"
                        urit = "line://app/1655527991-3Lbo8OkW?type=text&text=I want to close"
                    else:
                        urii = "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg"
                        urit = "line://app/1655527991-3Lbo8OkW?type=text&text=I want to open"
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Group intelligence",
                                        "weight": "bold",
                                        "size": "xl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "BAO?",
                                                "gravity": "center"
                                            },
                                            {
                                                "type": "image",
                                                "url": urii,
                                                "action": {
                                                    "type": "uri",
                                                    "uri": urit
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                    sendTemplate(to, dat)
                elif cmd == 'I want to open':
                    test["2"] = True
                    cl.relatedMessage(to, "ok\nTrue", msg_id)
                elif cmd == 'I want to close':
                    test["2"] = False
                    cl.relatedMessage(to, "ok\nFalse", msg_id)
                elif cmd == 'test3':
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Payment notice",
                                        "weight": "bold",
                                        "color": "#1DB446",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "Payment",
                                        "weight": "bold",
                                        "size": "xxl",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "xxl",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Permanent semi-scale",
                                                        "size": "sm",
                                                        "color": "#555555",
                                                        "flex": 0
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "x 1",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "$0",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "margin": "xxl",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Quantity",
                                                        "size": "sm",
                                                        "color": "#555555"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "1",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "total",
                                                        "size": "sm",
                                                        "color": "#555555"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "$0",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "payment method:cash",
                                                        "size": "sm",
                                                        "color": "#555555"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "$0",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Zero",
                                                        "size": "sm",
                                                        "color": "#555555"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "$0",
                                                        "size": "sm",
                                                        "color": "#111111",
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Order number",
                                                "size": "xs",
                                                "color": "#aaaaaa",
                                                "flex": 0
                                            },
                                            {
                                                "type": "text",
                                                "text": "#0000000000",
                                                "color": "#aaaaaa",
                                                "size": "xs",
                                                "align": "end"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "styles": {
                                "footer": {
                                    "separator": True
                                }
                            }
                        }
                    }
                    sendTemplate(to, dat)
                elif cmd == 'test4':
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "uri": "http://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Brown Cafe",
                                        "weight": "bold",
                                        "size": "xl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "size": "sm",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                            },
                                            {
                                                "type": "icon",
                                                "size": "sm",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                            },
                                            {
                                                "type": "icon",
                                                "size": "sm",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                            },
                                            {
                                                "type": "icon",
                                                "size": "sm",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                            },
                                            {
                                                "type": "icon",
                                                "size": "sm",
                                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "4.0",
                                                "size": "sm",
                                                "color": "#999999",
                                                "margin": "md",
                                                "flex": 0
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "lg",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Place",
                                                        "color": "#aaaaaa",
                                                        "size": "sm",
                                                        "flex": 1
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                        "wrap": True,
                                                        "color": "#666666",
                                                        "size": "sm",
                                                        "flex": 5
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Time",
                                                        "color": "#aaaaaa",
                                                        "size": "sm",
                                                        "flex": 1
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "10:00 - 23:00",
                                                        "wrap": True,
                                                        "color": "#666666",
                                                        "size": "sm",
                                                        "flex": 5
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "style": "link",
                                        "height": "sm",
                                        "action": {
                                            "type": "uri",
                                            "label": "CALL",
                                            "uri": "https://linecorp.com"
                                        }
                                    },
                                    {
                                        "type": "button",
                                        "style": "link",
                                        "height": "sm",
                                        "action": {
                                            "type": "uri",
                                            "label": "WEBSITE",
                                            "uri": "https://linecorp.com"
                                        }
                                    },
                                    None,
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    },
                                ],
                                "flex": 0
                            }
                        }
                    }
                    sendTemplate(to, dat)
                elif cmd == 'test5':
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {"type": "carousel", "contents": [{"type": "bubble", "header": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "作者 - 資訊", "wrap": True, "color": "#9023FF"}]}, "hero": {"type": "image", "url": "https://i.imgur.com/zgu5fcI.jpg", "size": "full", "aspectMode": "cover", "aspectRatio": "5:3"}, "body": {"type": "box", "layout": "vertical", "spacing": "sm", "contents": [{"type": "text", "text": "管理人：\U00100302\U00100140H⃣⃝a⃝r⃝u⃝  S⃣⃝a⃝K", "wrap": True, "margin": "sm", "maxLines": 0, "size": "md", "color": "#ffffff"}]}, "footer": {"type": "box", "layout": "vertical", "contents": [{"type": "button", "style": "primary", "color": "#00bfff", "action": {"type": "uri", "label": "加作者好友", "uri": "line://ti/p/aDtv2LTeKS"}}, {"type": "separator", "margin": "md", "color": "#fe8cb7"}, {"type": "button", "style": "primary", "color": "#00bfff", "action": {"type": "uri", "label": "前端網站", "uri": "https://bot.harusakura.cc"}}, {"type": "separator", "margin": "md", "color": "#fe8cb7"}, {"type": "button", "style": "primary", "color": "#00bfff", "action": {"type": "uri", "label": "匿名留言", "uri": "https://harusakura.cc/whisper"}}]}, "styles": {"header": {"backgroundColor": "#fe8cb7"}, "hero": {"backgroundColor": "#fe8cb7"}, "body": {"backgroundColor": "#fe8cb7"}, "footer": {"backgroundColor": "#fe8cb7"}}}]}
                    }
                    sendTemplate(to, dat)
                elif cmd == 'test6':
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {}
                    }
                    sendTemplate(to, dat)
                elif cmd == 'test7':
                    dat = {
                        "type": "flex",
                        "altText": "BAO?",
                        "contents": {}
                    }
                    sendTemplate(to, dat)
                elif cmd.startswith('ud'):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        targets = []
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        for x in MENTION["MENTIONEES"]:
                            if x["M"] not in targets:
                                targets.append(x["M"])
                        for target in targets:
                            cl.relatedMessage(
                                to, str(cl.getContact(target)), msg_id)
                elif cmd.startswith("cmd:"):
                    txt = text[4:]
                    try:
                        exec(str(txt))
                        print('\n===caveat===\nSpecial instructions\ninstruction:cmd\nTrigger text:{}\nuser:{}\nposition:{}\n===the end===\n'.format(
                            text, sender, to))
                    except Exception as e:
                        cl.relatedMessage(to, "Execute command error\n"+str(e), msg_id)
                elif cmd == 'cra':
                    a = cl.getChatRoomAnnouncements(to)
                    if a == []:
                        cl.relatedMessage(to, "Can't find", msg_id)
                    else:
                        for b in a:
                            c = b.contents
                            d = c.link
                            e = c.text
                            cl.replyMention(
                                msg_id, to, '[Announcement]\ncontent:{}\nBulletin:@!\nlink:{}'.format(e, d), [b.creatorMid])
                elif cmd.startswith("cra:"):
                    a = text[4:]
                    b = ChatRoomAnnouncementContents()
                    b.displayFields = 5
                    b.text = a
                    b.link = "line://nv/chatMsg?chatId={}&messageId={}".format(
                        to, msg_id)
                    cl.createChatRoomAnnouncement(to, 0, b)
                    cl.relatedMessage(to, "success\ncontent:{}".format(a), msg_id)
                elif cmd == "ccra":
                    a = cl.getChatRoomAnnouncements(to)
                    if a == []:
                        cl.relatedMessage(to, "Can't find", msg_id)
                    else:
                        for b in a:
                            cl.removeChatRoomAnnouncement(
                                to, b.announcementSeq)
                        cl.relatedMessage(to, "carry out", msg_id)
                elif cmd == "Pumper":
                    paths = []
                    for picpaths in os.walk('./images'):
                        paths.append(picpaths)
                    sample = random.choice(paths)
                    #cl.sendReplyMessage(msg.id, to, "Selected file:"+sample)
                    #print("\n\nSelected file: "+ Sample +" \ n \ n ")
                    Cl.sendImage (to, SAMPle[0]+"/"+random.choice(sample[2]))
                elif cmd == "Sis":
                    meizi = sum(len(files) for _, _, files in os.walk('./images'))
                    cl.relatedMessage(to, str(meizi), msg_id)
                elif cmd == "Sister":
                    fileDir = r"./images"
                    fileExt = r".jpg"
                    w = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
                    q = 0
                    cl.relatedMessage(to, "removing...", msg_id)
                    for x in w:
                        q += 1
                        os.remove("./images/"+x)
                    cl.relatedMessage(to, f"ok\ndelete {q} pic", msg_id)
                elif cmd in set['ccmd']['liffurl']:
                    cl.relatedMessage(
                        to, "https://liff.line.me/1655527991-3Lbo8OkW", msg_id)
                elif cmd in set['ccmd']['time']:
                    cl.relatedMessage(to, datetime.now(tz=pytz.timezone(
                        "Asia/Jakarta")).strftime('%H:%M:%S'), msg_id)
                elif cmd in set['ccmd']['date']:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday",
                           "Wednesday", "Thursday", "Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]:
                            hasil = hari[i]
                    readTime = timeNow.strftime(
                        '%Y') + "/" + bln + "/" + timeNow.strftime('%d') + " " + hasil
                    cl.relatedMessage(to, readTime, msg_id)
                elif cmd in set['ccmd']['lasttag']:
                    if set["lastt"] == {}:
                        cl.relatedMessage(to, "Can't find a label message", msg_id)
                    else:
                        cl.relatedMessage(to, "Caller:{}({})\ntime:{}\nposition:{}".format(cl.getContact(
                            set["lastt"]["mid"]).displayName, set["lastt"]["mid"], set["lastt"]["time"], set["lastt"]["to"]), set["lastt"]["msgid"])
                elif cmd in set['ccmd']['logout']:
                    cl.relatedMessage(to, "Will automatically log out the machine", msg_id)
                    cl.relatedMessage(to, "[prompt]\nAlready automatically logged out of the background server", msg_id)
                    os._exit(0)
                elif cmd in set['ccmd']['oplist']:
                    if set["owner"] == []:
                        cl.relatedMessage(to, "No permission", msg_id)
                    else:
                        mc = "[Permissions list]"
                        arr = []
                        mention = "@YTER "
                        for mi_d in set["owner"]:
                            mc += "\n➲"
                            slen = str(len(mc))
                            elen = str(len(mc) + len(mention) - 1)
                            arrData = {'S': slen, 'E': elen, 'M': mi_d}
                            arr.append(arrData)
                            mc += mention
                        cl.sendReplyMessage(msg_id, to, mc+"\n[the end]", contentMetadata={
                                            'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, contentType=0)
                elif cmd in set['ccmd']['restart']:
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                elif cmd in set['ccmd']['status']:
                    try:
                        cl.kickoutFromGroup(msg.to, ["test"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "Regulation"
                        else:
                            aa = "Can be implemented"
                    try:
                        cl.inviteIntoGroup(msg.to, ["test"])
                        bb = "Can be implemented"
                    except:
                        bb = "Regulation"
                    try:
                        cl.findAndAddContactsByMid("test")
                    except Exception as e:
                        if e.reason == "request blocked":
                            cc = "Regulation"
                        else:
                            cc = "Can be implemented"
                    try:
                        cl.acceptGroupInvitationByTicket("test", "test")
                    except Exception as e:
                        if e.reason == "request blocked":
                            dd = "Regulation"
                        else:
                            dd = "Can be implemented"
                    cl.relatedMessage(to, "ΞΞΞΞΞ〘Machine status query〙ΞΞΞΞΞ\n※Kick:" + str(aa) + "\n※Invitation status:" + str(
                        bb) + "\n※Cancel state:Can be implemented\n※Advance:" + str(cc) + "\n※URL status:" + str(dd), msg_id)
                elif cmd in set['ccmd']['findoa']:
                    oas = "[Nonmittent]"
                    if msg.toType == 1:
                        room = cl.getRoom(to)
                        for contact in room.contacts:
                            if contact.capableBuddy:
                                oas += "\n{}\n{}".format(cl.getContact(
                                    contact.mid).displayName, contact.mid)
                        if oas == "[Nonmittent]":
                            cl.relatedMessage(to, "Can't find", msg_id)
                        else:
                            cl.relatedMessage(to, oas, msg_id)
                    elif msg.toType == 2:
                        group = cl.getGroup(to)
                        for contact in group.members:
                            if contact.capableBuddy:
                                oas += "{}\n{}".format(cl.getContact(
                                    contact.mid).displayName, contact.mid)
                        if oas == "[Nonmittent]":
                            cl.relatedMessage(to, "Can't find", msg_id)
                        else:
                            cl.relatedMessage(to, oas, msg_id)
                elif cmd in set['ccmd']['ttag']:
                    if msg.toType == 1:
                        room = cl.getRoom(to)
                        nama = [contact.mid for contact in room.contacts]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in room.contacts[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendReplyMessage(msg_id, to, text=txt, contentMetadata={
                                                u'MENTION': json.dumps({'MENTIONEES': b})}, contentType=0)
                    elif msg.toType == 2:
                        group = cl.getGroup(to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in group.members[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendReplyMessage(msg_id, to, text=txt, contentMetadata={
                                                u'MENTION': json.dumps({'MENTIONEES': b})}, contentType=0)
                elif cmd in set['ccmd']['stag']:
                    if msg.toType == 1:
                        room = cl.getRoom(to)
                        nama = [contact.mid for contact in room.contacts]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in room.contacts[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendReplyMessage(msg_id, to, txt, {'STKVER': '100', 'STKID': str(
                                a+1), 'STKPKGID': '1', u'MENTION': json.dumps({'MENTIONEES': b})}, 7)
                    elif msg.toType == 2:
                        group = cl.getGroup(to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in group.members[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendReplyMessage(msg_id, to, txt, {'STKVER': '100', 'STKID': str(
                                a+1), 'STKPKGID': '1', u'MENTION': json.dumps({'MENTIONEES': b})}, 7)
                elif cmd in set['ccmd']['ltag']:
                    if msg.toType == 1:
                        room = cl.getRoom(to)
                        nama = [contact.mid for contact in room.contacts]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in room.contacts[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendTagLocation(
                                to, txt, {u'MENTION': json.dumps({'MENTIONEES': b})})
                    elif msg.toType == 2:
                        group = cl.getGroup(to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//21
                        for a in range(k+1):
                            txt = u''
                            s = 0
                            b = []
                            for i in group.members[a*20: (a+1)*20]:
                                b.append(
                                    {"S": str(s), "E": str(s+6), "M": i.mid})
                                s += 7
                                txt += u'@YTER \n'
                            cl.sendTagLocation(
                                to, txt, {u'MENTION': json.dumps({'MENTIONEES': b})})
                elif cmd.startswith('un:'):
                    try:
                        mes = int(cmd[3:])
                    except:
                        mes = 1
                    M = cl.getRecentMessagesV2(to, 1001)
                    MId = []
                    for ind, i in enumerate(M):
                        if ind == 0:
                            pass
                        else:
                            if i._from == clMID:
                                MId.append(i.id)
                                if len(MId) == mes:
                                    break
                    for i in MId:
                        try:
                            cl.unsendMessage(i)
                        except:
                            pass
                elif cmd.startswith("set:"):
                    a = cmd[4:]
                    if a == 'all':
                        b = "[All settings]"
                        for c in set2:
                            b += "\n{}:{}".format(c, str(set2[c]))
                        cl.relatedMessage(to, b, msg_id)
                    elif a == 'all on':
                        for b in set2:
                            set2[b] = True
                        cl.relatedMessage(to, "success\nAll:True", msg_id)
                    elif a == 'all off':
                        for b in set2:
                            set2[b] = False
                        cl.relatedMessage(to, "success\nAll:False", msg_id)
                    elif a in set2:
                        if set2[a] == True:
                            set2[a] = False
                            cl.relatedMessage(
                                to, "success\n{}:False".format(a), msg_id)
                        else:
                            set2[a] = True
                            cl.relatedMessage(
                                to, "success\n{}:True".format(a), msg_id)
                elif cmd.startswith("debugadd:"):
                    x = cmd[9:]
                    if x in test["debug"]:
                        cl.relatedMessage(
                            to, f"{x} already in", msg_id)
                    else:
                        test["debug"].append(x)
                        cl.relatedMessage(
                            to, f"okay\nadd {x}", msg_id)
                elif cmd.startswith("ccmd:"):
                    a = cmd.split(":")
                    if len(a) == 3 and a[1] != "" and a[2] != "":
                        if a[1] in set['ccmd']:
                            for b in set['ccmd']:
                                if a[2] in set['ccmd'][b]:
                                    cl.relatedMessage(
                                        to, "Overlap\nkey:{}\ncmd:{}".format(b, a[2]), msg_id)
                                    return
                                elif a[2] in ['help', 'allcmd', 'cmds', '幫助', '指令表', '指令', 'cmd', 'un', 'set', 'ccmd', 'dcmd', 'op', 'cra', 'ccra', 'test1', 'test2', 'debugadd', 'test3', 'test4', 'test5', 'test6']:
                                    cl.relatedMessage(
                                        to, "Instructions are not legal\ncmd:{}".format(a[2]), msg_id)
                                    return
                            set['ccmd'][a[1]].append(a[2])
                            cl.relatedMessage(
                                to, "New customization\nkey:{}\ncmd:{}".format(a[1], a[2]), msg_id)
                elif cmd.startswith("dcmd:"):
                    a = cmd[5:]
                    if a != "":
                        for b in set['ccmd']:
                            if a in set['ccmd'][b]:
                                set['ccmd'][b].remove(a)
                                cl.relatedMessage(
                                    to, "Delete Custom Customs Directive\nkey:{}\ncmd:{}".format(b, a), msg_id)
                                break
                elif cmd.startswith("op:"):
                    mids_re = re.compile("u[a-z0-9]{32}")
                    mids = mids_re.findall(cmd)
                    targets = []
                    for l in mids:
                        if l not in targets:
                            if ismid(l):
                                targets.append(l)
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        for x in MENTION["MENTIONEES"]:
                            if x["M"] not in targets:
                                targets.append(x["M"])
                    for target in targets:
                        if target in set["owner"]:
                            set["owner"].remove(target)
                        else:
                            set["owner"].append(target)
                    cl.relatedMessage(to, "Permission adjustment", msg_id)
        elif op.type in [32,126]:
            cl.sendMention(op.param1, "oh @! group cancel inv @!", [op.param2, op.param3])
        elif op.type in [60]:
            pass
        elif op.param1 in test["debug"] or set2["debugall"]:
            if op.type in OpType._VALUES_TO_NAMES:
                print(
                    f"[ {str(op.type)} ]{OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')}")
            else:
                print(f"[ {str(op.type)} ]UNKNOWN")
            print(op)
    except Exception as e:
        # print(e)
        error_class = e.__class__.__name__  # Number of error
        detail = e.args[0]  # Details
        cal, exc, tb = sys.exc_info()  # Obtain Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1]  # Obtain Call Stack Last information
        fileName = lastCallStack[0]  # A file name acquired
        lineNum = lastCallStack[1]  # Take the line number
        funcName = lastCallStack[2]  # Get the name of the function
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(
            fileName, lineNum, funcName, error_class, detail)
        print(errMsg)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=lineBot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
