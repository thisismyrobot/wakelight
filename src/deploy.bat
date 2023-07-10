pipenv run python build\pyboard.py --device COM4 -f cp neopixel.py :neopixel.py
pipenv run python build\pyboard.py --device COM4 -f cp light.py :light.py
pipenv run python build\pyboard.py --device COM4 -f cp credentials.py :credentials.py
pipenv run python build\pyboard.py --device COM4 -f cp timesource.py :timesource.py
pipenv run python build\pyboard.py --device COM4 -f cp main.py :main.py
pipenv run python build\pyboard.py --device COM4 --no-follow -c "import machine; machine.reset()"
pipenv run python build\pyboard.py --device COM4 --follow
pause