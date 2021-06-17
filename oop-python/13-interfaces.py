class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()
 
  def play(self):
    print("Playing chess!")
 
class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()
 
  def play(self):
    print("Playing checkers!")
    
    
    
def play_game(chess_or_checkers):
  chess_or_checkers.play()
 
chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()
 
for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)
"""
Prints out the following:
Playing chess!
Playing checkers!
Playing chess!
"""



#script.py
# Create a subclass of InsurancePolicy called VehicleInsurance.
# Create a different subclass of InsurancePolicy called HomeInsurance.
#Give VehicleInsurance a .get_rate() method that takes self as a parameter.
#Give HomeInsurance a .get_rate() method that takes self as a parameter. 
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005
  
    
