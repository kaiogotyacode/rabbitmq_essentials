import pika



# RabbitMQ interpreta a mensagem principal como Bytes por default.
# It was necessary to install Erland/OTP to use RabbitMQ on Windows.
# Installation: https://www.rabbitmq.com/docs/install-windows#installer
# Start RabbitMQ Service

# Starting RabbitMQ:
# run cmd command: rabbitmq-plugins enable rabbitmq_management
# if this don't work properly: go to your rabbitmq installation path, example: cd C:\Program Files\RabbitMQ Server\rabbitmq_server-4.1.0\sbin
# then, run once again: rabbitmq-plugins enable rabbitmq_management
# now restart rabbitmq service in your machine. You can do that by console (IDK Command) or you can open win + r :: services.msc stop and start manually RabbitMQ
# go to http:localhost:15672, it should work now.