import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, KeywordsOptions

authenticator = IAMAuthenticator('DZDE0KeTcfpsSJrCeCd-hjn7muTy39UjVr5f9LI6QQIp')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/e4e00b2a-5841-4634-acf7-2a82cf84a0f9')

def text_analysis(input, keywords):

    response = natural_language_understanding.analyze(
        text=input,
        features=Features(emotion=EmotionOptions(targets=keywords))).get_result()

    print(json.dumps(response, indent=2))


def keyword_analysis(input):

    response = natural_language_understanding.analyze(
        text = input,
        features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))).get_result()

    # print(json.dumps(response, indent=2))

    # Make list of keywords
    keywords = [keyword["text"] for keyword in response['keywords']]
    return keywords

test_text = "Supraja doesn't like IBM Watson. She hates him."

keywords = keyword_analysis(test_text)
text_analysis(test_text, keywords)