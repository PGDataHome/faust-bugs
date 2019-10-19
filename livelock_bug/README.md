# Examples for missing commit / livelock issue

Steps to reproduce (need 4 terminals)

1. Terminal: start kafka (root of the repo)

```bash
# give it a bit of time to start
docker-compose up kafka
```

2. Terminal: start working v 1.7.4

```bash
cd livelock_bug/working_1_7_4
pipenv install
pipenv run python app.py
```

3. Terminal: start working v 1.8.0

```bash
cd livelock_bug/working_1_8_0
pipenv install
pipenv run python app.py
```

4. Terminal: start broken v 1.8.1

```bash
cd livelock_bug/working_1_8_1
pipenv install
pipenv run python app.py
```
