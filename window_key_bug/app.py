from random import random
from datetime import timedelta
import faust

app = faust.App('window_key_broken_1_8_0', broker='kafka://localhost:9092')


class Model(faust.Record, serializer='json'):
    random: float


TOPIC = 'window_key_broken_1_8_0'

tumbling_topic = app.topic(TOPIC, value_type=Model)
tumbling_table = app.Table(
    'window_key_broken_1_8_0',
    default=int,
).tumbling(
    10,
    expires=timedelta(minutes=2),
)


@app.agent(tumbling_topic)
async def print_windowed_events(stream):
    async for _ in stream:
        tumbling_table['counter_up'] += 1
        tumbling_table['counter_down'] -= 1
        print("Counter processed")


@app.timer(2.0, on_leader=True)
async def publish_every_2secs():
    msg = Model(random=round(random(), 2))
    await tumbling_topic.send(value=msg)


@app.timer(2.0)
async def print_table():
    print(f"up: {list(tumbling_table['counter_up'].keys())}")
    print(f"down: {list(tumbling_table['counter_down'].keys())}")


if __name__ == '__main__':
    app.main()
