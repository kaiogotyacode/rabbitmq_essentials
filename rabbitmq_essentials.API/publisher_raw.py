import pika

connection_parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(username='guest', password='guest')
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange='main_exchange',
    routing_key='',
    body='This is the body content.',
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)


# Conceito de delivery type - RabbitMQ 