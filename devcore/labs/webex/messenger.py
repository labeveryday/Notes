import json
from urllib.parse import urlparse, parse_qs
import requests
from pprint import pprint


# API Key is obtained from the Webex Teams developers website
api_key = ''
# roomId is a required parameter when fetching messages,
# and identifies the space (room) from which the messages whill be retrieved.
# roomId can be configured here, or collected by the set_room_id method
room_id = ''
# Maximum number of messages per page
max_items = 3
# Webex Teams messages API endpoint
base_url = 'https://webexapis.com/v1/messages'

class Messenger():
    def __init__(self, base_url= base_url, api_key=api_key, room_id=room_id, requests=requests):
        self.base_url = base_url
        self.api_key = api_key
        self.room_id = room_id
        self.max_items = max_items
        self.api_url = f'{self.base_url}?roomId={self.room_id}&max={self.max_items}'
        self.headers = {
            "Authorization": f"Bearer {api_key}"
        }
        self.requests = requests

    def get_messages(self):
        """Get a list of messages in a room.
           Maximum number of items per page is set to 3"""
        print(f'Requesting {self.api_url}')
        self.response = self.requests.get(self.api_url, headers=self.headers)
        print(json.dumps(self.response.json(),indent=4))
        return self.response

    def has_next_page(self):
        """Check if more pages are available and set the cursor to next page.
           URI s parsed from the response Link Header"""

    def _get_parsed_link_header(self):
        """Parse the relation type and the URL from the LInk Header.
        Construct a dictionary of query parameters"""
        link_header = {}
        link_header["rel"] = requests.utils.parse_header_links(
            self.response.headers["Link"]
        )[0]["rel"]
        link_header["rel"] = requests.utils.parse_header_links(
            self.response.headers["Link"]
        )[0]["url"]
        link_header["params"] = parse_qs(
            urlparse(
                requests.utils.parse_header_links(
                    self.response.headers["Link"]
                )[0]["url"]
            ).query
        )
        print('PARSED LINK HEADER')
        print(json.dumps(link_header, indent=4))
        return link_header
    
    def reset_cursor(self):
        """Set the cursor back to the first page.
           The initial URL is constructed from the base_url, room_id and max variables."""
        self.api_url = f'{self.base_url}?roomId={self.room_id}&max={self.max_items}'
    
    def print_current_page(self):
        """Print just the text of the messages on the current page"""
        for msg in (self.response.json())['items']:
            print(msg['text'])
        print()
    
    def set_room_id(self):
        """Retrieves the room memberships for the bot
           and sets the room_id varaible to the first roomId in the list"""
        self.response = self.requests.get(
            "https://webexapis.com/v1/memberships",
            headers=self.headers
        )
        room_list = self.response.json().get("items")
        for room in room_list:
            print(f"roomId: {room.get('roomId')}")
            print(
                f"personDisplayName: {room.get('personDisplayName')}"
            )
            print()
        self.room_id = room_list[0].get("roomId")
        self.api_url = f"{self.base_url}?roomId={self.room_id}&max={self.max_items}"
        print(f"##### room_id SET TO {self.room_id}\n")
        return self.room_id