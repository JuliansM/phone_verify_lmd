from constants.cors_headers import CORS_HEADERS

class SuccessResponseBuilder:
    @staticmethod
    def build_response(phone_number: str, country_code: str | None):
        response_body = {
            "valid": country_code is not None,
            "number": f"+57{phone_number}" if country_code else phone_number,
            "local_format": f"0X, 04XX{phone_number}" if country_code else "",
            "international_format": f"+57{phone_number}" if country_code else "",
            "country_prefix": "+57" if country_code else "",
            "country_code": country_code if country_code else "",
            "country_name": "Colombia (Republic of)" if country_code else "",
            "location": "",
            "carrier": "Comunicacion Celular SA (COMCEL)" if country_code else "",
            "line_type": "mobile" if country_code else None
        }
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": response_body
        }
