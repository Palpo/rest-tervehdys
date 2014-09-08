import httplib

conn = httplib.HTTPConnection("localhost:8080")
headers = {'Accept': 'text/plain'}
conn.request("GET", "/tervehdys/Antti", headers=headers)
r = conn.getresponse()
if r.status == 200:
    print("Vastaus: %s" % r.read())
else:
    print("Jotain vialla :(")
