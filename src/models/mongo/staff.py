from src.models.mongo.base_model import BaseModel


class StaffCollection(BaseModel):
    """
        Danh sách nhân viên
    """

    def __init__(self):
        super().__init__()
        self.collection_name = 'nhanvien'

