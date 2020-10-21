'''
Repeat the 002... exercise, but using thread pool instead of thread primitives 
'''

from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool


def main():
    urls = [
        "http://www.python.org",
        "http://www.yahoo.com",
        "http://www.scala.org",
        "http://www.google.com",
        "http://matthewcale.com",
    ]

    pool = ThreadPool(4)
    results = map(urlopen, urls)
    [print(result.status) for result in results]
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

