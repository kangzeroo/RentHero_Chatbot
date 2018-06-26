import email
from email.parser import Parser

#Import file convert to string and readable file object
messagefile = './raw_data/raw_emails/MIME_Emails/1vqcsmni9o9td9cmp4l4vvg5qgqmrv6oi3jnaio1.txt'
with open(messagefile) as fp:
    headerString = fp.read()
headers = Parser().parsestr(headerString)

#Generate Body text
mail = email.message_from_string(headerString)

bodytext = 'To: %s' % headers['to'] \
            + '\n' + 'From: %s' % headers['from'] \
            + '\n' + 'Subject: %s' % headers['subject'] \
            + '\n' + mail.get_payload()[0].get_payload()

if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)

textVal = -1
textList = []
messageList = []
bodytextB = ''
bodytextB = bodytext.replace('------------------------------', '$*$') \
                    .replace(' wrote:', '$*$') \
                    .replace('\nwrote:', '$*$') \
                    .replace('>', '')

while True:
    textVal = bodytextB.find('$*$', textVal + 1)
    textList.append(textVal)
    if textVal == -1: break

textList.sort()

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#Generate seperating points of each message
emailList = ['$*$\n$END$\n']
for i in range(0, len(textList)-1):
    emailList.append('')
    for j in range(textList[i], textList[i+1]):
        emailList[i] += bodytextB[j]
    emailList[i] += '$*$\n'
    messageList.append(find_between(emailList[i], '$*$', '$*$'))

emailList.insert(0,bodytext)

for j in range(textList[len(textList)-1], len(bodytextB)):
    emailList[len(textList)-1] += bodytextB[j]
emailList.append('\n$START$\n$*$')

for i in range(0, len(messageList)):
     print(messageList[i])
     print('\n\n\n')
