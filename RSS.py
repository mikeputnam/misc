#from ntlm import HTTPNtlmAuthHandler
import argparse
import feedparser
#import getpass
import re
import urllib2

"""
REQUIRED
    * python-ntlm package
    * feedparser package
"""
#setup parameters this script will accept
parser = argparse.ArgumentParser()
parser.add_argument("url", help="url you want to fetch")
#parser.add_argument("-u","--user", help="user in the format DOMAIN\\USER")
#parser.add_argument("-p","--password", help="domain password")
args = parser.parse_args()
#if args.password:
#    password = args.password
#else:
#    password = getpass.getpass()

#deal with Microsoft NTLM so we can access IIS/Sharepoint/etc
#passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
#passman.add_password(None, args.url, args.user, password)
#auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
#proxy_handler = urllib2.ProxyHandler({})#ignore $http_proxy if set
#opener = urllib2.build_opener(proxy_handler, auth_NTLM)
#urllib2.install_opener(opener)
response = urllib2.urlopen(args.url)
parsedresponse = feedparser.parse(response)#actually get the RSS feed

#print parsedresponse

#begin problem-specific stuff for an RSS feed and the entries we care about
for entry in parsedresponse['entries']:
    print "* " + entry.title.encode('UTF-8')
    for link in entry.links:
        print "    " + link.href
