#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r"body)
channel.basic_consume(on_message_callback=callback,
                      queue='hello',
                      auto_ack=True
                      )
print("Waiting for messages")
channel.start_consuming()