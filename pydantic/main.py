from datetime import datetime
from pydantic import BaseModel

class Event(BaseModel):#型定義をしっかり管理したいとき
    
    name:str = "未定"
    
    start_datetime: datetime
    prticipants: list[str] = []