# Trying to reproduce https://github.com/robinhood/faust/issues/445

**Result: No error. Works as expected**

Steps to reproduce (need 3 terminals)

1. Terminal: start kafka (root of the repo)

```bash
# give it a bit of time to start
docker-compose up kafka
```

2. Terminal: start woker

```bash
cd tableofset_issue_445
pipenv install
pipenv run faust -A tableofset
```

3. Terminal: commands

```bash
cd tableofset_issue_445
pipenv run faust -A tableofset joining here sergej
```
