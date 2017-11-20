from abc import ABCMeta, abstractmethod


class Observer(object):
    """Observer object abstract."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        """Observable updates the observer."""
        pass
