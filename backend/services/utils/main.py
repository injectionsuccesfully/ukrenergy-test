from sqlalchemy.orm import Session

class Service:
    def __init__(self, db: Session):
        self.db = db