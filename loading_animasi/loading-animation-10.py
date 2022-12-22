#

from time import sleep
from progress.bar import Bar

with Bar('Processing',max = 5) as bar:
    for i in range(5):
        sleep(0.1)
        print('\n',i)
        bar.next()