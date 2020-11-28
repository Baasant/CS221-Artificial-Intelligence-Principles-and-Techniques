import shell
import util
import wordsegUtil

############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
       ## raise Exception("Not implemented yet")
        return self.query
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        ##raise Exception("Not implemented yet")
        # END_YOUR_CODE

        return len(state) == 0

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 7 lines of code, but don't worry if you deviate from this)
        ##raise Exception("Not implemented yet")
        result=[] ##list to add result .
        if not self.isEnd(state):
            for i in range(len(state),0,-1):
                action=state[:i]## get all possible action for this state
                cost=self.unigramCost(action)##calculate the cost of action
                remainingText = state[len(action):]
                result.append((action, remainingText, cost))## apend the result of action,remaining text,cost
        return result


        # END_YOUR_CODE

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    ##raise Exception("Not implemented yet")
    words=words=' '.join(ucs.actions) ##return the words
    return words

    # END_YOUR_CODE

############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        ##raise Exception("Not implemented yet")
        return (self.queryWords[0],0)

        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        ##raise Exception("Not implemented yet")
     return state[1]==len(self.queryWords)-1
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
        ##raise Exception("Not implemented yet")
        result = []
        index = state[1] + 1
        # temp=self.queryWords[index]
        choices = self.possibleFills(self.queryWords[index]).copy()
        if len(choices) == 0:
            choices.add(self.queryWords[index])
        for action in choices:
            cost = self.bigramCost(state[0], action)
            result.append((action, (action, index), cost))
        return result

        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    ##raise Exception("Not implemented yet")
    if len(queryWords) == 0:
        return ''
    else:
        queryWords.insert(0, wordsegUtil.SENTENCE_BEGIN)
    ucs = util.UniformCostSearch(verbose=1)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
    words = ' '.join(ucs.actions)
    return words

    # END_YOUR_CODE


############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        return (self.query,wordsegUtil.SENTENCE_BEGIN)
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        #raise Exception("Not implemented yet")
        if len(state[0]) == 0:
            return True
        return False
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 14 lines of code, but don't worry if you deviate from this)
        #raise Exception("Not implemented yet")
        result = []
        for i in range(1, len(state[0]) + 1):
            subword = state[0][:i]
            remainWord = state[0][i:]
            choices = self.possibleFills(subword).copy()
            for item in choices:
                cost = self.bigramCost(state[1], item)
                result.append((item, (remainWord, item), cost))
        return result

        # END_YOUR_CODE

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    ##raise Exception("Not implemented yet")
    ucs = util.UniformCostSearch(verbose=1)
    ucs.solve(JointSegmentationInsertionProblem(query, bigramCost, possibleFills))
    words = ' '.join(ucs.actions)
    return words

    # END_YOUR_CODE

############################################################

if __name__ == '__main__':
    shell.main()
