import os
from quixstreams import Application
import json

# for local dev, load env vars from a .env file
from dotenv import load_dotenv
load_dotenv()

def main():

    app = Application(consumer_group="chennai-weather",auto_offset_reset="latest")

    input_topic = app.topic(os.environ["input"])
    #print(input_topic.name)
    output_topic = app.topic(os.environ["output"])

    with app.get_consumer() as consumer:
        consumer.subscribe([input_topic.name])

        while True:
            msg=consumer.poll(1)

            if msg is None:
                print("waiting...")
            elif msg.error() is not None:
                raise Exception(msg.error())
            else:
                key = msg.key().decode('utf8')
                value = json.loads(msg.value())
                offset = msg.offset()
                consumer.store_offsets(msg)


#sdf = app.dataframe(input_topic)

# put transformation logic here
# see docs for what you can do
# https://quix.io/docs/get-started/quixtour/process-threshold.html

#sdf.print()
#sdf.to_topic(output_topic)

if __name__ == "__main__":
    main()