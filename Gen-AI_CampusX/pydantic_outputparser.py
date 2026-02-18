# This is like a pipeline.

# Step 1 → Template creates prompt
# Step 2 → Model generates output
# Step 3 → Parser validates and converts to Person object

# Like:

# 📄 Prompt → 🤖 AI → 📋 Validator

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai  import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
final_result = chain.invoke({'place': 'sri lankan'})

print(final_result)