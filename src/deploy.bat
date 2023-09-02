pipenv run python build\pyboard.py --device COM3 -f rm "*.py"
pipenv run python build\pyboard.py --device COM3 -f cp neopixel.py light.py credentials.py timesource.py main.py :
pipenv run python build\pyboard.py --device COM3 --no-follow -c "import machine; machine.reset()"
pipenv run python build\pyboard.py --device COM3 --follow
pause
