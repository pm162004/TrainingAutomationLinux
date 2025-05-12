import random
import requests
from Shrubs_Automation.shrubs_setup.randomeString import *
from Shrubs_Automation.shrubs_setup import randomeString
from cryptography.exceptions import AlreadyUpdated

INCORRECT_EMAIL = "abc"
INVALID_EMAIL = "modip89@gmail.com"
INCORRECT_PASSWORD = "00"
INVALID_PASSWORD = "TEST"
SIGNUP_PASSWORD = "Test@123"
# INCORRECT_MOBILE_NO = "12355"
# INVALID_PHONE_NO = ['[2abc@', '1234567890236']
# UNVERIFIED_USER_EMAIL = "0000000000"
WRONG_PASSWORD = ['Admin', 'Admin123456789admin', 'Admin@12']
INVALID_EMAIL_ID_INPUT = "abc@gmail"
ALREADY_REGISTERED_EMAIL = "testp567@yopmail.com"
ALREADY_REGISTERED_UNAME_TEST = "test"
ALREADY_REGISTERED_UNAME_ADMIN= "admin"
VALID_EMAIL = "testp5@yopmail.com"
VALID_UNAME = "Admin34"
# response = requests.get("https://random-word-api.herokuapp.com/word?number=10")
# words = response.json()
# random_word = random.choice(words)
VALID_SHRUBS = randomeString.get_random_word_from_datamuse()
EXISTING_SHRUBS = "NEWS 3"
LINK = "https://www.google.com"
# INCORRECT_FIRST_NAME = "P"
# INVALID_FIRST_NAME = "532"
# INCORRECT_LAST_NAME = "S"
# INVALID_LAST_NAME = "9@1"
# INVALID_EMAIL_ID_INPUT = "abc@gmail"
# INVALID_FEEDBACK_INPUT = "1"
# FEEDBACK_MINIMUM_VALIDATION_INPUT = "a"
# FIRST_NAME_INPUT = "Jake"
# LAST_NAME_INPUT = "Brown"
# EMAIL_ID_INPUT = "abc@gmail.com"
# FEEDBACK_INPUT = "xyz, test"
# INVALID_INPUT = ['a2./', '22..', '0']
# CURRENT_PRICE_INPUT = "17600"
# STRIKE_PRICE_INPUT = "1600"
# IMPLIED_VOLATILITY_INPUT = "33"
# INDEX_INPUT = ['NIFTY 50', 'Ba', 'FIN', 'MIDCP', 'OTHERS']
