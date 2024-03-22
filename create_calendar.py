import re
import datetime

def czyPrzestepny(rok):
  if rok % 400 == 0 and rok % 100 == 0:
    return True 
  elif rok % 4 == 0 and rok % 100 != 0:
    return True
  else:
    return False
    
def zmianaDaty(rok,miesiac,dzien):
  miesiac1=miesiac
  dzien1=dzien+1
  rok1=rok
  if miesiac1==1:
    if dzien+1>31:
      miesiac1=2
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==2 and czyPrzestepny(rok)==True:
    if dzien+1>29:
      miesiac1=3
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==2 and czyPrzestepny(rok)==False:
    if dzien+1>28:
      miesiac1=3
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==3:
    if dzien+1>31:
      miesiac1=4
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==4:
    if dzien+1>30:
      miesiac1=5
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==5:
    if dzien+1>31:
      miesiac1=6
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==6:
    if dzien+1>30:
      miesiac1=7
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==7:
    if dzien+1>31:
      miesiac1=8
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==8:
    if dzien+1>31:
      miesiac1=9
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==9:
    if dzien+1>30:
      miesiac1=10
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==10:
    if dzien+1>31:
      miesiac1=11
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==11:
    if dzien+1>30:
      miesiac1=12
      dzien1=1
      rok1=rok
      return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==12:
    if dzien+1>31:
      miesiac1=13
      dzien1=1
      rok1=rok+1
      return (rok,rok1,miesiac,1,dzien,1)
  return (rok,rok1,miesiac,miesiac1,dzien,dzien1)
  

f1 = open("Contacts.vcf","r")
f2 = open("Birthdays.ics","w")
lines = f1.readlines()
tmp=[]
for line in lines:
    if line.startswith("FN:"):
      line = line.replace("\n","")
      tmp.append(line)
    if line.startswith("BDAY:"):
      line = line.replace("\n","")
      tmp.append(line)
      
f2.write("BEGIN:VCALENDAR\n")
f2.write("PRODID:-//Google Inc//Google Calendar 70.9054//EN\n")
f2.write("VERSION:2.0\n")
f2.write("CALSCALE:GREGORIAN\n")
f2.write("METHOD:PUBLISH\n")
f2.write("X-WR-CALNAME:URODZINY\n")
f2.write("X-WR-TIMEZONE:Europe/Warsaw\n")

try:
  for i in tmp:
    x = re.search(r'-\d\d-\d\d', i)
    if x:
      index = tmp.index(i)
      name = tmp[index-1]
      birthday = tmp[index]
      if name.startswith("FN:"):
        name = name.replace("FN:","")
      if birthday.startswith("BDAY:"):
        birthday = birthday.replace("BDAY:","")
      birthday = birthday.replace("-","")
      birthday = birthday[4:]
      i = birthday[0]+birthday[1]
      j = birthday[2]+birthday[3]
      
      currentDateTime = datetime.datetime.now()
      date = currentDateTime.date()
      rok = int(date.strftime("%Y"))
      rok,rok1,miesiac,miesiac1,dzien,dzien1 = zmianaDaty(rok,int(i),int(j))
      
      if miesiac<10:
        miesiac=str("0"+str(miesiac))
      else:
        miesiac=str(miesiac) 
             
      if miesiac1<10:
        miesiac1=str("0"+str(miesiac1))
      else:
        miesiac1=str(miesiac1)
         
      if int(dzien)<10:
        dzien="0"+str(dzien)
     
      if dzien1<10:
        dzien1=str("0"+str(dzien1))
      else:
        dzien1=str(dzien1)
      
      print(rok,miesiac,miesiac1,dzien,dzien1)

      f2.write("BEGIN:VEVENT\n")
      f2.write("DTSTART;VALUE=DATE:"+str(rok)+str(miesiac)+str(dzien)+"\n")
      f2.write("DTEND;VALUE=DATE:"+str(rok1)+str(miesiac1)+str(dzien1)+"\n")
      f2.write("RRULE:FREQ=MONTHLY;INTERVAL=12;BYMONTHDAY="+str(dzien)+"\n")
      f2.write("DTSTAMP:20240101T125937Z\n")
      f2.write("UID:\n")
      f2.write("CLASS:PRIVATE\n")
      f2.write("CREATED:20240101T125437Z\n")
      f2.write("LAST-MODIFIED:20240101T125437Z\n")
      f2.write("SEQUENCE:0\n")
      f2.write("STATUS:CONFIRMED\n")
      f2.write("SUMMARY:"+name+" ma urodziny\n")
      f2.write("TRANSP:TRANSPARENT\n")
      f2.write("END:VEVENT\n")
      
except:
  print("An exception occurred") 
f2.write("END:VCALENDAR\n")
f2.close()
