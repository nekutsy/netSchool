import requests
import js2py
import json
import datetime
import html2text
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import threading
import os
import docx2pdf
import pdf2image
import configparser
from inspect import getsourcefile
from os.path import abspath

headers = {
    "Referer":"https://net-school.cap.ru/"
}
    
jsCode = 'function safe_add(n,t){var i=(n&65535)+(t&65535),r=(n>>16)+(t>>16)+(i>>16);return r<<16|i&65535} function rol(n,t){return n<<t|n>>>32-t} function cmn(n,t,i,r,u,f){return safe_add(rol(safe_add(safe_add(t,n),safe_add(r,f)),u),i)} function ff(n,t,i,r,u,f,e){return cmn(t&i|~t&r,n,t,u,f,e)} function gg(n,t,i,r,u,f,e){return cmn(t&r|i&~r,n,t,u,f,e)} function hh(n,t,i,r,u,f,e){return cmn(t^i^r,n,t,u,f,e)} function ii(n,t,i,r,u,f,e){return cmn(i^(t|~r),n,t,u,f,e)} function coreMD5(n){var t=1732584193,r=-271733879,u=-1732584194,f=271733878;for(i=0;i<n.length;i+=16){var e=t,o=r,s=u,h=f;t=ff(t,r,u,f,n[i+0],7,-680876936);f=ff(f,t,r,u,n[i+1],12,-389564586);u=ff(u,f,t,r,n[i+2],17,606105819);r=ff(r,u,f,t,n[i+3],22,-1044525330);t=ff(t,r,u,f,n[i+4],7,-176418897);f=ff(f,t,r,u,n[i+5],12,1200080426);u=ff(u,f,t,r,n[i+6],17,-1473231341);r=ff(r,u,f,t,n[i+7],22,-45705983);t=ff(t,r,u,f,n[i+8],7,1770035416);f=ff(f,t,r,u,n[i+9],12,-1958414417);u=ff(u,f,t,r,n[i+10],17,-42063);r=ff(r,u,f,t,n[i+11],22,-1990404162);t=ff(t,r,u,f,n[i+12],7,1804603682);f=ff(f,t,r,u,n[i+13],12,-40341101);u=ff(u,f,t,r,n[i+14],17,-1502002290);r=ff(r,u,f,t,n[i+15],22,1236535329);t=gg(t,r,u,f,n[i+1],5,-165796510);f=gg(f,t,r,u,n[i+6],9,-1069501632);u=gg(u,f,t,r,n[i+11],14,643717713);r=gg(r,u,f,t,n[i+0],20,-373897302);t=gg(t,r,u,f,n[i+5],5,-701558691);f=gg(f,t,r,u,n[i+10],9,38016083);u=gg(u,f,t,r,n[i+15],14,-660478335);r=gg(r,u,f,t,n[i+4],20,-405537848);t=gg(t,r,u,f,n[i+9],5,568446438);f=gg(f,t,r,u,n[i+14],9,-1019803690);u=gg(u,f,t,r,n[i+3],14,-187363961);r=gg(r,u,f,t,n[i+8],20,1163531501);t=gg(t,r,u,f,n[i+13],5,-1444681467);f=gg(f,t,r,u,n[i+2],9,-51403784);u=gg(u,f,t,r,n[i+7],14,1735328473);r=gg(r,u,f,t,n[i+12],20,-1926607734);t=hh(t,r,u,f,n[i+5],4,-378558);f=hh(f,t,r,u,n[i+8],11,-2022574463);u=hh(u,f,t,r,n[i+11],16,1839030562);r=hh(r,u,f,t,n[i+14],23,-35309556);t=hh(t,r,u,f,n[i+1],4,-1530992060);f=hh(f,t,r,u,n[i+4],11,1272893353);u=hh(u,f,t,r,n[i+7],16,-155497632);r=hh(r,u,f,t,n[i+10],23,-1094730640);t=hh(t,r,u,f,n[i+13],4,681279174);f=hh(f,t,r,u,n[i+0],11,-358537222);u=hh(u,f,t,r,n[i+3],16,-722521979);r=hh(r,u,f,t,n[i+6],23,76029189);t=hh(t,r,u,f,n[i+9],4,-640364487);f=hh(f,t,r,u,n[i+12],11,-421815835);u=hh(u,f,t,r,n[i+15],16,530742520);r=hh(r,u,f,t,n[i+2],23,-995338651);t=ii(t,r,u,f,n[i+0],6,-198630844);f=ii(f,t,r,u,n[i+7],10,1126891415);u=ii(u,f,t,r,n[i+14],15,-1416354905);r=ii(r,u,f,t,n[i+5],21,-57434055);t=ii(t,r,u,f,n[i+12],6,1700485571);f=ii(f,t,r,u,n[i+3],10,-1894986606);u=ii(u,f,t,r,n[i+10],15,-1051523);r=ii(r,u,f,t,n[i+1],21,-2054922799);t=ii(t,r,u,f,n[i+8],6,1873313359);f=ii(f,t,r,u,n[i+15],10,-30611744);u=ii(u,f,t,r,n[i+6],15,-1560198380);r=ii(r,u,f,t,n[i+13],21,1309151649);t=ii(t,r,u,f,n[i+4],6,-145523070);f=ii(f,t,r,u,n[i+11],10,-1120210379);u=ii(u,f,t,r,n[i+2],15,718787259);r=ii(r,u,f,t,n[i+9],21,-343485551);t=safe_add(t,e);r=safe_add(r,o);u=safe_add(u,s);f=safe_add(f,h)}return[t,r,u,f]} function binl2hex(n){for(var i="0123456789abcdef",r="",t=0;t<n.length*4;t++)r+=i.charAt(n[t>>2]>>t%4*8+4&15)+i.charAt(n[t>>2]>>t%4*8&15);return r} function charCodeAt_(n,t){var i=n.charCodeAt(t);return i>=0&&i<=255?i:i>=1040&&i<=1103?i-848:i==1025?168:i==1105?184:i==8470?185:0} function str2binl_(n){for(var r=(n.length+8>>6)+1,i=new Array(r*16),t=0;t<r*16;t++)i[t]=0;for(t=0;t<n.length;t++)i[t>>2]|=(charCodeAt_(n,t)&255)<<t%4*8;return i[t>>2]|=128<<t%4*8,i[r*16-2]=n.length*8,i} function hexMD5_(n){return binl2hex(coreMD5(str2binl_(n)))}'
jsFunc = js2py.eval_js(jsCode)

session = requests.session()
session.headers=headers

groupId = 0
groupToken = ""
accessToken = ""
delay = 0
password = ""
userName = ""
studentId = ""
vers = ""
dataPath = ""

lt = None
ver = None
salt = None
at = None



#init
def createConfig(path):
    config = configparser.ConfigParser()
    config.add_section("netSchool")
    config.set("netSchool", "password", "")
    config.set("netSchool", "userName", "")
    config.set("netSchool", "userId", "")
    config.set("netSchool", "vers", "")
    
    config.add_section("vk")
    config.set("vk", "groupToken", "")
    config.set("vk", "accessToken", "")
    config.set("vk", "groupId", "")

    config.add_section("main")
    config.set("main", "delay", "")
    config.set("main", "path", "")

    with open(path, "w") as config_file:
        config.write(config_file)

def createData():
    open(dataPath + "/shownNews.txt", "w+")
    os.mkdir(dataPath + "/tmp")

#alg
def sep(l, sep=";"):
    if len(l) == 1:
        return str(l[0])
    if len(l) == 0:
        return ""
    res = ""
    for i in l[:-1]:
        res += str(i) + sep
    return res + str(l[-1])

def isWebsiteExist(url):
    try:
        requests.get(url)
        return True
    except:
        return False

#netschool
def login():
    pre = str(isOnline())
    global session, lt, ver, salt, at
    r = session.post("https://net-school.cap.ru/webapi/auth/getdata")
    rc = json.loads(r.text)
    lt = rc.get("lt")
    ver = rc.get("ver")
    salt = rc.get("salt")
    p2 = {"LoginType":"1",
        "cid": "2",
        "sid": "21",
        "pid": "-449",
        "cn": "449",
        "sft": "2",
        "scid": "494",
        "UN": userName,
        "PW": jsFunc(salt+jsFunc(password))[:15],
        "lt": lt,
        "pw2": jsFunc(salt+jsFunc(password)),
        "ver": ver,
    }
    r = session.post("https://net-school.cap.ru/webapi/login", data=p2)
    rc = json.loads(r.text)
    at = rc.get("at")
    print("login called (isOnline: " + pre + "->" + str(isOnline()) + ")")

def logout():
    pre = str(isOnline())
    p = {
        "at": at,
        "VER": ver
    }
    session.post("https://net-school.cap.ru/asp/logout.asp", data = p)
    print("logout called (isOnline: " + pre + "->" + str(isOnline()) + ")")

def isOnline():
    p = { "At": at }
    r = session.get("https://net-school.cap.ru/webapi/reports", data=p)
    if r.status_code == 200:
        return True
    return False

def getFood(date: datetime.date):
    url = "http://cheblyceum2.ru/upload/goryachee_pitanie/" + date.strftime('%d.%m.%Y').replace("-", ".") + ".PDF"
    r = requests.get(url=url)
    open(dataPath + "/food/pdf.pdf", "wb").write(r.content)

def getDiary(start, end):
    p = {
        "At": at
    }
    params = { 
        "studentId": studentId,
        "vers": vers,
        "weekEnd": end,
        "weekStart": start,
        "withLaAssigns": "false",
        "yearId": "148662"
    }
    r = session.get("https://net-school.cap.ru/webapi/student/diary", params=params, data=p)
    rj = json.loads(r.text)
    return rj

def diary2text(diary, showMark=True, showMarkReason=False, showText=True, verbose=False):
    out = ""
    if diary.get("weekDays") == None:
        return str(diary[:100] + "...")
    for i in diary.get("weekDays"):
        date = i.get("date")[:10]
        intDay = datetime.date(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:])).weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        day = [date + " (" + days[intDay] + ")"]
        for j in i.get("lessons"):
            assignments = j.get("assignments")
            name = j.get("subjectName")
            text = []
            mark = []
            markReason = []
            if assignments != None:
                for k in assignments:
                    mk = k.get("mark")
                    if mk != None:
                        mark.append(mk.get("mark"))
                        markReason.append(k.get("assignmentName"))
                    else:
                        text.append(k.get("assignmentName"))

            line = ""
            if showText == True and len(text) != 0:
                line = line + " " + sep(text,",") + ";"
            if showMark == True and len(mark) != 0:
                line = line + " " + sep(mark,",") + ";"
            if showMarkReason == True and len(markReason) != 0:
                line = line + " " + sep(markReason,",") + ";"
            
            if line != "":
                line = name + ":" + line[:-1]
            elif verbose == True:
                line = name
            
            if line != "":
                day.append(line)
        out = out + "\n\n" + sep(day, "\n")
        if out == "":
            out = "diary2text: empty out\n" + str(diary)
    return out   

def getNews(take=-1):
    p = {
        "At": at
    }
    params = { 
        "take": take
    }
    r = session.get("https://net-school.cap.ru/webapi/announcements", params=params, data=p)
    rj = json.loads(r.text)
    return rj

def discardOldNews(news, updateOld = False):
    try:
        old = list(map(int, open(dataPath + "/shownNews.txt").readlines()))
    except:
        old = []
    i = 0
    while i < len(news):
        id = news[i].get("id")
        if id in old:
            del news[i]
        else:
            i+=1
            if updateOld:
                old.append(id)
    
    if updateOld and False:
        f = open(dataPath + "/shownNews.txt", "w")
        for i in old:
            f.write(str(i) + "\n")
    
    return news

def addToOld(l: list):
    f = open(dataPath + "/shownNews.txt", "a")
    for i in l:
        f.write(str(i) + "\n")

def news2text(news, showTitle=True, showDescription=True, showDate=True, showAuthor=True, showAttachments=True, showId=False):
    out = ""
    for i in news:
        this = ""
        attachments = []
        for j in i.get("attachments"):
            attachments.append(j.get("name"))
        attachments = sep(attachments, "; ")

        if showTitle == True:
            this += "➖Тема: " + i.get("name") + "<br>\n"
        if showDescription == True:
            this += "➖Основной текст: " +  i.get("description") + "<br>\n"
        if showAuthor == True:
            if i.get("author").get("fio") !=  i.get("author").get("nickName"):
                this += "➖Автор: " + i.get("author").get("fio") + " (" +  i.get("author").get("nickName") + ")<br>\n"
            else:
                this += "➖Автор: " + i.get("author").get("fio") + "<br>\n"
        if showDate == True:
            if i.get("deleteDate") != None:
                this += "➖Дата: " + i.get("postDate")[:10] + " (" + i.get("deleteDate")  + ")<br>\n" # ???
            else:
                this += "➖Дата: " + i.get("postDate")[:10] + "<br>\n"
        if showAttachments == True and attachments != "":
            this += "➖attachments: " + attachments + "<br>\n"
        if showId == True:
            this += "➖id: " + i.get("id") + "<br>\n"
        out += this + "<br>\n"
    return out

def attachments2images(attachments, name):
    count = 0
    for i in attachments:
        id = i.get("id")
        r = session.get("https://net-school.cap.ru/webapi/attachments/" + str(id), data = {"At": at})
        try:
            os.mkdir(dataPath + "/tmp/" + name)
        except:
            pass
        
        path = dataPath + "/tmp/" + name
        try:
            os.mkdir(path + "/files")
        except:
            pass
        extension = i.get("originalFileName").split(".")[-1]
        fileName = str(id) + "." + extension
        open(path + "/" + fileName, "wb").write(r.content)
        open(path + "/files/" + i.get("originalFileName"), "wb").write(r.content)
        if extension == "docx":
            nFileName = str(id) + ".pdf"
            os.system("doc2pdf -o " + path + "/" + nFileName + " " + path + "/" + fileName)
            #docx2pdf.convert(path + "/" + fileName, path + "/" + nFileName)

            fileName = nFileName
            extension = "pdf"
        
        if extension == "pdf":
            try:
                os.mkdir(path + "/img")
            except:
                pass
            pages = pdf2image.convert_from_path(path + "/" + fileName, last_page=10)
            for num, page in enumerate(pages):
                page.save(path + f"/img/{count}.jpg", 'JPEG')
                count += 1
    return count

#vk
def write_msg(user_id, message):
        if message == "":
            message = "EMPTY MESSAGE"
        else:
            message += ";"
        gVk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})

def post(p = "", attachments = ""):
    if p != "" or attachments != "":
        r = sVk.method("wall.post", {"owner_id": -groupId, "from_group": 1, "message": p, "attachments": attachments})
        print(r)

def photoUpload(photo: str):
    r = vk_api.upload.VkUpload.photo_wall(self=vk_api.upload.VkUpload(sVk), photos=[photo], group_id=groupId)[0]
    owner_id = r['owner_id']
    photo_id = r['id']
    return owner_id, photo_id

def docUpload(doc: str, name = "file"):
    r = vk_api.upload.VkUpload.document_wall(self=vk_api.upload.VkUpload(sVk), doc=[doc], title=name)['doc']
    owner_id = r['owner_id']
    doc_id = r['id']
    return owner_id, doc_id

def photo2attachment(photo: str):
    r = photoUpload(photo)
    return f'photo{r[0]}_{r[1]}'

def doc2attachment(doc, name):
    r = docUpload(doc, name)
    return f'doc{r[0]}_{r[1]}'



_path = abspath(getsourcefile(lambda:0)).replace("main.py", "").replace("\\", "/")
if not os.path.exists(_path + "conf.ini"):
    createConfig(_path + "conf.ini")
    print("an empty conf.ini file was created")
config = configparser.ConfigParser()
config.read(_path + "conf.ini", "utf8")

groupId = int(config["vk"]["groupid"])
groupToken = config["vk"]["grouptoken"]
accessToken = config["vk"]["accesstoken"]
delay = int(config["main"]["delay"])
dataPath = config["main"]["path"]
password = config["netSchool"]["password"]
userName = config["netSchool"]["username"]
studentId = config["netSchool"]["userid"]
vers = config["netSchool"]["vers"]

gVk = vk_api.VkApi(token=groupToken)
sVk = vk_api.VkApi(token=accessToken)

if not os.path.exists(dataPath + "/shownNews.txt"):
    createData()



isRun, autoRun = True, True
def messages():
    global isRun
    try:
        longpoll = VkLongPoll(gVk)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                
                if event.to_me:
                    request = event.text
                    words = request.split()
                    ln = len(words)
                    msg = ""
                    
                    if not isOnline():
                        login()

                    if words[0] == "дз":
                        if ln == 2:
                            start = words[1]
                            end = str(datetime.datetime.strptime(start, "%Y-%m-%d").date() + datetime.timedelta(days=3))

                        elif ln == 3:
                            start = words[1]
                            end = words[2]
                        else:
                            start = str(datetime.datetime.now())[:10]
                            end = str(datetime.datetime.strptime(start, "%Y-%m-%d").date() + datetime.timedelta(days=3))
                        
                        if len(start) == 10 and start[:4].isdigit() and start[5:7].isdigit() and start[8:].isdigit() and len(end) == 10 and end[:4].isdigit() and end[5:7].isdigit() and end[8:].isdigit():
                            dt = (datetime.date(year=int(end[:4]), month=int(end[5:7]), day=int(end[8:])) - datetime.date(year=int(start[:4]), month=int(start[5:7]), day=int(start[8:]))).days
                            if dt not in range(0, 10):
                                msg = "big date gap (" + str(dt) + ")"
                            else:
                                msg = diary2text(getDiary(start, end))
                        else:
                            msg = "invalid date (" + start + "; " + end + ")"

                    if words[0] == "новости":
                        if len(words) == 1:
                            news = getNews()
                            i = 0
                            while i < len(news):
                                date = datetime.datetime.strptime(news[i].get("postDate")[:10], "%Y-%m-%d").date()
                                if date != datetime.date.today():
                                    del news[i]
                                else:
                                    i+=1
                            
                            msg = news2text(news)
                        if len(words) == 2:
                            if words[1] == "все":
                                msg = "починить"
                            
                            if words[1] == "новые":
                                msg = news2text(discardOldNews(getNews(), True))
                                
                        msg = html2text.html2text(msg)
                        
                    if words[0] == "logout":
                        if not isOnline():
                            msg = "already"
                        else:
                            logout()
                            if isOnline():
                                msg = "unsuccessfuly"
                            else:
                                msg = "successfuly"
                    
                    if words[0] == "stop" or words[0] == "стоп":
                        global isRun, autoRun
                        isRun, autoRun = False, False
                        write_msg(event.user_id, "stop was applied")
                        break

                    write_msg(event.user_id, msg)
    except Exception as e:
        print(e)
        try:
            post(e)
        except Exception as _e:
            print("    ::::   ", _e)
        isRun = False

def posts():
    global isRun
    while isRun or True:
        if not isOnline():
            login()
        news = discardOldNews(getNews())
        for i in news:
            id = str(i.get("id"))
            attachmentsAmount = attachments2images(i.get("attachments"), id)
            attachments = []
            filesAmount = 0
            if os.path.isdir(dataPath + f"/tmp/{id}/files"):
                filesAmount = len(os.listdir(dataPath + f"/tmp/{id}/files"))

            for j in range(min(10 - filesAmount, attachmentsAmount)):
                path = dataPath + f"/tmp/{id}/img/{str(j)}.jpg"
                print(path)
                attachments.append(photo2attachment(path))

            if os.path.isdir(dataPath + f"/tmp/{id}/files"):
                for j in os.listdir(dataPath + f"/tmp/{id}/files"):
                    path = dataPath + f"/tmp/{id}/files/{j}"
                    attachments.append(doc2attachment(path, j))
            
            addToOld([id])
            attachments = sep(attachments, ",")
            post(html2text.html2text(news2text([i])), attachments)
        time.sleep(delay)
    

def foodPosts():
    global isRun
    try:
        try:
            os.mkdir(dataPath + "/food")
        except:
            pass
        date = None
        while isRun:
            if date != datetime.date.today():
                date = datetime.date.today()
                try:
                    getFood(date)
                    pages = pdf2image.convert_from_path(dataPath + "/food/pdf.pdf")
                    #for num, page in enumerate(pages):
                    #    page.save("/food/img.jpg", 'JPEG')
                    pages[0].save(dataPath + "/food/img.jpg", 'JPEG')
                    post(str(date), photo2attachment(dataPath + "/food/img.jpg"))
                except:
                    pass
            time.sleep(delay)
    except Exception as e:
        print(e)
        try:
            post(e)
        except Exception as _e:
            print("    ::::   ", _e)
        isRun = False
            
            

def main():
    msgThr, postThr, foodThr = threading.Thread(target=messages), threading.Thread(target=posts), threading.Thread(target=foodPosts)
    msgThr.start()
    postThr.start()
    foodThr.start()
    msgThr.join()
    postThr.join()
    foodThr.join()

#addToOld(["123123"])
posts()
while autoRun and False:
    try:
        main()
    except Exception as e:
        print(e)
        try:
            post(e)
        except Exception as _e:
            print("    ::::   ", _e)

if isOnline():
    logout()