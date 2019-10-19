import faust


class Greeting(faust.Record):
    from_name: str
    to_name: str


app = faust.App('livelock_working_1_7', broker='kafka://localhost')
topic = app.topic('livelock_working_1_7', value_type=Greeting)
app.conf.store = 'memory://'
app.conf.web_port = 6099


@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Hello from {greeting.from_name} to {greeting.to_name}')


@app.timer(interval=1.0)
async def example_sender(app):
    await hello.send(
        value=Greeting(from_name='Faust', to_name='you'),
    )

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.argv.extend(['worker', '-l', 'info'])
    app.main()
