"""Karrio DHL client settings."""

import attr
from karrio.providers.dhl_express.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """DHL connection settings."""

    site_id: str
    password: str
    account_number: str = None
    account_country_code: str = None

    id: str = None
    test: bool = False
    carrier_id: str = "dhl_express"
