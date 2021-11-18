
import logging
import torch


from transformers import LongformerTokenizer, EncoderDecoderModel
from .Exceptions import TransformerNotInitializedException

logger = logging.getLogger(__name__)
isSetup = False

__model = None
__tokenizer = None
__device = None

model_name = 'patrickvonplaten/longformer2roberta-cnn_dailymail-fp16'
tokenizer_name = 'allenai/longformer-base-4096'

def setup():
    """
    Setup the model and tokenizer
    """
    logger.info("Initializing Longformer")
    #logger.info(f"\twith model: {use_model}")
    global __model, __tokenizer, __device
    __model = EncoderDecoderModel.from_pretrained(model_name)
    __tokenizer = LongformerTokenizer.from_pretrained(tokenizer_name) 

    __device = torch.device('cpu')

    global isSetup
    isSetup = True
    logger.info("Setup complete")

def teardown():
    logger.info("Tearing down Longformer")
    global __model, __tokenizer, __device
    __model = None
    __tokenizer = None
    __device = None
    
    global isSetup 
    isSetup = False
    print("Teardown complete")

def __encode(preprocessed_text):
    logger.info("Encoding prepared Text")
    input_ids = __tokenizer(preprocessed_text, return_tensors="pt").input_ids
    return input_ids

def __summarize(input_ids):
    logger.info("Creating Summary")
    #this needs too much RAM (52GB)
    #position_ids = torch.stack([torch.arange(4096) for a in range(input_ids.shape[1])]).to(__device)
    logger.info(f"Batch-size: {input_ids.shape[1]}")
    
    output_ids = __model.generate(input_ids)

    return output_ids

def __decode(output_ids):
    logger.info("Decoding summary ids")
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
    
    return summary