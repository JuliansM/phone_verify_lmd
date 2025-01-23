from constants.cors_headers import CORS_HEADERS
from constants.errors import ERRORS

class ErrorResponseBuilder:
    @staticmethod
    def build_error_response(error: str):
        return {
            "statusCode": ERRORS[error]["code"],
            "headers": CORS_HEADERS,
            "body": {
                "success": False,
                "error": ERRORS[error]
            }
        }
    