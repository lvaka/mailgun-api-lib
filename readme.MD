# Mailgun Library 
 
This is a tiny library that handles sending a message through Mailgun's API.  Handles the requests required to send a message through Mailgun's API. 
 
 Example:  
```
mg = new Mailgun(api_key, domain)  # This initializes the object
mg.send(from, to=['destination@email.com'], subject='subject', text='content') # Method sends message through API
```