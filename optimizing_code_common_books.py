import time
import pandas as pd
import numpy as np


with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')


start = time.time()
'''using loops:'''
# recent_coding_books = []
# for book in recent_books:
#     if book in coding_books:
#         recent_coding_books.append(book)
# [OUTPUT]    96        Duration: 13.361320495605469 seconds

'''use vector instead of loops:'''
# recent_coding_books = np.intersect1d (recent_books,coding_books)
# [OUTPUT]    96        Duration: 0.028925418853759766 seconds

'''Use Python's set intersection: [FASTEST]'''
recent_coding_books = list(set(recent_books).intersection(coding_books))
# [OUTPUT]    96        Duration: 0.00695037841796875 seconds

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))