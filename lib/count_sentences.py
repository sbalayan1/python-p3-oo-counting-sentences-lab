#!/usr/bin/env python3
class MyString:
  pass
  def __init__(self, value=''):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if (type(value) == str): 
      self._value = value

    print('The value must be a string.')

  def is_sentence(self):
    pass
    return self._value.endswith('.')

  def is_question(self):
    return self._value.endswith('?')

  
  def is_exclamation(self):
    return self._value.endswith('!')

  def count_sentences(self):
    pass
    if len(self._value) == 0: return 0
    for punc in ["!", "?"]:
      self._value = self._value.replace(punc, ".")
    
    return len(self._value.split('. '))
    

  value = property(get_value, set_value)