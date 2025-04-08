from sqlalchemy.orm import Session
from backend.app.schemas.master_input import MasterInput
# from backend.app.schemas.product_schemas import MasterInputBase
from backend.app.database.session import SessionLocal
from sqlalchemy import select
from fastapi import APIRouter, HTTPException, Depends
from backend.app.database.session import get_db_session
import logging


def read_master_input(
    session: Session = Depends(get_db_session),
    page: int = 1,
    limit: int = 100
):
    offset = (page - 1) * limit
    
    try:
        # Fetch paginated data
        result = session.query(MasterInput).offset(offset).limit(limit).all()
        
        # Total records for pagination
        total_records = session.query(MasterInput).count()
        
        # Check if there are more pages
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
