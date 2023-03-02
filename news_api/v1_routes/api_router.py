import logging

from pydantic import BaseModel, Field, conint, validator
from fastapi import APIRouter, HTTPException, Depends, Query, Request
from fastapi import HTTPException
# from sqlalchemy.orm import Session


router = APIRouter()

logger = logging.getLogger(__name__)

# @router.post("/basic-agency", status_code=201, response_model=ReturnUrlWrapper)
# async def post_basic_agency(agency: BasicAgencyPayload, background_tasks: BackgroundTasks,
#                             crud: RedisCrud = Depends(get_crud), settings: Settings = Depends(get_settings)):
#     job_id = str(uuid.uuid4())
#     background_tasks.add_task(process_basic_agency, agency, crud, job_id)
#     return ReturnUrlWrapper(return_url=f"{settings.BASE_URL}{IMPORT_AGENCIES_PREFIX}/results?uuid={job_id}")
#


# async def get_all_news(settings: Settings = Depends(get_settings),
#                        client: BigQueryDataStore = Depends(get_big_query_data_store)):
#     return client.session.query(Articles).all()

class Article(BaseModel):
    body: str
    author: str
    headline: str
    url: str
    genre: str


@router.get("/news")
def get_all_news():
    return Article(body="body2", author="author", headline="headline", url="url", genre="genre")


@router.post("/", status_code=201)
def save_article(request: Request, payload: Article):
    return Article.parse_raw(payload.json())




