import datetime

from django.contrib.auth import get_user_model


DatingUser = get_user_model()

ZODIAC_INTERVALS = {
    (datetime.date(2000, 3, 21), datetime.date(2000, 4, 20)): 'Овен',
    (datetime.date(2000, 4, 21), datetime.date(2000, 5, 20)): 'Телец',
    (datetime.date(2000, 5, 21), datetime.date(2000, 6, 21)): 'Близнецы',  
    (datetime.date(2000, 6, 22), datetime.date(2000, 7, 22)): 'Рак',  
    (datetime.date(2000, 7, 23), datetime.date(2000, 8, 23)): 'Лев',  
    (datetime.date(2000, 8, 24), datetime.date(2000, 9, 23)): 'Дева',  
    (datetime.date(2000, 9, 24), datetime.date(2000, 10, 23)): 'Весы',  
    (datetime.date(2000, 10, 24), datetime.date(2000, 11, 22)): 'Скорпион',  
    (datetime.date(2000, 11, 23), datetime.date(2000, 12, 21)): 'Стрелец',  
    (datetime.date(2000, 12, 22), datetime.date(2001, 1, 20)): 'Козерог',  
    (datetime.date(2001, 1, 21), datetime.date(2001, 2, 20)): 'Водолей',  
    (datetime.date(2001, 2, 21), datetime.date(2001, 3, 20)): 'Рыбы',  
}


def get_user_zodiac_sign(user_data_birth: datetime.date) -> str:
    for interval in ZODIAC_INTERVALS:
        if interval[0] <= user_data_birth <= interval[1]:
            return ZODIAC_INTERVALS[interval]
        
        
def get_user_clear_gender(user: DatingUser) -> str:
    match user.gender:
        case 'ML':
            return 'мужской'
        case 'FL':
            return 'женский'
        case _:
            return 'не указан' 