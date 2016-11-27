from FileUrlProvider import FileUrlProvider
from DownloadAndSaveProvider import DownloadAndSaveProvider
import sys,getopt

def main(argv):
   inputfile = ''
   outputFolder = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputfile=","outputfolder="])
   except getopt.GetoptError:
      print('DownloadImagesAndSave.py -i <inputfile> -o <outputfolder>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('DownloadImagesAndSave.py -i <inputfile> -o <outputfolder>')
         sys.exit()
      elif opt in ("-i", "--inputfile"):
         inputfile = arg
      elif opt in ("-o", "--outputfolder"):
         outputFolder = arg
   print ('Input file is {0}'.format(inputfile))
   print ('Output folder is {0}'.format(outputFolder))   

   if inputfile is None or not inputfile:
       print ('Input file cannot be empty')
       sys.exit()
   else:
        try:
            print("Start processing...")
            print("...................")
            urlProvider= FileUrlProvider(inputfile)
            downloandImageAndSaveProvider=DownloadAndSaveProvider(urlProvider,outputFolder)
            failedUrls=downloandImageAndSaveProvider.DownloadandSave()
            totalUrls=downloandImageAndSaveProvider.urlProvider.DownloadUrl

            print("Process completed")
            print("...................")

            print("Total Url processed {0}".format(len(totalUrls)))
            print("Failed Urls {0}".format(len(failedUrls)))
        except Exception as err:
            print("Unexpected error occured. Error is {0}".format(err))
            sys.exit()
if __name__ == "__main__":
   main(sys.argv[1:])