from typing import List
from pydantic import BaseModel, Field

from app.models.about import About
from app.models.add_ons import AddOns
from app.models.branch import Branch
from app.models.service import Service
from app.models.theatre import Theatre


class AllInfo(BaseModel):
    home_page_image: str = Field(min_length=5, frozen=True)
    branches: List[Branch]
    Theatres: List[Theatre]
    our_services: List[Service]
    about: About
    tnc: About
    refund_policy: About
    themes_supported: List[Service]
    cakes: List[AddOns]
    decoration: List[AddOns]
