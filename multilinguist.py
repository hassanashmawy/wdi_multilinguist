import requests
import json
import random
import math

class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country
    Parameters
    ----------
    country_name : str
         The full name of a country.
    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country
    Parameters
    ----------
    country_name : str
        The full name of a country.
    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API
    Parameters
    ----------
    msg : str
        A message to be translated.
    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']


class MathGenius(Multilinguist):

  def report_total(self, numbers):
    return 'The total is ' + str(sum(numbers))

  def square_root(self, x):
    return 'The square root is ' + str(math.sqrt(x))

class QuoteCollector(Multilinguist):

  def __init__(self):
    self.quote_collection = []

  def add_quote(self, quote):
    self.quote_collection.append(quote)

  def random_quote(self):
    return self.quote_collection[random.randint(0,(len(self.quote_collection) - 1))]

class FoodRecommender(Multilinguist):

  def __init__(self):
    self.foodbycontinent = {
      'North America': "Willie Mae's Scotch House in New Orleans, Louisiana",
      'South America': 'Peumayen Resturant in Santiago, Chile',
      'Africa': 'Cape Malay food in Cape Town',
      'Europe': 'Figlmüller in Vienna',
      'Asia': 'In Love Restaurant in Bangkok',
      'Australia': 'Broad Arrow in the Western Australia Outback',
      'Antarctica': 'You should bring your own granola bars'
    }

  def ask(self):
    print("Please enter a continent to get a food recommendation.")
    user_input = input()
    for continent, recommendation in self.foodbycontinent.items():
      if continent == user_input:
        return "You should go to: " + recommendation


her = Multilinguist()
print(her)

print(her.language_in('Egypt'))
print(her.travel_to('Iran'))
print(her.say_in_local_language('Hello, Piss off'))

me = MathGenius()
print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
print(me.square_root(4))
me.travel_to("India")
print(me.say_in_local_language(me.report_total([6,3,6,68,455,4,467,57,4,534]))) # है को कुल 1604
print(me.say_in_local_language(me.square_root(4)))
me.travel_to("Italy")
print(me.say_in_local_language(me.report_total([324,245,6,343647,686545]))) # È Il totale 1030767
print(me.say_in_local_language(me.square_root(4)))

you = QuoteCollector()
you.add_quote('Now! I will listen now!')
you.add_quote('show me a trick')
you.add_quote('Pizza baby!!')
print(you.quote_collection)
print(you.random_quote())
you.travel_to('Italy')
print(you.say_in_local_language(you.random_quote()))

we = FoodRecommender()
print(we.ask())
we.travel_to('Italy')
print(we.say_in_local_language(we.ask()))

"""
# him = MathGuy()
# print(him.do_the_math([23,45,676,34,5778,4,23,5465])) # The total is 12048
# him.travel_to("India")
# print(him.do_the_math([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# him.travel_to("Italy")
# print(him.do_the_math([324,245,6,343647,686545])) # È Il totale 1030767



speak_2_lang = Multilinguist()
speak_2_lang.travel_to('Egypt')
# speak_2_lang.say_in_local_language('you are fuckin cool')
# print(speak_2_lang.say_in_local_language('you are fuckin cool'))

"""
