from builders.error_response_builder import ErrorResponseBuilder
from builders.success_response_builder import SuccessResponseBuilder
from validators.request_validator import RequestValidator

QUERY_STRING_PARAMETERS = "queryStringParameters"

def handler(event, ctx):
    if QUERY_STRING_PARAMETERS not in event:
        return ErrorResponseBuilder.build_error_response("invalidAccessKey")
    
    params = event.get(QUERY_STRING_PARAMETERS)
    
    try:
        RequestValidator.validate_params(params)
        return SuccessResponseBuilder.build_response(params["number"], params.get("country_code"))
    except ValueError as e:
        return ErrorResponseBuilder.build_error_response(str(e))
