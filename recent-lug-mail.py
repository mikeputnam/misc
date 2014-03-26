import imaplib
from email.Parser import HeaderParser
from email.Utils import parsedate_tz,mktime_tz,formatdate,parseaddr
import time
import datetime
from datetime import date
from xml.dom import minidom
import argparse 

def getmail(user, password, gmailfolder):
    webarchive = {
        'lacrosselug@googlegroups.com':'http://groups.google.com/group/lacrosselug/topics',
        'newlug@newlug.org':'http://newlug.org/pipermail/newlug/',
        'madlug@madisonlinux.org':'http://madisonlinux.org/pipermail/madlug/',
        'mlug-list@milwaukeelug.org':'http://www.milwaukeelug.org/wws/arc/mlug-list',
        'mlug-list@mail.milwaukeelug.org':'http://www.milwaukeelug.org/wws/arc/mlug-list',
        'fdllug-list@lists.fdllug.org':'http://lists.fdllug.org/mailman/listinfo/fdllug-list',
        'bratlug@lists.bratlug.org':'http://bratlug.org/pipermail/bratlug/',
        'kenoshalinux@googlegroups.com':'http://groups.google.com/group/kenoshalinux/topics',
        'blinux@googlegroups.com':'http://groups.google.com/group/blinux/topics',
        'ec_lug@googlegroups.com':'http://groups.google.com/group/ec_lug/topics',
        'ubuntu-us-wi@lists.ubuntu.com':'https://lists.ubuntu.com/archives/ubuntu-us-wi/',
        'dhmn-discussion@googlegroups.com':'http://groups.google.com/group/dhmn-discussion/'
    }
    print 'Logging in...'
    conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    conn.login(user, password)
    print 'Querying for mail...'
    conn.select(gmailfolder) #mailbox/gmail label
    since = datetime.datetime.today() - datetime.timedelta(days=7) 
    since = since.strftime("%d-%b-%Y")
    typ, mailnumlist = conn.search(None, 'SINCE', since) #or ALL
    #typ, mailnumlist = conn.search(None, 'ALL') #or ALL
    maillist = []
    for num in mailnumlist[0].split():#search returns space delimited tuple
        alldata = conn.fetch(num, '(BODY[HEADER])')
        header_data = alldata[1][0][1]
        headerparser = HeaderParser()
        msg = headerparser.parsestr(header_data)
        mail = []
        # Force dates to be in Central time.  This is Wisconsin after all.
        mail.append(mktime_tz(parsedate_tz(msg['Date'])))
        mail.append(parseaddr(msg['From'])[0]) #just the realname portion
        mail.append(msg['Subject'])
        tolug = parseaddr(msg['To'])[1].lower()
        cclug = parseaddr(msg['Cc'])[1].lower()
        if   tolug in webarchive: url = webarchive[tolug]
        elif cclug in webarchive: url = webarchive[cclug] 
        else: url = '#'
        mail.append(url)
        print 'Loading mail: ',num,'|',parseaddr(msg['From'])[0],\
            '|',msg['Subject']
        maillist.append(mail)
    conn.close()
    print 'Mail load complete.'

    print 'Sorting by date...'
    #maillist.sort(reverse=True) #most recent on top
    maillist.sort() #most recent on bottom

    print 'Building xml...'
    xmldoc = minidom.Document()
    rootelem = xmldoc.createElement('recentmail')
    xmldoc.appendChild(rootelem)
    #for m in maillist[0:10]: #just the 10 most recent
    for m in maillist[len(maillist)-10:len(maillist)]: #just the 10 most recent
        mailelem = xmldoc.createElement('mail')
        #mailelem.setAttribute('date'   , formatdate(m[0],localtime=True))
        mailelem.setAttribute('date'   , time.strftime('%Y-%m-%d %I:%M%p',\
            time.localtime(m[0])).lower())
        mailelem.setAttribute('from'   , m[1])
        mailelem.setAttribute('subject', m[2])
        mailelem.setAttribute('url'    , m[3])
        rootelem.appendChild(mailelem)
    fp = open("/home/mike/crons/recentmail_" + gmailfolder + ".xml",'w')
    xmldoc.writexml(fp, '  ', '  ', '\n', 'UTF-8')
    print 'Done.'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download recent email and produce an XML file of it.')
    parser.add_argument('-u', '--user')
    parser.add_argument('-p', '--password')
    parser.add_argument('gmailfolder')
    args = parser.parse_args()
    getmail(args.user, args.password, args.gmailfolder)
