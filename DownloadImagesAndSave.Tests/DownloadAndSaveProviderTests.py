from TestUrlProvider import TestUrlProvider
from DownloadAndSaveProvider import DownloadAndSaveProvider
import unittest

class Test_DownloadAndSaveProviderTests(unittest.TestCase):

    def setUp(self):
        self.savefilePath=r"E:\Images"

    def test_DownloadandSaveImage_SuccessAllFiles(self):
        urlProvider = TestUrlProvider(1)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),0)

    def test_DownloadandSaveImage_FailAllFiles(self):
        urlProvider = TestUrlProvider(2)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),3)

    def test_DownloadandSaveImage_FailFewFiles(self):
        urlProvider = TestUrlProvider(3)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),1)

    def test_DownloadandSaveImage_InvalidContentType_FailAll(self):
        urlProvider = TestUrlProvider(4)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),1)

    def test_DownloadandSaveImage_InvalidPath_FailAll(self):
        urlProvider = TestUrlProvider(1)
        downloadProvider = DownloadAndSaveProvider(urlProvider,r"E:\InvalidPath")
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),3)

    def test_DownloadandSaveImage_InvalidResponse_FailAll(self):
        urlProvider = TestUrlProvider(5)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        failedCount=downloadProvider.DownloadandSave()
        self.assertEqual(len(failedCount),1)

    def test_DownloadandSaveImage_EmptyUrls_FailAll(self):
        urlProvider = TestUrlProvider(6)
        downloadProvider = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        self.assertRaises(ValueError,downloadProvider.DownloadandSave)

    def test_DownloadandSaveImage_SuccessAll_CountsShouldBeEqual(self):
        urlProvider = TestUrlProvider(1)

        downloadProviderFirst = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        downloadProviderSecond = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        self.assertCountEqual(downloadProviderFirst.DownloadandSave(),downloadProviderSecond.DownloadandSave())

    def test_DownloadandSaveImage_FailAll_CountsShouldBeEqual(self):
        urlProvider = TestUrlProvider(2)
        downloadProviderFirst = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        downloadProviderSecond = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        self.assertCountEqual(downloadProviderFirst.DownloadandSave(),downloadProviderSecond.DownloadandSave())

    def test_DownloadandSaveImage_FailFew_CountsShouldBeEqual(self):
        urlProvider = TestUrlProvider(3)
        downloadProviderFirst = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        downloadProviderSecond = DownloadAndSaveProvider(urlProvider,self.savefilePath)
        self.assertCountEqual(downloadProviderFirst.DownloadandSave(),downloadProviderSecond.DownloadandSave())

if __name__ == '__main__':
    unittest.main()
