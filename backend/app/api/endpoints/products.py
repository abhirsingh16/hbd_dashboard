from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any
import logging

from backend.app.api.endpoints.crud import read_master_input
from backend.app.schemas.product_schemas import MasterInputBase
from backend.app.schemas.master_input import MasterInput
from backend.app.database.session import get_db_session

router = APIRouter()



@router.get("/read_master_input/")
def read_complete_data(
    session: Session = Depends(get_db_session),
    page: int = 1,
    limit: int = 100
):
    offset = (page - 1) * limit

    print(f"Fetching data with OFFSET: {offset}, LIMIT: {limit}")

    try:
        result = session.query(MasterInput).offset(offset).limit(limit).all()
        print(f"Fetched {len(result)} records with OFFSET {offset}")

        total_records = session.query(MasterInput).count()
        has_more = offset + limit < total_records

        if not result:
            raise HTTPException(status_code=404, detail="Data not found")
        
        return {
            "data": [record.as_dict() for record in result],
            "total_records": total_records,
            "offset": offset,
            "limit": limit,
            "has_more": has_more
        }
    except Exception as e:
        logging.error(f"Error fetching data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")




def record_to_dict(record):
    return {
        "id": record.id,
        "category": record.category,
        "city": record.city,
        "name": record.name,
        "area": record.area,
        "address": record.address,
        "phone_no_1": record.phone_no_1,
        "phone_no_2": record.phone_no_2,
        "url": record.url,
        "ratings": record.ratings,
        "sub_category": record.sub_category,
        "state": record.state,
        "country": record.country,
        "email": record.email,
        "latitude": record.latitude,
        "longitude": record.longitude,
        "reviews": record.reviews,
        "facebook_url": record.facebook_url,
        "linkedin_url": record.linkedin_url,
        "twitter_url": record.twitter_url,
        "description": record.description,
        "pincode": record.pincode,
        "virtual_phone_no": record.virtual_phone_no,
        "whatsapp_no": record.whatsapp_no,
        "phone_no_3": record.phone_no_3,
        "avg_spent": record.avg_spent,
        "cost_for_two": record.cost_for_two
    }
