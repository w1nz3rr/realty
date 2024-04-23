import datetime

class Message:

    message_id: int
    chat_id: int
    sender_id: int
    message: str
    create_at: datetime.datetime
    update_at: datetime.datetime


class Chat:
    chat_id: int
    announcement_id: int
    buyer_id: int

class Blacklist:
    record_id: int
    sender_id: int
    user_id: int

class Complaint:
    complaint_id: int
    sender_id: int
    user_id: int
    reason: str
    description: str
    create_at: datetime.datetime

class Requisite:
    requisite_id: int
    user_id: int
    BIC: str
    recipient: str