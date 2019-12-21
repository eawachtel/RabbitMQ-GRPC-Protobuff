import pika
import json
from protobuff_files.test_pb2 import Number


class RabbitMQConsumer:

    def __init__(self, host='localhost', queue='hello'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue)
        self.channel.basic_consume(queue, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        message = Number()
        message.ParseFromString(body)
        # steer = int(message['steer'])
        print(" [x] Received %r" % message.steer)
        return ['message recieved']



if __name__ == "__main__":
    print(' [*] Waiting for messages. To exit press CTRL+C')
    rabbitmq = RabbitMQConsumer()
    consume = rabbitmq.callback()



