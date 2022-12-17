Why should we split punctuation from the token it goes with ?
Punctuation is treated as a token separate from word tokens and number tokens. Bounding punctuation, like commas (,) and apostrophes ('), are treated as their own tokens. So splitting tokens would help the process of tokenizing, which is one of the early steps in NLP.

Should abbreviations with space in them be written as a single token or two tokens ?
Abbreviations should be treated as two tokens as the space between them in another format for e.g. W.H.O would have punctuations which are tokenized. Even the numericals would have commas like 134,000. And in many ways spacing is seen as a special character like for programmers.

Should contractions and clitics be a single token or two (or more) tokens ?
Clitics and contractions could be seen as more than one single token. for e.g. the word I'm is a clitic for I am which originally consists of 2 tokens. 
