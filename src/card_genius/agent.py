# From https://ai.pydantic.dev/models/#example-local-usage

from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class CityLocation(BaseModel):
    city: str
    country: str


ollama_model = OpenAIModel(
    model_name='llama3.2', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
agent = Agent(ollama_model, result_type=CityLocation)

if __name__ == "__main__":
    result = agent.run_sync('Where were the olympics held in 2012?')
    print(result.data)
    print(result.usage())