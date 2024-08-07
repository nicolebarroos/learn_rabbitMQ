import pika

connection_parameters = pika.ConnectionParameters(
    host = "localhost",
    port = 5673,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="Teste22",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)