
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


import logging

logger = logging.getLogger(__name__)

logger.info("Initializing T5-Transformer")

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

text ="""
DevOps is a software development methodology that intends
to automate the process between software development and IT
operations. The goal is to reduce the time between committing
a change to a system and placing it to production, while
ensuring high quality [1]. Compared to traditional software de-
velopment process, DevOps provides faster feedback between
software development and IT operations so that new features
and bug fixes can be released faster to the customers. To ensure
the quality and the health of the deployed systems, software
logging plays a central role.
Software logging in the context of DevOps refers to the
practices of developing and maintaining logging code and
analyzing the resulting execution logs. Logging code refers
to the code snippets that developers inserted into source code
(e.g., LOG.info("User " + userName + " logged
in")) to monitor the behavior of systems during runtime.
There are typically four types of components in a snippet
of logging code: a logging object, a verbosity level, static
texts, and dynamic contents. In the above example, the logging
object is Logger, the verbosity level is info, the static
texts are User and logged in, and the dynamic content is
userName. Execution logs (a.k.a., logs), which are generated
by logging code during runtime, are readily available in large-
scale software systems for many purposes like system monitor-
ing [2], problem debugging [3], workload characterization [4],
and business decision making [5]. Stale or incorrect logging
code may cause confusion [6] or even more serious issues like
system crash [7]. In particular, there are four major challenges
associated with the software logging practices in DevOps
"""

preprocess_text = text.strip().replace("\n"," ")

t5_prepared_Text = "summarize: "+preprocess_text

logger.debug("original text preprocessed: \n", preprocess_text)

tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)

# summmarize 
summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=30,
                                    max_length=200,
                                    early_stopping=True)

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

logger.debug("\nSummarized text: \n",output)
print("\nSummarized text: \n" + output)

