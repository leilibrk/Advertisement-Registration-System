import json

import pika, sys, os
from tagging import tag
from mail import send_email
from save_to_DB import saveToDB

AMQP_URL = "amqps://raqdycjp:Ee4hbbWKYGfrLgjo94N5gMuxyoykLT50@hawk.rmq.cloudamqp.com/raqdycjp"
bucket_url = 'https://adv-images-cloud.s3.amazonaws.com/'


def main():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='adv_ids')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        # image url from s3
        image_id = str(body).replace('b', '').replace('\'', '')
        image_url = bucket_url + image_id + '.png'
        # send it to tagging system
        state, category = tag(image_url)
        saveToDB(state, category, image_id)
        # send email
        req = send_email(state, image_id)
        print(req)

    channel.basic_consume(queue='adv_ids', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
