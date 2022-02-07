
import logging
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .Exceptions import TransformerNotInitializedException

logger = logging.getLogger(__name__)
isSetup = False

__model = None
__tokenizer = None
__device = None

model_name = 'google/roberta2roberta_L-24_cnn_daily_mail'
tokenizer_name = 'google/roberta2roberta_L-24_cnn_daily_mail'

def setup():
    """
    Setup the model and tokenizer
    """
    logger.info("Initializing Roberta2Roberta")
    #logger.info(f"\twith model: {use_model}")
    global __model, __tokenizer, __device
    __tokenizer = AutoTokenizer.from_pretrained(tokenizer_name) 
    __model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
 
    if torch.cuda.is_available():
        logger.info("Found cuda-capable device. Model will use this instead of cpu.")
        torch_device = 'cuda:0' 
        __model = __model.cuda()
    else:
        logger.info("Running model on cpu.")
        torch_device = 'cpu' 
        
    __device = torch.device(torch_device)

    global isSetup
    isSetup = True
    logger.info("Setup complete")


def teardown():
    logger.info("Tearing down Roberta2Roberta")
    global __model, __tokenizer, __device
    __model = None
    __tokenizer = None
    __device = None
    
    global isSetup 
    isSetup = False
    print("Teardown complete")

def __encode(preprocessed_text):
    logger.info("Encoding prepared Text")
    input_ids = __tokenizer(preprocessed_text, return_tensors="pt").to(__device).input_ids
    return input_ids

def __summarize(input_ids):
    logger.info("Creating Summary")
    
    output_ids = __model.generate(input_ids)[0]

    return output_ids

def __decode(output_ids):
    logger.info("Decoding summary ids")
    summary = __tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary

def create_summary(preprocessed_text):
    """
    create a summary on basis of a preprocessed text
    """
    if not isSetup:
        logger.error("Transformer is not setup yet.")
        logger.info("Please run Transformer.setup() before trying to create a summary")
        raise TransformerNotInitializedException("Transformer has not been setup")
    else:
        logger.info("Encoding input text..")
        encoded_text = __encode(preprocessed_text)

        logger.info("Summarizing text")
        summary_ids = __summarize(encoded_text)

        logger.info("Decoding summarized IDs")
        summary = __decode(summary_ids)
    
    return summary