# 
from appdata import AppData
import recommendations as rec
import sys
import pickle

def batch_import_task(app_data):

  print "Importing users..."
  count = 0
  for k, v in app_data.get_users().iteritems():
    print v

  print '%s users were imported.\n' % count

  print "Importing items..."
  count = 0
  for k, v in app_data.get_items().iteritems():
    count += 1
    if (count % 200 == 0):
      print '%s' % count

  print '%s items were imported.\n' % count

  print "Importing rate actions..."
  count = 0
  for v in app_data.get_rate_actions():
    count += 1
    if (count % 10000 == 0):
      print '%s' % count

  print '%s rate actions were imported.\n' % count

if __name__ == '__main__':
  # app_data = AppData()
  # # batch_import_task(app_data)
  # for item in app_data.get_rate_actions():
  #   print item.uid, app_data.get_item(item.iid).name, item.rating
  prefs = rec.loadMovieLens('../data/movielens-100k')


  try:
    input = open('data.pkl', 'rb')
    similarItems = pickle.load(input)
    input.close()
  except Exception, e:
    similarItems = rec.calculateSimilarItems(prefs, 10)
    output = open('data.pkl', 'wb')
    pickle.dump(similarItems, output)
    output.close();

  # rec = rec.getRecommendations(prefs, '100')
  # print rec
  # print prefs['99']
  # print rec.topMatches(prefs, '99');

  # print rec.topMatches(prefs, '99');

  prefs['vincent'] = {}
  prefs['vincent']['Seven (Se7en) (1995)'] = 5.0
  print rec.getRecommendedItems(prefs, similarItems, 'vincent')

  # vincent = {'HBirdcage, The (1996)': 5.0, 'Kull the Conqueror (1997)': 2.0}
  # prefs['vincent'] = vincent;

  # print rec.sim_distance(prefs, 'vincent', '100') 

  # print rec.topMatches(prefs, 'vincent');

