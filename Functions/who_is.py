import whois

def getWhoIs(url): #runs the who is
    process = whois.whois(url)
    results = str(process) #runs a whois search on presented URL
    return results #returns results


