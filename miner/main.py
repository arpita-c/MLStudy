import searchengine as se
import ast

eval_tests = [
    "a and b",
    "a or b",
    "a and (b or c)",
]

class MyVisitor(ast.NodeVisitor):
    def visit_Name(self, node):
        print 'Found string "%s"' % node
    def visit_BoolOp(self, node):
        if isinstance(node, ast.BinOp) and \
             isinstance(node.op, (ast.And, ast.Or)):
            # fields = [(a, _format(b)) for a, b in iter_fields(node)]
            print 'Found Object "%s"' % node
            print node.left
            print node.right

for test in  eval_tests:
    node = ast.parse(test)
    print ast.dump(node)
    MyVisitor().visit(node)
    print '\n'

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
	dbname = 'searchindex.db'
	if False:
		crawler = se.crawler(dbname)
		crawler.createindextables()
		pages = ['https://www.zhihu.com/']
		crawler.crawl(pages, depth=3)
	else:
		searcher = se.searcher(dbname)
		print searcher.getmatchrows('zhihu career')

