from fastapi import FastAPI

app = FastAPI(
    title="QuickStore API - Clean Architecture",
    description="The RESTAPI application documentation for QuickStore",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)
