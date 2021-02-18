#!/usr/bin/env python3

# Testing pagination on Webex Teams API. Created mock requests module in mock_requests.py
# First we provide a precoded example of an API call to webex teams (mocked)
# A rel="next" link header will be present if another page of results is available
# We will use the 'beforeMessage' cursor (which points to a message id), not 'before' (which is a data cursor)

from lib import mock_requests
from messenger import Messenger
import unittest
from pprint import pprint
import json


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Messenger(requests=mock_requests)
    
    def test_get_messages(self):
        # Check if any messages exists
        messages = self.msg.get_messages().json().get('items')
        self.assertGreater(len(messages), 0)

    def test_has_next_page(self):
        # Check if there are more pages of messages available
        pass

    def test_get_next_page(self):
        # Get the first page

        # Get the next page
        pass
