from typing import List, Tuple
from usps_lib.track_field_request import TrackFieldRequest, TrackIDType
from usps_lib.track_response import TrackInfoType, TrackDetailType
from karrio.core.utils import Serializable, Element, XP, DF, SF
from karrio.core.models import (
    TrackingRequest,
    Message,
    TrackingDetails,
    TrackingEvent,
)
from karrio.providers.usps.error import parse_error_response
from karrio.providers.usps import Settings


def parse_tracking_response(
    response: Element, settings: Settings
) -> Tuple[List[TrackingDetails], List[Message]]:
    tracks_info = response.xpath(".//*[local-name() = $name]", name="TrackInfo")
    details = [
        _extract_details(node, settings)
        for node in tracks_info
        if len(node.xpath(".//*[local-name() = $name]", name="TrackDetail")) > 0
    ]

    return details, parse_error_response(response, settings)


def _extract_details(node: Element, settings) -> TrackingDetails:
    info = XP.to_object(TrackInfoType, node)
    details: List[TrackDetailType] = [*([info.TrackSummary] or []), *info.TrackDetail]
    delivered = info.StatusCategory.lower() == "delivered"
    expected_delivery = info.ExpectedDeliveryDate or info.PredictedDeliveryDate

    return TrackingDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        tracking_number=info.ID,
        delivered=delivered,
        events=[
            TrackingEvent(
                code=str(event.EventCode),
                date=DF.fdate(event.EventDate, "%B %d, %Y"),
                time=DF.ftime(event.EventTime, "%H:%M %p"),
                description=event.Event,
                location=SF.concat_str(
                    event.EventCity,
                    event.EventState,
                    event.EventCountry,
                    str(event.EventZIPCode or ""),
                    join=True,
                    separator=", ",
                ),
            )
            for event in details
        ],
        estimated_delivery=DF.fdate(expected_delivery, "%B %d, %Y"),
    )


def tracking_request(
    payload: TrackingRequest, settings: Settings
) -> Serializable[TrackFieldRequest]:
    request = TrackFieldRequest(
        USERID=settings.username,
        Revision="1",
        ClientIp="127.0.0.1",
        SourceId="Karrio",
        TrackID=[
            TrackIDType(ID=tracking_number, DestinationZipCode=None, MailingDate=None)
            for tracking_number in payload.tracking_numbers
        ],
    )
    return Serializable(request, _request_serializer, logged=True)


def _request_serializer(request: TrackFieldRequest) -> str:
    return XP.export(request)
