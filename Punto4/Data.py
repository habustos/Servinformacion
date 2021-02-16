import pandas as pd


class Vote():
    Voting = pd.read_excel('xlsx\\Votes.xlsx')
    Voting = pd.DataFrame(Voting)
    Voting = Voting.groupby(["candidato","partido","codigo_puesto","nombre_puesto","municipio","departamento"]).votos.sum()
    Voting = Voting.to_excel('xlsx\\Voting_Result.xlsx')