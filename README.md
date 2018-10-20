# Google App Engine Proxy
Python based application that act as a reverse proxy,<br> 
you can modify the data in both ways toward the origin and toward the client . 
 
## Content : 
- app.yaml
- main.py
- static/robots.txt

## usage
Modify <b>main.py</b> and set the domain this app will use and the destination,<br>
feel free to modify anything else you think worth changing or modifing  ;-) 

```
  intdomain = "destination.example.com"
  extdomain = "origin.example.com"
```

extdomain is the domain the client hits while intdomain is the origin destination FQDN/IP<br>
Upload the files to a google app engine , and thats it. <br>
if you need to have some static files served from by this proxy, <br>
you can use the example for the robotx.txt .
