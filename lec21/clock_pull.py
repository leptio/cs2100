from abc import ABC, abstractmethod

class IPullingClock(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def tick(self) -> None:
        pass

    @abstractmethod
    def get_time(self) -> int:
        pass

class SimpleClock(IPullingClock):
    def __init__(self) -> None:
        self.time = 0

    def reset(self) -> None:
        self.time = 0

    def tick(self) -> None:
        self.time +=1

    def get_time(self) -> int:
        return self.time

class ClockClient:
    def __init__(self, the_clock: IPullingClock):
        self.the_clock = the_clock

    def get_time_from_clock(self) -> int:
        return self.the_clock.get_time()

if __name__ == "__main__":
    clock = SimpleClock()
    clock_client = ClockClient(clock)
    for _ in range(3):
        clock.tick()
        print(f"Clock time pulled from producer: {clock_client.get_time_from_clock()}")

