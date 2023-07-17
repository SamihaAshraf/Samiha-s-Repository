#Samiha Ashraf
#1884227
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
    team = Team()

    team_name = input()
    team_wins = float(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses


    if team.get_win_percentage() >= 0.5:
        print("Congratulations, Team Ravens has a winning average!")
    else:
        print("Team Angels has a losing average.")