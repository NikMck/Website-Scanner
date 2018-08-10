import urllib2
import io

def getRobotsTxt(url): #used to get robots txt file, contains pages that aren't supposed to be seen
    if url.endswith("/"): #if presented url ends with a /, everything is fine
        path = url
    else: #if it doesn't, it is given a /
        path = url + "/"
    request = urllib2.urlopen(path + "robots.txt") #goes to presented url, opens robot.txt and stores the results
    return request.read() #returns collected data



