from transformers import LongformerTokenizer, EncoderDecoderModel

# Load model and tokenizer
model = EncoderDecoderModel.from_pretrained("patrickvonplaten/longformer2roberta-cnn_dailymail-fp16")
tokenizer = LongformerTokenizer.from_pretrained("allenai/longformer-base-4096") 

# Specify the article
article = """Germany (German: Deutschland, German pronunciation: [ˈdɔʏtʃlant]), officially the Federal Republic of Germany,[e] is a country at the intersection of Central and Western Europe. It is situated between the Baltic and North seas to the north, and the Alps to the south; covering an area of 357,022 square kilometres (137,847 sq mi), with a population of over 83 million within its 16 constituent states. It borders Denmark to the north, Poland and the Czech Republic to the east, Austria and Switzerland to the south, and France, Luxembourg, Belgium, and the Netherlands to the west. Germany is the second-most populous country in Europe after Russia, as well as the most populous member state of the European Union. Its capital and largest city is Berlin, and its financial centre is Frankfurt; the largest urban area is the Ruhr.Various Germanic tribes have inhabited the northern parts of modern Germany since classical antiquity. A region named Germania was documented before AD 100. In the 10th century, German territories formed a central part of the Holy Roman Empire. During the 16th century, northern German regions became the centre of the Protestant Reformation. Following the Napoleonic Wars and the dissolution of the Holy Roman Empire in 1806, the German Confederation was formed in 1815. In 1871, Germany became a nation-state when most of the German states unified into the Prussian-dominated German Empire. After World War I and the German Revolution of 1918–1919, the Empire was replaced by the semi-presidential Weimar Republic. The Nazi seizure of power in 1933 led to the establishment of a dictatorship, World War II, and the Holocaust. After the end of World War II in Europe and a period of Allied occupation, Germany was divided into the Federal Republic of Germany, generally known as West Germany, and the German Democratic Republic, East Germany. The Federal Republic of Germany was a founding member of the European Economic Community and the European Union, while the German Democratic Republic was a communist Eastern Bloc state and member of the Warsaw Pact. After the fall of communism, German reunification saw the former East German states join the Federal Republic of Germany on 3 October 1990—becoming a federal parliamentary republic led by a chancellor.Germany is a great power with a strong economy; it has the largest economy in Europe, the world's fourth-largest economy by nominal GDP, and the fifth-largest by PPP. As a global leader in several industrial, scientific and technological sectors, it is both the world's third-largest exporter and importer of goods. As a developed country, which ranks very high on the Human Development Index, it offers social security and a universal health care system, environmental protections, and a tuition-free university education. Germany is also a member of the United Nations, NATO, the G7, the G20, and the OECD. It also has the fourth-greatest number of UNESCO World Heritage Sites."""

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

# Tokenize and summarize
input_ids = tokenizer(preprocess_text, return_tensors="pt").input_ids
output_ids = model.generate(input_ids)

# Get the summary from the output tokens
summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("Article:")
print(preprocess_text)
print()
# Print summary
print("Summary:")
print(summary)