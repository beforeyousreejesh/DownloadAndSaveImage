from UrlProvider import UrlProvider

class FileUrlProvider(UrlProvider):
    """File Url provider from given file"""

    def __init__(self,filename):
       self.filename=filename

    def GetUrls(self):
        """Get urls from given file"""
        try:
            with open(self.filename,"r") as file:
              self.DownloadUrl = file.read().splitlines() # reading urls from given file
            return self.DownloadUrl
        except Exception as err:
            pass
    
