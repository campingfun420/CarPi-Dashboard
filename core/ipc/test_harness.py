import logging
from ipc.message_schema import SetGearPayload, RadioMutedPayload
from ipc.messages import SetGearCommand, RadioMutedEvent


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("test_harness")


def test_set_gear_message():
    try:
        msg = SetGearCommand(
            source="gear_service",
            payload=SetGearPayload(gear="DRIVE"),
        )
        logger.info("SetGearCommand created successfully")
    except Exception as e:
        logger.error(f"SetGearCommand failed: {e}")

    try:
        msg = SetGearCommand(
            source="gear_service",
            payload=SetGearPayload(gear="INVALID"),
        )
        logger.error("Invalid SetGearCommand did NOT fail")
    except Exception as e:
        logger.info(f"Correctly blocked invalid message: {e}")


def test_radio_muted_message():
    try:
        msg = RadioMutedEvent(
            source="radio_service",
            payload=RadioMutedPayload(muted=True),
        )
        logger.info("RadioMutedEvent created successfully")
    except Exception as e:
        logger.error(f"RadioMutedEvent failed: {e}")

    try:
        msg = RadioMutedEvent(
            source="radio_service",
            payload=RadioMutedPayload(muted="yes"),
        )
        logger.error("Invalid RadioMutedEvent did NOT fail")
    except Exception as e:
        logger.info(f"Correctly blocked invalid message: {e}")


if __name__ == "__main__":
    test_set_gear_message()
    test_radio_muted_message()
