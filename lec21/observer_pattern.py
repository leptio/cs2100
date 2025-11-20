#could use push method: producer as primary pushing to consumer
#works if info updates rarely and lots of people need it
#also known as observer pattern / publish-subscribe pattern

class Consumer:
    def __init__(self) -> None:
        self.needed_data = 0
    
    def receive_notification(self, data_value: int) -> None:
        self.needed_data = data_value
    
    def do_some_work(self) -> None:
        self.do_something(self.needed_data)
    
    def do_something(self, input:int) -> None:
        #Placeholder for actual work
        pass

class Producer:
    def __init__(self, local_consumer: Consumer) -> None:
        self.consumer = local_consumer
        self.the_data = 0
    
    def do_something_with_input(self, input_value: int) -> int:
        #placeholder processing step
        return input_value * 2
    
    def update_data(self, input_value: int) -> None:
        self.the_data = self.do_something_with_input(input_value)
        self.consumer.receive_notification(self.the_data)


if __name__ == "__main__":
    consumer = Consumer()
    producer = Producer(consumer)
    for value in [1,5,10]:
        print(f"Producer receives input: {value}")
        producer.update_data(value)
        consumer.do_some_work()
