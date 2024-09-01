import time

from app.exceptions import GenericException
from app.exceptions.validation_exceptions import MissingRequiredField
from app.responses.error import ErrorResponse
from app.routers import admin_resource, booking_resource, user_resource
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_reader, prod_others_db_writer
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException as StarletteException

log = logger()
server = FastAPI()

server.include_router(admin_resource.router)
server.include_router(booking_resource.router)
server.include_router(user_resource.router)


@server.on_event("shutdown")
async def app_shutdown():
    prod_others_db_reader.close()
    prod_others_db_writer.close()


@server.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time_ms = "{:.3f}".format((time.time() - start_time) * 1000)
    log.debug(
        event="Processed Request",
        path=request.url.path,
        duration_ms=process_time_ms,
        query_params=request.query_params,
        path_params=request.path_params,
    )
    response.headers["x-response-time-ms"] = process_time_ms
    return response


@server.exception_handler(StarletteException)
async def http_exception_handler(request: Request, ex: StarletteException):
    log.error(event="Api failed", status_code=ex.status_code, detail=ex.detail)
    params = {"q": request.query_params.__str__(), "path": request.url.__str__()}
    context = ErrorResponse.builder(ex)
    return ORJSONResponse(status_code=ex.status_code, content=context)


@server.exception_handler(GenericException)
async def generic_exception_handler(request: Request, ex: GenericException):
    return ORJSONResponse(status_code=ex.status_code, content=ErrorResponse.builder(ex))


@server.exception_handler(Exception)
async def exception_handler(request: Request, ex: Exception):
    params = {"q": request.query_params.__str__(), "path": request.url.__str__()}
    json_response = ErrorResponse.builder(ex)
    return ORJSONResponse(status_code=500, content=json_response)


@server.exception_handler(RuntimeError)
async def runtime_error_handler(request: Request, ex: RuntimeError):
    params = {"q": request.query_params.__str__(), "path": request.url.__str__()}
    json_response = ErrorResponse.builder(ex)
    return ORJSONResponse(status_code=500, content=json_response)


@server.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()
    # Returning the first validation error.
    raise MissingRequiredField(
        field=".".join([str(each) for each in details[0]["loc"]])
    )
