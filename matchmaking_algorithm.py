import csv

class Club:
    def __init__(self, name: str, player_ratings: list):
        self.name = name
        self.player_ratings = player_ratings
        self.player_count = len(player_ratings)
        self.club_rating = round(sum(player_ratings) / self.player_count, 1)

    def get_players(self):
        return self.player_ratings

    def __str__(self):
        return self.name + " (" + str(self.club_rating) + ")"


def read_csv(filename):
    """
    A function that reads a file with the string filename <filename> (example "hello.csv"),
    interprets the contents and forms a list of clubs that participate in the matchmaking.
    """
    clubs = []

    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for line in csv_reader:
                line = line[0: len(line)]
                name = line[0]
                players = [int(line[i]) for i in range(1, len(line)) if len(line[i]) != 0]
                if len(players) != 0:
                    clubs.append(Club(name, players))
    except FileNotFoundError:
        print("<ERROR>: File was not found in current directory.")

    return clubs

def form_club_pairs(clubs: list):
    """
    A function that takes a list of clubs <clubs> (example [Club, Club, ...])
    and return a list of possible pairings and clubs which are transferred to a wait queue
    """
    wait_queue = []

    if len(clubs) % 2 != 0:
        wait_queue.append(clubs[len(clubs) - 1])
        clubs = clubs[0: len(clubs) - 1]
    clubs.sort(key=lambda club: club.club_rating)
    club_pairs = [[clubs[i], clubs[i + 1]] for i in range(0, len(clubs) - 1, 2)]

    return club_pairs, wait_queue

clubs = read_csv("input.csv")
club_pairs, wait_queue = form_club_pairs(clubs)


for club_pair in club_pairs:
    print("<" + club_pair[0].__str__() + ">" + " VS " + "<" + club_pair[1].__str__() + ">")

if len(wait_queue) == 0:
    print("The wait queue is empty.")
else:
    print("The following users are in the wait queue:")
    for club in wait_queue:
        print(club)