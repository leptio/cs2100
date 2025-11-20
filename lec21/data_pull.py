#producer/consumer problem
#subject = producer = publisher
#observer = consumer = subscriber = listener
#two solutions: broadcast to everyone (push) or have individual requests (pull)

#"data pull" pattern:

class Producer:
    def get_data(self) -> int:
        return 500

class Consumer:
    def __init__(self, producer: Producer):
        self.producer = producer

    def do_some_work(self) -> None:
        needed_data = self.producer.get_data()
        self.do_something(needed_data)

    def do_something(self, data:int) -> None:
        #Placeholder for actual work
        pass
