import datetime

class Announcement:
    announcement_id: int
    seller_id: int
    object_id: int
    title: str
    description: str
    create_at: datetime.datetime
    update_at: datetime.datetime

class Review:
    review_id: int
    announcement_id: int
    buyer_id: int
    estimation: int
    description: str
    create_at: datetime.datetime

class Favorites:
    favorite_id: int
    announcement_id: int
    user_id: int
    create_at: int


