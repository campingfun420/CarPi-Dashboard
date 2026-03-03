import threading
import time
import logging

logger = logging.getLogger("heartbeat")

class HeartbeatMonitor:
    """
    Periodically sends heartbeat events and checks liveness of services.
    """

    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self._running = False
        self._thread = None
        self._subscribers = []

    def subscribe(self, callback):
        self._subscribers.append(callback)

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        logger.info("Heartbeat monitor started")

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()
        logger.info("Heartbeat monitor stopped")

    def _loop(self):
        while self._running:
            for callback in self._subscribers:
                try:
                    callback(time.time())
                except Exception as e:
                    logger.error(f"Heartbeat subscriber error: {e}")
            time.sleep(self.interval)
