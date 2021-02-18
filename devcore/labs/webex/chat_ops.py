import json
import requests
import os


# As a general security best practice,
# 'secrets' (such as API tokens) should not be hard-coded into scripts/apps or passed via the command-line, 
# But rather handed-off via environment variables.
teams_access_token = os.environ["WEBEX_API"]
token = teams_access_token if teams_access_token else None

# Navigate to https://developer.webex.com/docs/api/v1/rooms/list-rooms to get room ID
BOT_ROOM_ID = ""

def send_it(token=token, room_id=BOT_ROOM_ID, message="Hola I am working on my script"):

        header = {"Authorization": "Bearer %s" % token,
                  "Content-Type": "application/json"}

        data = {"roomId": room_id,
                "text": message}

        return requests.post("https://api.ciscospark.com/v1/messages/", headers=header, data=json.dumps(data), verify=True)


if __name__ == "__main__":
    send_it()
