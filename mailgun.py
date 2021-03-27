"""
Mailgun Class to send messages through Mailgun's v3 API.
"""
import requests
BASE_URL = 'https://api.mailgun.net/v3'


class Mailgun:

    def __init__(self, api_key: str, domain: str) -> None:
        """
        Initialize Class with API key and domain.

            mg = new Mailgun(api_key, domain)
        """
        self.api_key = api_key
        self.domain = domain

    def send(self, *args, **kwargs):
        """
        Send Message.

            mg.send(from, to=[], subject='subject', text='content')
        """
        data = {
            'to': [],
            'subject': '',
            'text': ''
        }
        data.update(kwargs)
        data['from'] = args[0]
        auth = ('api', self.api_key)
        endpoint = f'{BASE_URL}/{self.domain}/messages'

        return requests.post(endpoint, auth=auth, data=data)
