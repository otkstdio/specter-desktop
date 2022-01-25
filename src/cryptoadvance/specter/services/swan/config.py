"""
Swan API uses PKCE OAuth2. Per Swan's API team: The client secret here is not considered
to be a real secret. There is no reasonable attack vector for this secret being public.
"""


class BaseConfig:
    SWAN_CLIENT_ID = "specter-dev"
    SWAN_CLIENT_SECRET = (
        "BcetcVcmueWf5P3UPJnHhCBMQ49p38fhzYwM7t3DJGzsXSjm89dDR5URE46SY69j"
    )
    SWAN_API_URL = "https://dev-api.swanbitcoin.com"


class ProductionConfig(BaseConfig):
    SWAN_CLIENT_ID = "specter"
    SWAN_CLIENT_SECRET = (
        "UcqMZw3D70#E*Zo1hnC8f8P^Ils^6wligXMB*vL1fX@DYm6zloDI#p9Eemk8!y9#"
    )
    SWAN_API_URL = "https://api.swanbitcoin.com"