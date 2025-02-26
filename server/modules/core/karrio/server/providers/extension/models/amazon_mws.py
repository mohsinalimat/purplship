from django.db import models
from karrio.server.providers.models.carrier import Carrier


class AmazonMwsSettings(Carrier):
    CARRIER_NAME = "amazon_mws"

    class Meta:
        db_table = "amazon_mws-settings"
        verbose_name = "AmazonMws Settings"
        verbose_name_plural = "AmazonMws Settings"

    access_key = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)
    aws_region = models.CharField(max_length=200, default="us-east-1")

    @property
    def carrier_name(self) -> str:
        return self.CARRIER_NAME

    @property
    def x_amz_access_token(self) -> str:
        return ""  # Setup the access token here.


SETTINGS = AmazonMwsSettings
