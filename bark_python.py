import requests
import json


class Bark:    
    """This is a bark class
    
    Attributes:
        DEVICE_KEY: device_KEY is the key which generated by Bark app. It is not the DEVICE TOEKN!!! It is called Device Key
        SERVER_URL: is the server address like 'https://example.com' no slash at the last character.
    """
    SERVER_URL = ""
    DEVICE_KEY = ""

    def __init__(self, device_KEY: str, server_url: str) -> None:
        self.DEVICE_KEY = device_KEY
        self.SERVER_URL = server_url + "/push"
        

    def send_message(
            self,
            title = 'Notification title',
            body = 'Notification content',
            level = 'active',
            copy = '',
            automaticallyCopy = '1',
            badge = 1,
            sound = '',
            icon = '',
            group = '',
            isArchive = '1',
            url = '',
            user_config = None,
    ) -> None:
        """Send message to device

        Args:
            title (str, optional): _description_. Defaults to 'Notification title'.
            body (str, optional): _description_. Defaults to 'Notification content'.
            levle (str, optional): _description_. Defaults to 'active'.
            copy (str, optional): _description_. Defaults to ''.
            automaticallyCopy (str, optional): _description_. Defaults to '1'.
            badge (int, optional): _description_. Defaults to 1.
            sound (str, optional): _description_. Defaults to ''.
            icon (str, optional): _description_. Defaults to ''.
            group (str, optional): _description_. Defaults to ''.
            isArchive (str, optional): _description_. Defaults to '1'.
            url (str, optional): _description_. Defaults to ''.
            user_config (_type_, optional): _description_. Defaults to None.
        """        
        payload ={
            "title": title,
            "body": body,
            "level": level,
            "copy": copy,
            "automaticallyCopy": automaticallyCopy,
            "badge": badge,
            "sound": sound,
            "icon": icon,
            "group": group,
            "isArchive": isArchive,
            "url": url,
            "device_key": self.DEVICE_KEY
        }

        if user_config is not None:
            payload.update(user_config)
        try:
            response = requests.post(
                url = self.SERVER_URL,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                },
                data = json.dumps(payload)
            )
            print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')