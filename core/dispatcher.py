class Dispatcher:
    def __init__(self, initial_state, reducer, effects, logger):
        self.state = initial_state
        self.reducer = reducer
        self.effects = effects
        self.logger = logger
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def unsubscribe(self, callback):
        if callback in self.subscribers:
            self.subscribers.remove(callback)

    def dispatch(self, event):
        old_state = self.state
        if self.logger:
            self.logger.log(event)
        new_state = self.reducer(old_state, event)
        if self.effects:
            self.effects.handle(old_state, new_state, event)
        for subscriber in self.subscribers:
            subscriber(old_state, new_state, event)
        self.state = new_state
        return new_state
