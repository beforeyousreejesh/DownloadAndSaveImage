from abc import ABCMeta,abstractmethod

class UrlProvider(metaclass=ABCMeta):
    """Base class for Url fetcher"""

    def __init__(self):
        self.DownloadUrl=[];

    @abstractmethod
    def GetUrls(self):
      return self.DownloadUrl


