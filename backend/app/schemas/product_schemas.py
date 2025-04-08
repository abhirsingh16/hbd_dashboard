from pydantic import BaseModel
from typing import Optional, List

class MasterInputBase(BaseModel):
    id: Optional[int] = None
    category: Optional[str] = None
    city: Optional[str] = None
    name: Optional[str] = None
    area: Optional[str] = None
    address: Optional[str] = None
    phone_no_1: Optional[str] = None
    phone_no_2: Optional[str] = None
    url: Optional[str] = None
    ratings: Optional[str] = None
    extra_column3_type_of_products: Optional[str] = None
    extra_column10_type_of_course: Optional[str] = None
    sub_category: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    extra_column6_Source_File: Optional[str] = None
    extra_column1_ifsc: Optional[str] = None
    extra_column5_micr: Optional[str] = None
    extra_column9_branch_code: Optional[str] = None
    extra_column7_branch: Optional[str] = None
    extra_column8_Address: Optional[str] = None
    extra_column2_district: Optional[str] = None
    email: Optional[str] = None
    extra_column4_avg_fees: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    reviews: Optional[str] = None
    facebook_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    twitter_url: Optional[str] = None
    description: Optional[str] = None
    pincode: Optional[str] = None
    virtual_phone_no: Optional[str] = None
    whatsapp_no: Optional[str] = None
    phone_no_3: Optional[str] = None
    avg_spent: Optional[str] = None
    cost_for_two: Optional[str] = None


    # This model is used to receive data (POST requests), 
    # while the following model is used for returning the data (GET requests).

    class Config:

        from_attributes = True    # This tells Pydantic to read data from ORM models (SQLAlchemy) and convert it to Pydantic models.



class PaginatedMasterInputResponse(BaseModel):
    data: List[MasterInputBase]
    total_records: int
    offset: int
    limit: int
    has_more: bool