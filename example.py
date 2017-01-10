
from definitions import MCDAProblem

def mojaMetoda(problem):
    #tutaj kod metody
    pass





if __name__ == '__main__':
    
    problem = MCDAProblem()
    problem.readPerformanceTable('performanceTable.csv')
    problem.readCriteriaMinMax('criteriaMinMax.csv')
    problem.readNumberOfBreakPoints('numberOfBreakPoints.csv')
    problem.readAlternativesRanks('alternativesRanks.csv')


    solution = mojaMetoda(problem)
