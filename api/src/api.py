from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.ConfigDB import origins
from .routes.Routes import routes

description = """

## Introduction
The objective of this repository is to create a standard project with fastapi and angular with good design patterns \n
and that can be used as a standard for other projects
"""

app = FastAPI(
    title="Ecommerce Application",
    description=description,
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in routes:
    app.include_router(route.router) 