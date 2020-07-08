import requests

class USNewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=us&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class HKNewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=hk&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class TWNewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=tw&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class CANewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=ca&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class UKNewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=gb&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class ChinaNewsScrapper():
    def __init__(self):
        self.url = 'http://newsapi.org/v2/top-headlines?country=cn&' \
                   'pageSize=10&apiKey=085fcc80c1ff4a4199279071b3341182'
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response
