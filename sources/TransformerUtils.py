
import logging

from . import T5Transformer
from . import Longformer
from . import RoBERTa
from .Exceptions import InvalidModelException

logger = logging.getLogger(__name__)

__t5_model = 't5-base'

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
    if not T5Transformer.isSetup:
        T5Transformer.setup(__t5_model)
    
    #generate abstract
    summary = T5Transformer.create_summary(preprocessed_text=data)

    return summary

def __run_longformer(data: str):
    #set up transformer
    if not Longformer.isSetup:
        Longformer.setup()
    
    #generate abstract
    summary = Longformer.create_summary(data) 
    
    return summary

def __run_roberta(data: str):
    #set up transformer
    if not RoBERTa.isSetup:
        RoBERTa.setup()
    
    #generate abstract
    summary = RoBERTa.create_summary(data)
    
    return summary

def __teardown_t5_transofrmer():
    T5Transformer.teardown()

def __teardown_longformer():
    Longformer.teardown()

def __teardown_roberta():
    RoBERTa.teardown()

run_switcher = {
    "t5": __run_t5_transformer,
    "longformer": __run_longformer,
    "roberta": __run_roberta,
    }
teardown_switcher = {
    "t5": __teardown_t5_transofrmer,
    "longformer": __teardown_longformer,
    "roberta": __teardown_roberta,
    }


def start_Transformer(transformer_type: str, data: str):
    func = run_switcher.get(transformer_type, lambda x: "Invalid option")
    logger.info("Found consumer: %s", func)
    return func(data)

def stop_transformer(transformer_type: str):
    func = teardown_switcher.get(transformer_type, lambda x: "Invalid option")
    logger.info("Found consumer: %s", func)
    return func()