from csv_source import CsvSource
from quixstreams import Application
import os
import requests
import json
import time

# import the dotenv module to load environment variables from a file
from dotenv import load_dotenv
load_dotenv(override=False)

def get_weather():
    response = requests.get("https://api.open-meteo.com/v1/forecast",
                            params={
                                "latitude": 13.0878,
                                "longitude": 80.2785,
                                "current": "temperature_2m",
                            },)
    
    return response.json()

def main():
    # Create an Application.
    app = Application()

    # Define the topic using the "output" environment variable
    topic_name = os.getenv("output", "")
    if topic_name == "":
        raise ValueError("The 'output' environment variable is required. This is the output topic that data will be published to.")

    topic = app.topic(topic_name)

    i=0

    with app.get_producer() as producer:
        while i<100:
            weather=get_weather()
            producer.produce(
                topic=topic.name,
                key="chennai",
                value=json.dumps(weather),
            )
            i+=1
            time.sleep(10)

#csv_source = CsvSource("demo-data.csv", sleep_between_rows=0.2)
#sdf = app.dataframe(source=csv_source)
#output_topic = app.topic(topic_name)

#sdf.print()
#sdf.to_topic(output_topic)


if __name__ == "__main__": 
    main()