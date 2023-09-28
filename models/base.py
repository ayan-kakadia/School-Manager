class ObservableModel:
    def __init__(self):
        self._event_listeners = {}

    def add_event_listener(self, event, fn):
        if event in self._event_listeners:
            self._event_listeners[event].append(fn)
        else:
            self._event_listeners[event] = [fn]

    def trigger_event(self, event):
        if not event in self._event_listeners:
            return

        for fn in self._event_listeners[event]:
            fn(self)
