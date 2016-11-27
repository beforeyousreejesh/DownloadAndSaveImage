from UrlProvider import UrlProvider
import re
import requests
import configparser

class DownloadAndSaveProvider(object):
    """Provider for managing Image download and save to given path"""

    def __init__(self,urlProvider,saveFilePath):
      if urlProvider is None:
        raise TypeError("Argument passed {0} is None".format(urlProvider))

      if not isinstance(urlProvider,UrlProvider):
        raise TypeError("Argument passed {0} is not type of UrlProvider".format(urlProvider))

      self.urlProvider = urlProvider
      self.saveFilePath = saveFilePath
      self.FailedUrl = []

    def DownloadandSave(self):
          """Download and save image for given urls. Url provder should be dynamic"""

          print("Retrieving URL's from Url provider")
          print("...................")
          fileDownloadUrls = self.urlProvider.GetUrls()
          print("Retrieved URL's from Url provider")
          print("...................")
          if len(fileDownloadUrls) <= 0:
            raise ValueError("Could not find any URL")

          for url in fileDownloadUrls:
            try:
                #Getting the image name from url
                regex = r"(^.*\/)([^\/]+\.[\S]+$)" # More generic can be more specific
                matchObj = re.match(regex,url,re.M | re.I)

                if matchObj:
                    if self.saveFilePath is not None:
                        destination = self.saveFilePath + "/" + matchObj.group(2)
                    else:
                        destination = matchObj.group(2)
                else:
                    print("Invalid Url")
                    self.FailedUrl.append(url)
                    continue
                print("Downloading & saving {0}".format(url))
                print("...................")
                # Getting response
                uriResponse = requests.get(url)

                if uriResponse.status_code == 200: # we know status code should be 200 ( as per HTTP standard).
                    contentType = uriResponse.headers['content-type']

                    if self.__IsValidMimeType(contentType):  # checking if valid content type for response
                        with open(destination, 'wb') as f:
                          for chunk in uriResponse.iter_content(chunk_size=1024): # avoiding keeping large images in memory. Wrting as chunks of 1024 bytes
                                if chunk: # filter out keep-alive new chunks
                                   f.write(chunk)
                        print("Downloaded & saved {0}".format(url))
                        print("...................")
                    else:
                        print("Download failed for {0}. Invalid Image".format(url)) # Logging invalid content type
                        self.FailedUrl.append(url)
                        continue
                else:
                    print("Download failed for {0}. Invalid Reponse. Response code is{1}".format(url,uriResponse.status_code)) # Logging invalid response from server(other than 200).
                    self.FailedUrl.append(url)
                    continue

            except Exception as err:
                self.FailedUrl.append(url)

                print("Error occured while downloading {0}. Error message:{1}".format(url,err)) # Logging unexpected error
          return self.FailedUrl

    def __IsValidMimeType(self,mimeType):
            """Checking if given MimeType is in configured MimeTypes"""  
                  
            config = configparser.ConfigParser()
            config.readfp(open('config.cfg'))
            validTypes=config.get("common","image_mime_type")
            if mimeType in validTypes:
                isValid = True
            else:
                isValid = False
            return isValid



