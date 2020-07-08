import requests


class AINewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=artificial+intelligence&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class RoboticsNewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=robots&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class BDNewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=big+data&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class CCNewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=cloud+computing&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class IOTNewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=iot&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class EnergyNewsScrapper():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=renewable+energy&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class BrainNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=brain&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class GeneEditNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=gene+edit&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class NanotechNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=nanotechnology&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class SpaceNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=space&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class SynthBioNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=synthetic+biology&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response


class BlockchainNews():
    def __init__(self):
        self.url = "http://newsapi.org/v2/everything?q=blockchain&pageSize=10" \
                   "&language=en&sortBy=publishedAt&apiKey=085fcc80c1ff4a4199279071b3341182"
        self.response = requests.get(self.url).json()

    def getNews(self):
        return self.response
