"""
This module translates English to French and French to English
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Add code to create an instance of the IBM Watson Language translator
auth = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=auth)
lang_translator.set_service_url(url)


# Add function which takes in the English_Text as a string argument and returns French_Text.
def english_to_french(text_to_translate):
    """
    This function translates English to French
    """

    french_translation = lang_translator.translate(
        text=text_to_translate,
        model_id='en-fr'
    ).get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    return french_text


# Add function which takes in the French_Text as a string argument and returns English_Text.
def french_to_english(text_to_translate):
    """
    This function translates French to English
    """

    english_translation = lang_translator.translate(
        text=text_to_translate,
        model_id='fr-en'
    ).get_result()
    english_text = english_translation.get("translations")[0].get("translation")
    return english_text
