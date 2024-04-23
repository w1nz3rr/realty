import datetime

class Deal:
    deal_id: int
    buyer_id: int
    seller_id: int
    realtor_id: int
    object_id: int
    lawyer_id: int
    type_deal: str
    notary_id: int
    term: str
    conditions: str
    price: int
    create_at: datetime.datetime
