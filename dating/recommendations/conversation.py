import os
import json
import requests

from django.conf import settings
from django.contrib.auth import get_user_model

from .utils import get_user_zodiac_sign, \
                    get_user_clear_gender


DatingUser = get_user_model()


class AiHelper:
    """
    AiHelper describes an asking ai help to start 
    communications with another user.
    """
    def __init__(self, asker: DatingUser, target: DatingUser) -> None:
        """
        asker: user who need help
        target: user who will be analyzed 
        """
        self.asker = asker
        self.target = target
    
    @staticmethod
    def _get_data_from_prompt_file() -> str:
        """Opens prompt file and returns content from it"""
        path_to_file = os.path.join(
            settings.BASE_DIR, 'recommendations',
            'static', 'recommendations', 'txt',
            'prompt.txt')
        
        with open(path_to_file, 'r', encoding='utf-8') as prompt:
            content = prompt.read()
            return content
        
    def _format_content(self, content: str) -> str:
        """
        Creates and formats data to content and returns it
        """
        asker_zodiac = get_user_zodiac_sign(self.asker.date_birth)
        target_zodiac = get_user_zodiac_sign(self.target.date_birth)
        asker_interests = ', '.join(self.asker.interests.all())
        target_interests = ', '.join(self.target.interests.all())
        asker_gender = get_user_clear_gender(self.asker)
        target_gender = get_user_clear_gender(self.target)

        return content.format(
            asker_username=self.asker.username, asker_gender=asker_gender, 
            asker_zodiac=asker_zodiac, asker_age=self.asker.age, 
            asker_interests=asker_interests, asker_description=self.asker.description, 
            asker_city=self.asker.city,
            target_username=self.target.username, target_gender=target_gender, 
            target_zodiac=target_zodiac, target_age=self.target.age, 
            target_interests=target_interests, target_description=self.target.description,
            target_city=self.target.city)
    
    @staticmethod
    def _send_request(content: str) -> requests.Response:
        """
        Sends request to AI API and returns response 
        """
        response = requests.post(
            url='https://openrouter.ai/api/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {settings.OPENROUTER_AUTH_KEY}'
            },
            data=json.dumps({
                'model': 'deepseek/deepseek-r1:free',
                'messages':  [
                    {
                        'role': 'user',
                        'content': content
                    }
                ]
            })
        )
        return response

    def get_helper_answer(self) -> str | None:
        """Receives text answer from API response"""
        content = self._get_data_from_prompt_file()
        content = self._format_content(content)
        response = self._send_request(content)

        if response.status_code != 200:
            return None
        return response.json()['choices'][0]['message']['content']
        