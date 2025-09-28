# Agentic-Experiments

## Setting up Venv
python3 -m venv .venv
source .venv/bin/activate

## Handy Commands
docker build -t python-autogen .

### Unix/Linux
docker run -v $(pwd):/app -w /app python-autogen:latest python my_script.py
### Windows
docker run -v ${pwd}:/app -w /app python-autogen:latest python my_script.py

- Run but delete once done
- `docker run --rm -v G:\Docker\UserImages\Agentic-Experiments\AutoGen\app:/app -w /app python-autogen:latest python my_script.py`

- Run with specific name
- `docker run --name autogen-test -v G:\Docker\UserImages\Agentic-Experiments\AutoGen\app:/app -w /app python-autogen:latest python my_script.py`
- Run Specific one again
- `docker start -ai autogen-test`



docker run --rm -p 8081:8081 -v G:\Docker\UserImages\Agentic-Experiments\UserData:/data -w /data python-autogen:latest autogenstudio ui --host 0.0.0.0 --port 8081 --appdir /data

docker run --name autogen-test -v /media/akbis/drive/dev/Agentic-Experiments/CrewUserData:/data -w /app python-crew:latest python my_script.py

docker run --rm -v /media/akbis/drive/dev/Agentic-Experiments/CrewUserData:/data -w /app python-crew:latest python app.py
docker build -t python-autogen /media/akbis/drive/dev/Agentic-Experiments/Crew && docker run --rm -v /media/akbis/drive/dev/Agentic-Experiments/CrewUserData:/data -w /app python-crew:latest python app.py
