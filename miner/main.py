import searchengine as se

if __name__ == '__main__':
	'''
2. Boolean operations. Many search engines support Boolean queries, which allow
users to construct searches like "python OR perl." An OR search can work by
doing the queries separately and combining the results, but what about "python
AND (program OR code)"? Modify the query methods to support some basic
Boolean operations.
3. Exact matches. Search engines often support "exact match" queries, where the
words in the page must match the words in the query in the same order with no
additional words in between. Create a new version of getrows that only returns
results that are exact matches. (Hint: you can use subtraction in SQL to get the
difference between the word locations.)	
	'''

	crawler=se.crawler('searchindex.db')
	crawler.createindextables()
	pages= ['https://en.wikipedia.org/wiki/Thomas_Wayne']
	crawler.crawl(pages)