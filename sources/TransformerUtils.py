
import logging

from . import T5Transformer
from Exceptions import InvalidModelException

logger = logging.getLogger(__name__)

__t5_model = 't5-small'

__possible_t5_models = {
    "t5-small",
    "t5-base",
    "t5-large",
    "t5-3b",
    "t5-11b",
    }

def set_t5_model(model: str):
    #check if given model is valid
    if model in __possible_t5_models:
        global __t5_model 
        __t5_model = model
    else :
        raise InvalidModelException(f"Model ({model} is not a valid option)")

def __run_t5_transformer(data: str):
    #set up transformer
    T5Transformer.setup(__t5_model)
    
    #generate abstract
    summary = T5Transformer.create_summary(preprocessed_text=data)

    return summary

def __run_longformer(data: str):
    return "Longformer"

switcher = {
    "t5": __run_t5_transformer,
    "longformer": __run_longformer,
    }


def start_Transformer(type_of_transformer: str, data: str):
    func = switcher.get(type_of_transformer, lambda x: "Invalid option")
    logger.info("Found consumer: %s", func)
    return func(data)