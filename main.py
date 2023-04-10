from decouple import config
import openai

from Server.server import create_server

openai.api_key = config("OPENAI_KEY")

create_server()
