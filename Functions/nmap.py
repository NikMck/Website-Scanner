import os

def getNmap(options, ip): #gets nmap
    command = "nmap " + options + " " + ip #creates line to go into cmd
    process = os.popen(command) #puts line through cmd
    if not str(process.read()).find("Host seems down."): #If it doesn't fail, its stored
        result = str(process.read()) #turns results from process into readable string
        return result #returns readable results
    else: #If it is failed
        print("REGULAR NMAP FAILED - RESORTING TO -Pn\n(this can take a long time to complete)")
        command = "nmap -Pn " + ip #It is re-run with the -Pn filter
        process = os.popen(command)
        result = str(process.read())
        return result #Same as above
