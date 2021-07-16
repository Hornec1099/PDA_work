### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # double equals required for if function as single equals assigns value
    if card.value = 1:
      return True
    # there is no colon after the else which will impact the results
    else
      return False
   
# the def is spelt incorrectly and a missing comma
  dif highest_card(self, card1 card2):
  # the indentation is incorrect for the if
  if card1.value > card2.value:
    # it should return card1
    return card
  else:
    return card2
  

# total is not defined and function not indented correctly
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    # return is indented incorrectly and also total is an int and will need to be a string
    return "You have a total of" + total
  
```
