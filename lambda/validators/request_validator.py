class RequestValidator:
    @staticmethod
    def validate_params(params: dict):
        if not params.get("access_key"):
            raise ValueError("invalidAccessKey")
        if not params.get("number"):
            raise ValueError("invalidPhone")
        if not params.get("country_code"):
            raise ValueError("invalidCountryCode")
