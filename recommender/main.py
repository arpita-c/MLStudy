# 
from appdata import AppData
import recommendations as rec
import sys
import pickle

if __name__ == '__main__':
  prefs = rec.loadMovieLens('../data/movielens-100k')
  itemPrefs=rec.transformPrefs(prefs)

  try:
    input = open('itemNeighbours.pkl', 'rb')
    itemNeighbours = pickle.load(input)
    input.close()
  except Exception, e:
    print "Calculating itemNeighbours.pkl"
    itemNeighbours = rec.calcNarestNeighbours(prefs, 10)
    output = open('itemNeighbours.pkl', 'wb')
    pickle.dump(itemNeighbours, output)
    output.close()

  try:
    input = open('userNeighbours.pkl', 'rb')
    userNeighbours = pickle.load(input)
    input.close()
  except Exception, e:
    print "Calculating userNeighbours.pkl"
    userNeighbours = rec.calcNarestNeighbours(itemPrefs, 10)
    output = open('userNeighbours.pkl', 'wb')
    pickle.dump(userNeighbours, output)
    output.close()

  user = '9'
  print rec.getItemBasedRec(prefs, itemNeighbours, user)[0:10]
  print rec.getUserBasedRec(prefs, userNeighbours, user)[0:10]

  user = 'vincent'
  prefs[user] = {}
  prefs[user]['Seven (Se7en) (1995)'] = 5.0
  print rec.getItemBasedRec(prefs, itemNeighbours, user)[0:10]
