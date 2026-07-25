from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_target(self, target):
        pass

    @abstractmethod
    def compute_control(self, robot, dt):
        pass