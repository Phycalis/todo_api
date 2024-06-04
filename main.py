from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.endpoints.todos import router

app = FastAPI()


# Обработчик глобальных исключений, который "ловит" все необработанные исключения
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "hueta"}
    )


app.include_router(router)
