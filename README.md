# Website-Scanner

This is a website scanner I made in python based off of thenewboston's tutorial. It's pretty crap but for me it was a good learning experience and I'm happy that I managed to make it. It could definitely be improved but I won't be touching it for a while.

# What it does

It takes a URL and with that URL, obtains and stores the following information

- Full URL
- Domain Name
- IP Address
- Nmap scan
- Whois scan
- The site's robot.txt

After the user has entered the full URL, it will ask for the name that the user would like the folder in which the info will be stored in to be called. It will take that name and create a folder with it. You can then put any custom nmap stuff in and after that it will scan and store.




If it doesn't work, its probably for one of these reasons:

- whois package isn't installed
- tld package isn't installed
- nmap isn't installed

