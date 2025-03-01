from langchain_core.output_parsers import JsonOutputParser
from src.data_models import MatchesResponse
from src.prompt_template import template
from src.model_factory import GoogleGenerativeAIFactory
from src.config import MODEL_TYPE_GEMINI
from langchain_core.prompts import PromptTemplate
from src.logger import get_logger
import json
import os

logger = get_logger(__name__)

def load_peer_supporter_profiles():
    with open("src/data/peer_supporters.json", "r") as file:
        return json.load(file)

def create_chain(model_type):
    model = __get_model(model_type)
    output_parser = JsonOutputParser(pydantic_object=MatchesResponse)
    prompt = PromptTemplate(template=template,
                            input_variables=["condition", "hobbies", "about"],
                            partial_variables={"format_instructions": output_parser.get_format_instructions(), 
                                               "peer_supporter_profiles_json":load_peer_supporter_profiles()}
                            )
    #prompt.format()
    logger.debug("------- prompt -----")
    logger.debug(prompt)
    logger.debug("----------------------")
    return prompt | model | output_parser

def __get_model(type: str):
    logger.debug("Model type: {type}")
    match type:
        case MODEL_TYPE_GEMINI:
            return GoogleGenerativeAIFactory().create_model()
