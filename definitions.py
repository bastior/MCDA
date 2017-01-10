import csv


class alternative():
    def __init__(self):
        
        self.name = ""
        self.criteriaList = []
        self.rank = 0
    
    def addCriterion(self, criterion):
        self.criteriaList.append(criterion)

    def clearCriteria(self):
        self.criteriaList.clear()
        pass


class criterion():
    def __init__(self, value = 0):
        self.value = value
        self.minMax = "max"
        self.numberOfBreakPoints = 2


class MCDAProblem():
    def __init__(self):
        self.alternativesList = []
        '''
        MCDA problem we are solving
        lets say:
        0 - find ranking of alternatives
        1 - find best alternative
        2 - class aggregation
        3 - .... something else
        '''
        self.problemType = 0
        #if anyone needs it, enjoy
        self.epsilon = 0.05

    def readPerformanceTable(self, filePath):

        with open(filePath) as data_file:
            reader = csv.reader(data_file, delimiter=';')
            for data in reader:
                alt = alternative()
                alt.name = data.pop(0)
                for val in data:
                    crit = criterion(val)
                    alt.addCriterion(crit)
                self.alternativesList.append(alt)



    def readAlternativesRanks(self, filePath):

        with open(filePath) as data_file:
            reader = csv.reader(data_file, delimiter=';')
            line = next(reader)

            if not len(line) == len(self.alternativesList):
                raise ValueError("Not maching numberOfBreakPoints len with alt len")
            for val, alt in zip(line, self.alternativesList):
                alt.rank = int(val)



    def readNumberOfBreakPoints(self, filePath):

        with open(filePath) as data_file:
            reader = csv.reader(data_file, delimiter=';')
            line = next(reader)
            for alt in self.alternativesList:
                #check input for each alternative
                if not len(line) == len(alt.criteriaList):
                    raise ValueError("Not maching numberOfBreakPoints len with criteria len in alt: " + alt.name)
            for alt in self.alternativesList:
                for val, crit in zip(line, alt.criteriaList):
                    crit.numberOfBreakPoints = int(val)



    def readCriteriaMinMax(self, filePath):

        with open(filePath) as data_file:
            reader = csv.reader(data_file, delimiter=';')
            line = next(reader)
            for alt in self.alternativesList:
                #check input for each alternative
                if not len(line) == len(alt.criteriaList):
                    raise ValueError("Not maching criteriaMinMax len with criteria len in alt: " + alt.name)
            for alt in self.alternativesList:
                for val, crit in zip(line, alt.criteriaList):
                    crit.minMax = val
