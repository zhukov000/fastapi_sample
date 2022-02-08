from starlette.config import Config

config = Config(".env_dev")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="8e68b530c18e457da9ac7ff63b61ad96f91d7709f46fd951b78758ab3d90ed07")