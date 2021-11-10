
TEST_TEXT = """
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

T5_SUMMARY = """
software logging in the context of DevOps is a software development methodology
that intends to automate the process. the goal is to reduce the time between
committing changes and placing it to production, while ensuring high quality [1].
compared to traditional software de- velopment process, the methodology provides
faster feedback so that new features and bug fixes can be released faster to the
customers. 
""".strip().replace("\n"," ")

LF_SUMMARY = """
DevOps is a software development methodology that aims to reduce the time between
committing a change to a system and placing it to production. The goal is to
reduce time between commits and placing the production of a system to production,
while ensuring high quality. Software logging plays a central role in developing
and maintaining logging code and analyzing the resulting execution logs.
""".strip().replace("\n"," ")