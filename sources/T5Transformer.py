
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import logging

logger = logging.getLogger(__name__)
isSetup = False

model = None
tokenizer = None
device = None

class TransformerNotInitializedException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def setup(use_model = 't5-small'):
    """
    Setup the model, tokenizer and the device on which torch will run
    """
    logger.info("Initializing T5-Transformer")
    global model, tokenizer, device
    logger.info(f"\twith model: {use_model}")
    model = T5ForConditionalGeneration.from_pretrained(use_model)
    tokenizer = T5Tokenizer.from_pretrained(use_model)
    device = torch.device('cpu')

    global isSetup 
    isSetup= True
    logger.info("Setup complete")

def teardown():
    logger.info("Tearing down T5-Transformer")
    global model, tokenizer, device
    model = None
    tokenizer = None
    device = None
    
    global isSetup 
    isSetup = False
    print("Teardown")

def encode(prepared_text):
    logger.info("Encoding prepared Text")
    tokenized_text = tokenizer.encode(prepared_text, return_tensors="pt").to(device)

    return tokenized_text

def summarize(tokenized_text, beams = 6, no_repeat_n_gram = 2, min_len = 250, max_len = 500, early_stop = True):
    logger.info("Creating Summary")
    logger.info(f"\twith number of beams: {beams}")
    logger.info(f"\tmin_length_of_summary: {min_len}")
    logger.info(f"\tmax_length_of_summary: {max_len}")
    logger.info(f"\tearly stopping allowed: {early_stop}")
    
    summary_ids = model.generate(tokenized_text,
                                        num_beams=beams,
                                        no_repeat_ngram_size=no_repeat_n_gram,
                                        min_length=min_len,
                                        max_length=max_len,
                                        early_stopping=early_stop)
    return summary_ids

def decode(summary_ids):
    logger.info("Decoding summary ids")
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
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
        encoded_text = encode(t5_prepared_text)

        logger.info("Summarizing text")
        summary_ids = summarize(encoded_text)

        logger.info("Decoding summarized IDs")
        summary = decode(summary_ids)
        
        #logger.debug("Summarized text: \n",summary)
    
    return summary
