from sources import Transformer

TEST_TEXT = """
DevOps is a software development methodology that intends
to automate the process between software development and IT
operations. The goal is to reduce the time between committing
a change to a system and placing it to production, while
ensuring high quality. Compared to traditional software de-
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
ing, problem debugging, workload characterization,
and business decision making. Stale or incorrect logging
code may cause confusion or even more serious issues like
system crash. In particular, there are four major challenges
associated with the software logging practices in DevOps
"""

TEST_SUMMARY = """
software logging in the context of DevOps refers to the practices
of developing and maintaining logged code and analyzing the resulting
execution logs. there are typically four types of components in a snippet
of logger code: an object, an verbosity level, static texts, and dynamic
contents.
""".strip().replace("\n"," ")

def test_setup_function():
    #test if setup has been run
    assert Transformer.isSetup == False
    assert not hasattr(Transformer, 'model')
    assert not hasattr(Transformer, 'tokenizer')
    assert not hasattr(Transformer, 'device')

    Transformer.setup()

    assert Transformer.isSetup
    assert hasattr(Transformer, 'model')
    assert hasattr(Transformer, 'tokenizer')
    assert hasattr(Transformer, 'device')

def test_summarization_task():
    Transformer.setup()
    preprocess_text = TEST_TEXT.strip().replace("\n"," ")
    result = Transformer.create_summary(preprocess_text)    
    assert result == TEST_SUMMARY