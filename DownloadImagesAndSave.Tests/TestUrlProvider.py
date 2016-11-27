from UrlProvider import UrlProvider

class TestUrlProvider(UrlProvider):
    """Url provider for test purpose"""

    def __init__(self,option):
        self.options = {
        1 : "Test_SuccessAll",
        2 : "Test_FailAll",
        3 : "Test_FailOrSuccessFew",
        4 : "Test_InvalidContentType",
        5 : "Test_InvalidResponseCode",
        6 : "Test_EmptyUrl"
        }
        self.option=option

    def GetUrls(self):
        method_name=self.options[self.option]
        method=getattr(self,method_name,lambda:"nothing")
        return method()


    def Test_SuccessAll(self):
       self.DownloadUrl = ["https://s-media-cache-ak0.pinimg.com/236x/38/cb/d0/38cbd0f6b73df4414c6831806b65a070.jpg",
                           "http://www.autumnhillnursery.com/wp-content/uploads/2012/03/Perfect-Moment-.jpg",
                           "https://s-media-cache-ak0.pinimg.com/236x/22/04/13/22041377bfcbcad4fddb4a6799c19fc5.jpg"]
       return self.DownloadUrl

    def Test_FailAll(self):
        self.DownloadUrl = ["https://s-media-cache-ak0.pi.com/236x/38/cb/d0/38cbd0f6b73df4414c6831806b65a070.jpg",
                            "http://www.autumnhillnursery.com/wp-c/uploads/2012/03/Perfect-Moment-.jpg",
                            "https://s-media-cache-ak0.pig.com/236x/22/04/13/22041377bfcbcad4fddb4a6799c19fc5.jpg"]
        return self.DownloadUrl

    def Test_FailOrSuccessFew(self):
        self.DownloadUrl = ["https://s-media-cache-ak0.pinimg.com/236x/38/cb/d0/38cbd0f6b73df4414c6831806b65a070.jpg",
                           "http://www.autumnhillnursery.com/wp-content/up/2012/03/Perfect-Moment-.jpg",
                           "https://s-media-cache-ak0.pinimg.com/236x/22/04/13/22041377bfcbcad4fddb4a6799c19fc5.jpg"]
        return self.DownloadUrl

    def Test_InvalidResponseCode(self):
        self.DownloadUrl = ["http://www.frontiersin.org/test"]
        return self.DownloadUrl
    
    def Test_InvalidContentType(self):
        self.DownloadUrl = ["https://www.google.co.in"]
        return self.DownloadUrl

    def Test_EmptyUrl(self):
        self.DownloadUrl = []
        return self.DownloadUrl