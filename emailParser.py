import email
from email.parser import Parser

#Import file convert to string and readable file object
messagefile = './raw_data/raw_emails/MIME_Emails/1vqcsmni9o9td9cmp4l4vvg5qgqmrv6oi3jnaio1.txt'
textVal = -1
textList = []
messageList = []
contactInfoList = []
masterList = []
weekday = ['On Mon,', 'On Tue,', 'On Wed,', 'On Thu,', 'On Fri,', 'On Sat,', 'On Sun,']
bodytextB = ''
bodytextA = ''

with open(messagefile) as fp:
    headerString = fp.read()
headers = Parser().parsestr(headerString)
mail = email.message_from_string(headerString)

#Generate Body text
# bodytext = 'To: %s' % headers['to'] \
#             + '\n' + 'From: %s' % headers['from'] \
#             + '\n' + 'Subject: %s' % headers['subject'] \
bodytext = mail.get_payload()[0].get_payload()

masterList.append(['HEADER CONTENT', headers['to'], headers['from'],headers['subject']])
# print(masterList)

if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)

bodytextB = bodytext.replace('*', '') \
                    .replace('------------------------------', '$*$') \
                    .replace('---------- Forwarded message ---------', '') \
                    .replace('On Mon,', '$*$') \
                    .replace('On Tue,', '$*$') \
                    .replace('On Wed,', '$*$') \
                    .replace('On Thu,', '$*$') \
                    .replace('On Fri,', '$*$') \
                    .replace('On Sat,', '$*$') \
                    .replace('On Sun,', '$*$')
print(bodytextB)
# for i in range(0, len(weekday)):
#     bodytextB = bodytextA.replace(weekday[i], '$*$')
                    # .replace(' wrote:', '$*$') \
                    # .replace('\nwrote:', '$*$')


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
    contactInfoList.append([find_between(emailList[i], 'From:', '\n'), \
                            find_between(emailList[i], 'To:', '\n'), \
                            find_between(emailList[i], 'Sent:', '\n'), \
                            find_between(emailList[i], ' ', 'wrote:'), \
                            find_between(emailList[i], 'Subject:', '\n')])

for i in range(0, len(messageList)):
    for j in range(0, len(contactInfoList)):
        for k in range(0, len(contactInfoList[j])):
            if (contactInfoList[j][k] in messageList[i]):
                bodytextA = bodytextB.replace(contactInfoList[j][k], '')

emailList.insert(0,bodytext)

for j in range(textList[len(textList)-1], len(bodytextB)):
    emailList[len(textList)-1] += bodytextB[j]
emailList.append('\n$START$\n$*$')
# print(bodytext)
# for i in range(0, len(messageList)):
#      print(messageList[i])
#      print('\n\n\n')
