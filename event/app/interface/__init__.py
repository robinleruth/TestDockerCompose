import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..domain.services.event_service.bean import get_event_service
from ..domain.services.event_store.bean import get_event_store

api = FastAPI(title='Token API',
              description='',
              version='0.1')

from .controllers import event_controller

api.include_router(event_controller.router,
                   prefix='/api/v1/event_controller',
                   tags=['event_controller'])

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def init_services():
    await get_event_store()
    await get_event_service()


asyncio.run(init_services())
