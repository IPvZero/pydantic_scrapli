"""
Define Models for Data Validation
"""

from ipaddress import IPv4Address
from typing import List, Optional
from pydantic import BaseModel, Field


class Peers(BaseModel):
    """Class for BGP Peer Configuration.
       Inherits from the BGPConfig class.

    Types:
        neighbor: BGP peer neighbor address. Must be valid IPv4 address.
        peer_asn: BGP peer autonomous system number. Must be an integer (Range: 1-65535).
    """

    neighbor: IPv4Address
    peer_asn: int = Field(gt=0, le=65536)


class BGPConfig(BaseModel):
    """Class for BGP Configuration.

    Types:
        asn: The local autonomous system number. Must be an integer (Range: 1-65535).
        peers: Remote BGP peer configurations. Must adhere to the types defined in Peers.
    """

    asn: int = Field(gt=0, le=65536)
    peers: Optional[List[Peers]]
