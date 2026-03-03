import logging

logger = logging.getLogger("capability_negotiation")

class CapabilityNegotiation:
    """
    Handles negotiation of service capabilities between nodes.
    """

    def __init__(self):
        self._capabilities = {}

    def register_capability(self, service_name: str, capabilities: dict):
        self._capabilities[service_name] = capabilities
        logger.info(f"Registered capabilities for {service_name}: {capabilities}")

    def get_capabilities(self, service_name: str) -> dict:
        return self._capabilities.get(service_name, {})

    def negotiate(self, remote_caps: dict) -> dict:
        """Return intersection of local and remote capabilities."""
        negotiated = {}
        for service, caps in self._capabilities.items():
            if service in remote_caps:
                negotiated[service] = {
                    k: v for k, v in caps.items() if k in remote_caps[service]
                }
        logger.info(f"Negotiated capabilities: {negotiated}")
        return negotiated
