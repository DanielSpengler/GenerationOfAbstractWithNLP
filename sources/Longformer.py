
import logging

from transformers import LongformerTokenizer, EncoderDecoderModel
from .Exceptions import TransformerNotInitializedException

logger = logging.getLogger(__name__)
isSetup = False

__model = None
__tokenizer = None

model_name = 'patrickvonplaten/longformer2roberta-cnn_dailymail-fp16'
tokenizer_name = 'allenai/longformer-base-4096'

def setup():
    """
    Setup the model and tokenizer
    """
    logger.info("Initializing Longformer")
    #logger.info(f"\twith model: {use_model}")
    global __model, __tokenizer
    __model = EncoderDecoderModel.from_pretrained(model_name)
    __tokenizer = LongformerTokenizer.from_pretrained(tokenizer_name) 

    global isSetup
    isSetup = True
    logger.info("Setup complete")

def teardown():
    logger.info("Tearing down Longformer")
    global __model, __tokenizer
    __model = None
    __tokenizer = None
    
    global isSetup 
    isSetup = False
    print("Teardown complete")

def __encode(preprocess_text):
    # Tokenize and summarize
    input_ids = __tokenizer(preprocess_text, return_tensors="pt").input_ids
    return input_ids

def __summarize(input_ids):
    output_ids = __model.generate(input_ids)
    return output_ids

def __decode(output_ids):
    summary = __tokenizer.decode(output_ids[0], skip_special_tokens=True)
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
        
        #logger.debug("Summarized text: \n",summary)
    
    return summary