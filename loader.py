from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Environment variables not loaded because .env file is missing')
else:
    load_dotenv()
