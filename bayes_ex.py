from numpy import *

class NaiveBayesClassifier:

    def trainNB(self, trainMatrix, trainCategory):
        numTrainDocs = len(trainMatrix)
        numWords = len(trainMatrix[0])
        pAbusive = sum(trainCategory) / float(numTrainDocs)
        p0Num = ones(numWords)
        p1Num = ones(numWords)
        p0Denom = 2.0
        p1Denom = 2.0
        for i in range(numTrainDocs):
            if trainCategory[i] == 1:
                p1Num += trainMatrix[i]
                p1Denom += sum(trainMatrix[i])
            else:
                p0Num += trainMatrix[i]
                p0Denom += sum(trainMatrix[i])
        p1Vect = log(p1Num / p1Denom)
        p0Vect = log(p0Num / p0Denom)
        return p0Vect, p1Vect, pAbusive

    def classifyNB(self, vec2Classify, p0Vec, p1Vec, pClass1):
        p1 = sum(vec2Classify * p1Vec) + log(pClass1)
        p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
        if p1 > p0:
            return 1
        else: 
            return 0
    
    def testingNB(self):
        listOPosts, classVec = self.create_data_set()
        myVocabList = self.create_vocablist(listOPosts)
        trainMat = []
        for postinDoc in listOPosts:
            trainMat.append(self.setOfWords2Vec(myVocabList, postinDoc))
        p0V, p1V, pAb = self.trainNB(array(trainMat), array(classVec))
        testEntry = ['love', 'my', 'dalmation']
        thisDoc = array(self.setOfWords2Vec(myVocabList, testEntry))
        print(testEntry, 'classified as: ', self.classifyNB(thisDoc, p0V, p1V, pAb))
        testEntry = ['stupid', 'garbage']
        thisDoc = array(self.setOfWords2Vec(myVocabList, testEntry))
        print(testEntry, 'classified as: ', self.classifyNB(thisDoc, p0V, p1V, pAb))
    
    def textParse(self, bigString):    
        import re
        listOfTokens = re.split(r'\W*', bigString)
        return [tok.lower() for tok in listOfTokens if len(tok) > 2]
