class orchid:
    kind = "flora"
    def __init__(self, colour, flowering_time, type):
        self.colour = colour
        self.flowering_time = flowering_time
        self.type = type



if __name__ == "__main__":
    red_orchid = orchid('red', 'august', 'cattleya')
    yellow_orchid = orchid('yellow', 'march', 'Phalaenopsis')