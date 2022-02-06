
import logging
import torch

from transformers import T5Tokenizer, T5ForConditionalGeneration
from .Exceptions import TransformerNotInitializedException

logger = logging.getLogger(__name__)
isSetup = False

__model = None
__tokenizer = None
__device = None

def setup(use_model = 't5-small'):
    """
    Setup the model, tokenizer and the device on which torch will run
    """
    logger.info("Initializing T5-Transformer")
    global __model, __tokenizer, __device
    logger.info(f"\twith model: {use_model}")
    
    __model = T5ForConditionalGeneration.from_pretrained(use_model)
    __tokenizer = T5Tokenizer.from_pretrained(use_model)
    
    if torch.cuda.is_available():
        logger.info("Found cuda-capable device. Model will use this instead of cpu.")
        torch_device = 'cuda:0' 
        __model = __model.cuda()
    else:
        logger.info("Running model on cpu.")
        torch_device = 'cpu' 
        
    __device = torch.device(torch_device)

    global isSetup 
    isSetup= True
    logger.info("Setup complete")

def teardown():
    logger.info("Tearing down T5-Transformer")
    global __model, __tokenizer, __device
    __model = None
    __tokenizer = None
    __device = None
    
    global isSetup 
    isSetup = False
    print("Teardown complete")

def __encode(prepared_text):
    logger.info("Encoding prepared Text")
    tokenized_text = __tokenizer.encode(prepared_text, return_tensors="pt").to(__device)

    return tokenized_text

def __summarize(tokenized_text, beams = 4, no_repeat_n_gram = 2, min_len = 30, max_len = 200, early_stop = True):
    logger.info("Creating Summary")
    logger.info(f"\twith number of beams: {beams}")
    logger.info(f"\tmin_length_of_summary: {min_len}")
    logger.info(f"\tmax_length_of_summary: {max_len}")
    logger.info(f"\tearly stopping allowed: {early_stop}")
    
    summary_ids = __model.generate(tokenized_text,
                                        num_beams=beams,
                                        no_repeat_ngram_size=no_repeat_n_gram,
                                        min_length=min_len,
                                        max_length=max_len,
                                        early_stopping=early_stop)
    return summary_ids

def __decode(summary_ids):
    logger.info("Decoding summary ids")
    output = __tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output


def create_summary(preprocessed_text):
    """
    create a summary on basis of a preprocessed text
    """
    if not isSetup:
        logger.error("Transformer is not setup yet.")
        logger.info("Please run Transformer.setup() before trying to create a summary")
        raise TransformerNotInitializedException("Transformer has not been setup")
    else:
        t5_prepared_text = "summarize: " + preprocessed_text
        logger.info("Encoding input text..")
        encoded_text = __encode(t5_prepared_text)

        logger.info("Summarizing text")
        summary_ids = __summarize(encoded_text)

        logger.info("Decoding summarized IDs")
        summary = __decode(summary_ids)
        
        #logger.debug("Summarized text: \n",summary)
    
    return summary
