import urllib, urllib2
import bs4
import logging

def check_mailcatch(email, retries = 2):
    
    while retries>=0:
        #get mailcatch inbox
        request = urllib2.Request("http://mailcatch.com/en/temporary-inbox?box="+str(email))
        req = urllib2.urlopen(request)
        response =req.read()

        #build dom and parse result
        dom = bs4.BeautifulSoup(response)
        mailslist = dom.find("div",{"id":"mailsList"})
        mailslist = mailslist.findAll("tr",{'class':'mail'})

        count = len(mailslist)
        if count: retries = -1
        else:
            retries = retries - 1
            logging.warn("No mails, retrying")

    mailslist = map(
        lambda x:  {
            'from': x.find("td",{"class":"from"}).attrs['title'],
            'subject': x.find("td",{"class":"subject"}).find('a').text
            }, 
        mailslist)

    return mailslist