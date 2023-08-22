# OpenAI settings
OPENAI_API_KEY = 'your-openai-api-key'
DEFAULT_SITE_URL = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
ENGINE = 'text-davinci-003'
MAX_TOKENS = 500
TEMPERATURE = 0.3
PROMPT_FOR_SUMMARY = '''Create a website summary for the given text in 200 words. 
Please also format the text and re-phrase it so that it is meaningful and gramatically correct\n{0}'''

PROMPT_FOR_POINTS = '''Create a pointwise website summary for the given text in 6 points only. 
Example: 
1. xyz
2. pqr
etc..

Please also format the text and re-phrase it so that it is meaningful and gramatically correct.

\n{0}

'''

# Server settings
HOST = "0.0.0.0"
PORT = 3010
