# Tournament Winner Algorthims
'''
There's an algorithms tournament taking place in which teams of programmers compete against each other
to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces
off against all other teams. Only two teams compete against each other at a time, and for each competition,
one team is designated the home team, while the other team is the away team. In each competition there's
always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses.
 The winner of the tournament is the team that receives the most amount of points.Given an array of pairs
 representing the teams that have competed against each other and an array containing the results of each competition,
 write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively.
 The competitions array has elements in the form of [homeTeam, away Team] , where each team is a string
 of at most 30 characters representing the name of the team. The results array contains information about
 the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner
 of competitions[i] , where a 1 in the results array means that the home team in the corresponding competition won
 and a means that the away team won. It's guaranteed that exactly one team will win the tournament and that each team
will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.
'''

HOME_TEAM_WON = 1
def tournamentWinner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}
    for counter, competition in enumerate(competitions):
        result = results[counter]
        home_team, away_team = competition
        winning_team = home_team if result == HOME_TEAM_WON else away_team
        update_score(winning_team, 3, scores)
        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team
    return current_best_team


def update_score(winning_team, points, scores):
    if winning_team not in scores:
        scores[winning_team] = 0
    scores[winning_team] += points

print(tournamentWinner([["HTML", "C#"],["C#", "Python"],["Python", "HTML"]],[0, 0, 1]))