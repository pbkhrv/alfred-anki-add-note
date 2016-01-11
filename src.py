import subprocess
import httplib, urllib

def get_user_input(prompt):
  script = """
    tell application "System Events"
        activate
        set txt to the text returned of (display dialog "%s" default answer "")
        copy txt to stdout
    end tell
""" % prompt
  p = subprocess.Popen(['osascript'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  out, err = p.communicate(script)
  return out

def post_to_anki(front, back):
  params = urllib.urlencode({'front': front, 'back': back})
  headers = {"Content-type": "application/x-www-form-urlencoded"}
  conn = httplib.HTTPConnection("127.0.0.1", 41837)
  conn.request("POST", "/decks/programming16", params, headers)
  response = conn.getresponse()
  response.read()
  conn.close()
  print "added?"

card_front = get_user_input("FRONT of the card:")
card_back = get_user_input("BACK of the card:")
post_to_anki(card_front, card_back)
