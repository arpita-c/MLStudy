# 
from appdata import AppData
# import predictionio
import sys

def batch_import_task(app_data):

  print "Importing users..."
  count = 0
  for k, v in app_data.get_users().iteritems():
    count += 1
    if (count % 200 == 0):
      print '%s' % count

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
  app_data = AppData()
  batch_import_task(app_data)
