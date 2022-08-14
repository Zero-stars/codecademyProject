destinations=["Paris, France","Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler= ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination= traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = [[] for x in destinations]

def add_attraction(destination, attraction):
  destination_index= get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return attractions_for_destination

add_attraction("Los Angeles, USA", ["Vience Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attraction(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction= attraction 
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination= traveler[1]
  traveler_interest= traveler[2]

  traveler_attractions= find_attraction(traveler_destination,   traveler_interest)

  interests_string= "Hi " + traveler[0]+ ", we think you'll like these places around " + traveler_destination + ": "

  for i in range(len(traveler_attractions)): 
    #End of the list
    if traveler_attractions[i] ==traveler_attractions[-1]:
      interests_string += "the " + traveler_attractions[i] + "."
      #Beginning and any items except the last item
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string 

sites= get_attractions_for_traveler(["Dereck Smill", "São Paulo, Brazil",  ["historical site","zoo"]])

print(sites)
