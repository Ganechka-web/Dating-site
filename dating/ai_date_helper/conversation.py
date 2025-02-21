import os
import json
import requests
import datetime

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
        self.asker = asker
        self.target = target
    
    @staticmethod
    def _get_data_from_prompt_file() -> str:
        path_to_file = os.path.join(
            settings.BASE_DIR, 'ai_helper',
            'static', 'ai_helper', 'txt',
            'prompt.txt')
        
        with open(path_to_file, 'r', encoding='utf-8') as prompt:
            content = prompt.read()
            return content
        
    def _format_content(self, content: str) -> str:
        """
        This method creates and formats data to content and returns it
        """
        asker_zodiac = get_user_zodiac_sign(self.asker.date_birth)
        target_zodiac = get_user_zodiac_sign(self.target.date_birth)
        asker_interests = self.asker.interests.all().join(', ')
        target_interests = self.target.interests.all().join(', ')
        asker_gender = get_user_clear_gender(self.asker)
        target_gender = get_user_clear_gender(self.target)

        content.format(
            asker_username=self.asker.username, asker_gender=asker_gender, 
            asker_zodiac=asker_zodiac, asker_age=self.asker.age, 
            asker_interests=asker_interests, asker_description=self.asker.description, 
            asker_city=self.asker.city,
            target_username=self.target.username, target_gender=target_gender, 
            target_zodiac=target_zodiac, target_age=self.target.age, 
            target_interests=target_interests, target_description=self.target.description,
            target_city=self.target.city)
        
        return content
    
    @staticmethod
    def _send_request(content: str) -> requests.Response:
        """
        This method sends request to AI API and returns response 
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

    def get_helper_answer(self) -> tuple[int, str | None]:
        content = self._get_data_from_prompt_file()
        response = self._send_request(content)

        # TO DO: implement getting text data from response
