from Functions.others import *
from Functions.domain_name import *
from Functions.get_ip import *
from Functions.nmap import *
from Functions.robots_txt import *
from Functions.who_is import * #Imports all commands needed.

ROOT_DIR = "sites" #Creates the root directory, names it sites
createDir(ROOT_DIR) #If this shit doesn't already exist then god creates it

def obtainInfo(name, url, nmapOption): #Function that uses all commands to get info
    print("COLLECTING DOMAIN NAME")
    domainName = getDomainName(url) #gets domain name from the presented url
    print("COLLECTING IP ADDRESS")
    ipAddress = getIP(domainName) #uses collected domain name to get IP
    print("COLLECTING NMAP")
    nmap = getNmap(nmapOption, ipAddress) #collects the nmap, takes in any desired settings and uses collected ip
    print("COLLECTING ROBOTS.TXT")
    robots_txt = getRobotsTxt(url)  #gets the robots.txt from the presented url
    print("COLLECTING WHOIS.TXT")
    whois = getWhoIs(domainName) #gets the whois from the collected domain name
    saveInfo(name, url, domainName, nmap, robots_txt, whois, ipAddress) #uses save info to save all the collected info in separate files in a separate folder
    print("ALL INFORMATION SAVED SUCCESSFULLY")

def saveInfo(name, fullUrl, domainName, nmap, robots_txt, whois, ipAddress): #function used to save collected info
    projectDir = ROOT_DIR + "/" + name #defines a variable which has the root directory + whatever the user wants to call the specific folder
    createDir(projectDir) #creates the dir based on the desired name
    print("SAVING DOMAIN NAME")
    writeFile(projectDir + "/domainName.txt", domainName)  # creates domainName.txt and stores the domain name
    print("SAVING IP ADDRESS")
    writeFile(projectDir + "/ip_address.txt", ipAddress) #creates ip_address.txt and stores the ip
    print("SAVING NMAP")
    writeFile(projectDir + "/nmap.txt", nmap) #creates nmap.txt and stores the nmap
    print("SAVING ROBOTS.TXT")
    writeFile(projectDir + "/robots_txt.txt", robots_txt) #creates robot.txt and stores the robot.txt
    print("SAVING WHOIS.TXT")
    writeFile(projectDir + "/whois.txt", whois) #creates whois.txt and stores the who is
    print("SAVING FULL URL")
    writeFile(projectDir + "/full_url.txt", fullUrl)  #creates full_url.txt and stores the full url

userURL = raw_input("Please enter the URL that you would like to scan (e.g. https://www.reddit.com)\n") #gets the desired url from the user
userName = raw_input("Please enter the name that you would like to have the folder to have\n") #gets the desired folder name from the user
userNmapOptions = raw_input("If you have any custom nmap options, enter them here. If not, enter nothing.\n") #gets any desired nmap options

obtainInfo(userName, userURL, userNmapOptions) #runs the function with user inputs