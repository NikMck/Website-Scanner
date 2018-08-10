from tld import get_fld

def getDomainName(url): #gets top level domain from url
    domainName = get_fld(url) #get_tld returns the top level domain (eg google.com) from presented url
    return domainName #returns top level domain
