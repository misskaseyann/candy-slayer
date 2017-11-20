class Observable(object):
    """Observable object."""
    def __init__(self):
        """Initializes with empty set of observers."""
        self.observers = []

    def register(self, observer):
        """
        Register an observer.

        :param observer: observer object to be add
        """
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        """
        Un-register an observer.

        :param observer: observer object to be removed
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        """Un-register all observers."""
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        """
        Update all observers.

        :param args: object
        :param kwargs: additional argument that can be passed
        """
        for observer in self.observers:
            observer.update(*args, **kwargs)
