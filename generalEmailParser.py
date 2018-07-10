import email
import re

messagefile = './raw_data/raw_emails/MIME_Emails/1vqcsmni9o9td9cmp4l4vvg5qgqmrv6oi3jnaio1.txt'
filters = [lambda a: a!= '', lambda a: a != '>', lambda a: a!= '> ', lambda a: a!= ' >', \
           lambda a: a!= '>>', lambda a: a!= '>> ', lambda a: a!= ' >>', lambda a: 'https://' not in a]
d = {} # {'From' : [], 'To' : [], 'Date' : [], 'Subject' : [], 'Body' : []}
textIndexList = []
emailList = []
messageList = []
filteredList = []
bodyReplaced = ''

#reads file, strips away HTML and gets converted to string
with open(messagefile) as fp:
    headerString = fp.read()
mailMIMEForm = email.message_from_string(headerString)
bodytext = mailMIMEForm.get_payload()[0].get_payload()

#seperates all lines of the text
#splitBody = bodytext.split('\n')

#apply multiple filters to text
def multiFilter(filters, text):
    for f in filters:
        text = filter(f, text)
    return text

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def seperateMessages(text):
        textVal = -1
        bodyReplaced = text.replace('*', '') \
                               .replace('------------------------------', '$*$') \
                               .replace('---------- Forwarded message ---------', '') \
                               .replace('On Mon,', '$*$') \
                               .replace('On Tue,', '$*$') \
                               .replace('On Wed,', '$*$') \
                               .replace('On Thu,', '$*$') \
                               .replace('On Fri,', '$*$') \
                               .replace('On Sat,', '$*$') \
                               .replace('On Sun,', '$*$')
        while True:
            textVal = bodyReplaced.find('$*$', textVal + 1)
            textIndexList.append(textVal)
            if textVal == -1: break
        textIndexList.sort()
        for i in range(0, len(textIndexList)-1):
            emailList.append('')
            for j in range(textIndexList[i], textIndexList[i+1]):
                emailList[i] += bodyReplaced[j]
            emailList[i] += '$*$\n'
            messageList.append(find_between(emailList[i], '$*$', '$*$'))
        return messageList,textIndexList

def classifyString(text):
    if 'To:' in text:
        d.setdefault('To', []).append(text.replace('To:',''))
    elif 'From:' in text:
        d.setdefault('From', []).append(text.replace('From:',''))
    elif 'Date:' in text:
        d.setdefault('Date', []).append(text.replace('Date:',''))
    elif 'Sent:' in text:
        d.setdefault('Date', []).append(text.replace('Date:',''))
    elif 'Subject:' in text:
        d.setdefault('Subject', []).append(text.replace('Subject:',''))
    else:
        d.setdefault('Body', []).append(text)

#Loop through each message block
for message in seperateMessages(bodytext)[0]:
    newD = {}
    #Split each message block line by line
    splitMessage = message.split('\n')

    #Filter and append each line to a new list
    filteredList.append(list(multiFilter(filters, splitMessage)))

for i in range(0,len(filteredList)):
    for j in range(0,len(filteredList[i])):
        classifyString(filteredList[i][j])
    newD.setdefault('Email',[]).append(d)
    d = {}
print(newD)
