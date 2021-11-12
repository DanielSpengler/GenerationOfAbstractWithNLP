import pytest

from sources import TextSplitter

chapter_1 = """
INTRODUCTION
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
"""
chapter_2 = """
CURRENT RESEARCH ON SOFTWARE LOGGING
In this section, we describe the current research on software
logging. We separate them in two aspects: logging in the
context of software development and IT operations.
A. Logging for Software Development
The current research works on developing high quality
logging code can be categorized into three types: what-to-log,
where-to-log, and how-to-log.
"""
chapter_3 = """
RESEARCH HYPOTHESIS
Software repositories (e.g., code repositories, communica-
tion repositories, runtime repositories, and bug repositories)
which are readily available and contain rich information
about software development and system behavior during
runtime, can be leveraged to systematically improve the
software logging practices in the context of DevOps
"""
TEST_TEXT = f"""
I. {chapter_1}
II. {chapter_2}
IV. {chapter_3}
"""
import re 

def test_split_text_into_chapters():
    chapters = TextSplitter.split_text_into_chapters(TEST_TEXT)
    assert len(chapters) == 3

    assert chapters[0].strip() == chapter_1.strip()
    assert chapters[1].strip() == chapter_2.strip()
    assert chapters[2].strip() == chapter_3.strip()
    