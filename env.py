import os
from dotenv import load_dotenv


class Env:
    isProduction: bool
    isDevelopment: bool
    OPENAI_API_KEY: str

    def __init__(self) -> None:
        self.isProduction = "ENV" in os.environ and os.environ["ENV"] == "production"
        self.isDevelopment = not self.isProduction
        if self.isProduction:
            load_dotenv(".env.production")
        else:
            load_dotenv(".env.development")

        load_dotenv(".secret")
        self.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

    def __str__(self) -> str:
        return "\n".join(
            [f"{key}: {value}" for key, value in vars(self).items()]
        )


# exported
env = Env()
print(env)
