import pika
from protobuff_files.test_pb2 import Number


class RabbitMQProducer:

    def __init__(self, queue='hello'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue)

    """ Infinate loop counting up to produce test message"""
    def data(self):
        x = 0
        while True:
            x = x + 1
            x
            test = self.produce(x)
        return ['data sent']

    def produce(self, x):
        message = Number()
        message.steer = x
        message2 = message.SerializeToString()
        self.channel.basic_publish(exchange='',
                                   routing_key='hello',
                                   body=message2)
        print('message produced')
        return 'message produced'


if __name__ == "__main__":
    """Call rabbitMQProducer Class will loop through n = n+1 infinately."""
    rabbitmq = RabbitMQProducer()
    produce = rabbitmq.data()

