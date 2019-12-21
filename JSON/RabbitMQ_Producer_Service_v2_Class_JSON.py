import pika
import json


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
            d = {"steer": "{}".format(x)}
            test = self.produce(d)
        return ['data sent']

    def produce(self, d):
        self.channel.basic_publish(exchange='',
                                   routing_key='hello',
                                   body=json.dumps(d))
        print('message produced')
        return 'message produced'


if __name__ == "__main__":
    """Call rabbitMQProducer Class will loop through n = n+1 infinately."""
    rabbitmq = RabbitMQProducer()
    produce = rabbitmq.data()

