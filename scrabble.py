letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#support lower case letter
letters += [letter.lower() for letter in letters]
points+=points

#Pair the key to value
letter_to_points ={key: value for key, value in zip(letters,points)}

letter_to_points.update({" ": 0})

#Count the point base on word
def score_word(word):
  point_total=0
  for letter in word:
    point_total+=letter_to_points.get(letter,0)
  return point_total


player_to_words={"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_point={}

#Track player points based on words they created
def update_point_totals(player_to_words):
  for players, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points+=score_word(word)
    player_to_point[players]= player_points

#Add word to player
def play_word(player, word):
  player_to_words[player].append(word)

play_word("player1", "Game")

update_point_totals(player_to_words)

print(player_to_words)
print(player_to_point)


