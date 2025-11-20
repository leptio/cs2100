from abc import ABC, abstractmethod

class IPushingClock(ABC):
    @abstractmethod
    def reset(self) -> None:
        """Resets the time to 0."""
        pass

    @abstractmethod
    def tick(self) -> None:
        """Increments the time and sends a notification with the
        current time to all consumers."""
        pass

    @abstractmethod
    def add_listener(self, listener: 'IPushingClockClient') -> int:
        """Adds another consumer and initializes it with the current time."""
        pass

class IPushingClockClient(ABC):
    @abstractmethod
    def receive_notification(self, t: int) -> None:
        """Notifies the client with the current time."""
        pass

# Producer
class PushingClock(IPushingClock):
    def __init__(self) -> None:
        self.observers: list[IPushingClockClient] = []
        self.time = 0

    def add_listener(self, listener: 'IPushingClockClient') -> int:
        self.observers.append(listener)
        return self.time

    def notify_all(self) -> None:
        for obs in self.observers:
            obs.receive_notification(self.time)

    def reset(self) -> None:
        self.time = 0
        self.notify_all()

    def tick(self) -> None:
        self.time += 1
        self.notify_all()

# Consumer
class PushingClockClient(IPushingClockClient):
    def __init__(self, the_clock: IPushingClock) -> None:
        self.time = the_clock.add_listener(self)

    def receive_notification(self, t: int) -> None:
        self.time = t
    
    def __str__(self) -> str:
        return f"Current clock time: {self.time}"

    
if __name__ == "__main__":
    clock = PushingClock()
    PushingClockClient1 = PushingClockClient(clock)
    PushingClockClient2 = PushingClockClient(clock)

    print("Initial:")
    print(PushingClockClient1, PushingClockClient2)

    for _ in range(3):
        clock.tick()
        print("After tick:")
        print(PushingClockClient1, PushingClockClient2)

    clock.reset()
    print("After reset:")
    print(PushingClockClient1, PushingClockClient2)
