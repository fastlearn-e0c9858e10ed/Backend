# To run the app locally


## Without Docker
Create a new python virtual environment:
`python -m venv .venv`

Start that virtual environment (Windows instruction):
`.venv\Scripts\activate`

Install the python dependencies:
`pip install -r requirements.txt`

Start the Flask server:
`uvicorn api.main:app --reload`

Check the output for what port you should navigate to. It defaults to http://localhost:8000/

## With Docker

Requires Docker to be preinstalled and running on your computer

### Run just the docker container
Run all these commands from the repo root:

1. Build and run the container:
   `docker build . -t fastapi`

2. Run the Docker container:
   `docker run --rm -p 8000:8000 fastapi`

    The -p 8000:8000 option in the docker run command maps the container's port 5000 to your machine's port 5000, so you can access the app at http://localhost:8000/.

3. Navigate to http://localhost:8000/ in your web browser to access the application.

### Run the full server
From the repo root:
1. Run `docker compose up --build`
1. You can access the app at http://localhost:8000/

This launches everything defined in `docker-compose.yml`