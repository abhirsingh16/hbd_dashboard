from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Base for SQLAlchemy models
Base = declarative_base()

class MasterInput(Base):
    __tablename__ = 'master_input'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)
    area = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    phone_no_1 = Column(String(255), nullable=True)
    phone_no_2 = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)
    ratings = Column(String(255), nullable=True)
    extra_column3_type_of_products = Column(String(255), nullable=True)
    extra_column10_type_of_course = Column(String(255), nullable=True)
    sub_category = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    extra_column6_Source_File = Column(String(255), nullable=True)
    extra_column1_ifsc = Column(String(255), nullable=True)
    extra_column5_micr = Column(String(255), nullable=True)
    extra_column9_branch_code = Column(String(255), nullable=True)
    extra_column7_branch = Column(String(255), nullable=True)
    extra_column8_Address = Column(String(255), nullable=True)
    extra_column2_district = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    extra_column4_avg_fees = Column(String(255), nullable=True)
    latitude = Column(String(255), nullable=True)
    longitude = Column(String(255), nullable=True)
    reviews = Column(String(255), nullable=True)
    facebook_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    twitter_url = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    pincode = Column(String(255), nullable=True)
    virtual_phone_no = Column(String(255), nullable=True)
    whatsapp_no = Column(String(255), nullable=True)
    phone_no_3 = Column(String(255), nullable=True)
    avg_spent = Column(String(255), nullable=True)
    cost_for_two = Column(String(255), nullable=True)
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    


 