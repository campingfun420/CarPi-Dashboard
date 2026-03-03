class EventDispatcher:
    def init(self, capability_manager):
        self._handlers = {}
        self.capability_manager = capability_manager

    def register(self, capability, handler_fn):
        if capability not in self._handlers:
            self._handlers[capability] = []
        self._handlers[capability].append(handler_fn)

    def dispatch(self, event):
        capability = event.get('capability')
        if not capability:
            return
        handlers = self._handlers.get(capability, [])
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                print(f"Error handling event: {e}")
import threading
import heapq
from concurrent.futures import ThreadPoolExecutor
from .messages import IPCMessage
import logging

logger = logging.getLogger("event_dispatcher")

class EventDispatcher:
    """
    Single-threaded event loop in its own thread with priority queue
    and parallel handler execution.
    """

    def __init__(self, worker_threads: int = 4):
        self._handlers = {}
        self._critical_queue = []
        self._normal_queue = []
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)
        self._running = False
        self._thread = None
        self._executor = ThreadPoolExecutor(max_workers=worker_threads)

    def register_handler(self, message_type: str, handler):
        if message_type not in self._handlers:
            self._handlers[message_type] = []
        self._handlers[message_type].append(handler)

    def publish(self, message: IPCMessage, priority: int = 50):
        with self._condition:
            if priority <= 10:
                heapq.heappush(self._critical_queue, (priority, message))
            else:
                heapq.heappush(self._normal_queue, (priority, message))
            self._condition.notify()

    def _dispatch(self, message: IPCMessage):
        handlers = self._handlers.get(message.message_type, [])
        for handler in handlers:
            self._executor.submit(handler, message)

    def _loop(self):
        while self._running:
            with self._condition:
                while not self._critical_queue and not self._normal_queue and self._running:
                    self._condition.wait()
                if not self._running:
                    break
                if self._critical_queue:
                    _, message = heapq.heappop(self._critical_queue)
                else:
                    _, message = heapq.heappop(self._normal_queue)
            self._dispatch(message)

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        with self._condition:
            self._condition.notify_all()
        if self._thread:
            self._thread.join()
        self._executor.shutdown(wait=True)
