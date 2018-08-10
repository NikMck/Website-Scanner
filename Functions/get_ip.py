import os

def getIP(url): #used to get IP
    command = "ping " + url
    process = os.popen(command)
    results = str(process.read())
    marker1 = results.find("[") + 1
    marker2 = results.find("]")
    return results[marker1:marker2].splitlines()[0]
