class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False, hand=None):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive
        self.hand = hand

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.

PLANETS = {
    "Mercury": PlanetCard("Mercury", "Increases High Card hand value",2,10,1, hand="High Card"),
    "Venus": PlanetCard("Venus", "Increases One Pair hand value",2,15,1, hand="One Pair"),
    "Earth": PlanetCard("Earth", "Increases Two Pair hand value",2,15,2, hand="Two Pair"),
    "Mars": PlanetCard("Mars", "Increases Three of a Kind hand value",2,25,2, hand="Three of a Kind"),
    "Jupiter": PlanetCard("Jupiter", "Increases Straight hand value",3,25,3, hand="Straight"),
    "Saturn": PlanetCard("Saturn", "Increases Flush hand value",3,30,3, hand="Flush"),
    "Uranus": PlanetCard("Uranus", "Increases Full House hand value",3,35,3, hand="Full House"),
    "Neptune": PlanetCard("Neptune","Increases Four of a Kind hand value",3,40,4, hand="Four of a Kind"),
    "Sun": PlanetCard("Sun", "Increases all hands value",12,30,2, hand="ALL"),

}
