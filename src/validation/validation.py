from typing import Dict, List, Any
from pydantic import BaseModel, ValidationError
from utils.logger import log

class ValidatedData(BaseModel):
    company_name: str
    job_name: str
    job_location: str
    job_type: str
    job_date_creation: str
    job_link: str

class DataValidator:
    @staticmethod
    def result_validation(list_dict_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        validated_data = []

        for item in list_dict_data:
            try:
                ValidatedData(**item)
                validated_data.append(item)
            except ValidationError as e:
                log().error(f"Validation error: {e}")

        if not validated_data:
            log().info("No valid job data found")
        else:
            log().info("Validation Completed!")

        return validated_data