import os
from dotenv import load_dotenv


class Env:
    isProduction = "ENV" in os.environ and os.environ["ENV"] == "production"
    isDevelopment = not isProduction

    def __init__(self) -> None:
        if self.isProduction:
            load_dotenv(".env.production")
        else:
            load_dotenv(".env.development")

    def __str__(self) -> str:
        return f"isProduction: {self.isProduction}\nisDevelopment: {self.isDevelopment}"


# exported
env = Env()
print(env)
