from src.models.mongo.base_model import BaseModel


class DealCollection(BaseModel):
    """
        Danh sách công việc
    """

    def __init__(self):
        super().__init__()
        self.collection_name = 'congviec'
