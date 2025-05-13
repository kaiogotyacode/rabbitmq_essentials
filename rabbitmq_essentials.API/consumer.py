import pika

class RabbitMQConsumer:
    def __init__(self, callback):
        self.__host = "localhost"
        self.__port = 15672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host = self.__host,
            port = self.__port,
            credentials = pika.PlainCredentials(self.__username, self.__password)
        )

        channel = pika.BlockingConnection(connection_parameters).channel()

        channel.queue_declare(
            queue = self.__queue,
            durable = True
        )

        channel.basic_consume(
            queue = self.__queue,
            auto_ack = True,
            on_message_callback = self.__callback
        )

        return channel

    def start(self):            
        print('Listening to RabbitMQ on Port 5672')
        self.__channel.start_consuming()

def callback_function(ch, method, properties, body):
    print(body)

rabbitmq_consumer = RabbitMQConsumer(callback_function)
rabbitmq_consumer.start()