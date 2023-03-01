### Allows push notifications to be processed through Pushover application
import http.client, urllib

def pushOver(message):
  conn = http.client.HTTPSConnection("api.pushover.net:443")

  conn.request("POST", "/1/messages.json",

    urllib.parse.urlencode({
    "token": "aobd9y8u2nyerhprujnkwesdnf6sos",
    "user": "ugn1u7k4hgcv6841jdff2wfux3nc8r",
    "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })

  conn.getresponse()

pushOver('message')