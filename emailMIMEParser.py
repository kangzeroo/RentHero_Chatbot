import email
import re

messagefile = './raw_data/raw_emails/MIME_Emails/1vqcsmni9o9td9cmp4l4vvg5qgqmrv6oi3jnaio1.txt'
emailList = ['$*$\n$END$\n']
bodyReplaced = ''
textVal = -1
textIndexList = []
messageList = []
messageListReplaced = []

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

with open(messagefile) as fp:
    headerString = fp.read()
mailMIMEForm = email.message_from_string(headerString)
for payload in mailMIMEForm.get_payload():
    x = payload.get_payload().strip()
print(x)
bodytext = mailMIMEForm.get_payload()[0].get_payload()

#emailList.append(['HEADER', mailMIMEForm['from'], mailMIMEForm['to'], mailMIMEForm['date'], mailMIMEForm['subject']])

bodyReplaced = bodytext.replace('*', '') \
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
contentList = []
for i in range(0, len(textIndexList)-1):
    emailList.append('')
    for j in range(textIndexList[i], textIndexList[i+1]):
        emailList[i] += bodyReplaced[j]
    if i < 1 :
        contentList.append([find_between(emailList[i], 'From:', 'Date:'), \
                            find_between(emailList[i], 'To:', '\n'), \
                            find_between(emailList[i], 'Date:', 'Subject:'), \
                            find_between(emailList[i], 'Subject:', 'To:')])
        # else:
        #     contentList.append([find_between(emailList[i], 'From:', 'Date:'), \
        #                         find_between(emailList[i], 'To:', '\n'), \
        #                         find_between(emailList[i], 'Date:', 'Subject:'), \
        #                         find_between(emailList[i], 'Subject:', 'To:')])
    emailList[i] += '$*$\n'
    messageList.append(find_between(emailList[i], '$*$', '$*$'))
    messageList[i] = re.sub(' .*?wrote:','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('From:.*?>','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('To:.*?\n','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('Sent:.*?\n','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('Subject:.*?\n','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('Date:.*?\n','', messageList[i], flags=re.DOTALL)
    messageList[i] = re.sub('<.*?>','', messageList[i], flags=re.DOTALL)
    messageListReplaced.append(messageList[i].replace('>', '').replace('\n', '').replace('$END$', '').replace('  ', ''))

for i in range(0, len(messageListReplaced)):
    print(messageListReplaced[i])
    print('\n')
