# Trying to get a windowed table by key

Steps to reproduce

1. Terminal: start kafka (root of the repo)

```bash
# give it a bit of time to start
docker-compose up kafka
```

2. Terminal: start woker

```bash
cd window_key_bug
pipenv install
pipenv run faust -A app
```

See as output all keys (up and down) of topic, even though only one was asked for
