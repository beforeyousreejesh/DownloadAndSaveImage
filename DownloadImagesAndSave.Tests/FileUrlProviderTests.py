from FileUrlProvider import FileUrlProvider
import unittest

class Test_FileUrlProvider(unittest.TestCase):

    def test_GetUrl_ValidateFilePath_ShouldReturnUrls(self):
        fileurlprovider = FileUrlProvider(r"E:\test.txt")
        self.assertIsNotNone(fileurlprovider.GetUrls())

    def test_GetUrl_ValidateFilePath_ShouldThrowException(self):
        fileurlprovider = FileUrlProvider(r"E:\test1.txt")
        self.assertRaises(IOError,fileurlprovider.GetUrls())

    def test_GetUrl_ValidateNumberOfUrls_ShouldReturnNUrls(self):
        fileurlprovider = FileUrlProvider(r"E:\test.txt")
        length=len(fileurlprovider.GetUrls())
        self.assertEqual(length,4)

    def test_GetUrl_ValidateNumberOfUrls_ShouldReturnUnExptectedNumberOfUrl(self):
        fileurlprovider = FileUrlProvider(r"E:\test.txt")
        length=len(fileurlprovider.GetUrls())
        self.assertNotEqual(length,5)

    def test_GetUrl_ValidateSameFilesUrlCount_ShouldReturnEqualNumberOfUrl(self):
        fileurlproviderFirst = FileUrlProvider(r"E:\test.txt")
        fileurlproviderSecond = FileUrlProvider(r"E:\test.txt")
        self.assertCountEqual(fileurlproviderFirst.GetUrls(),fileurlproviderSecond.GetUrls())

if __name__ == '__main__':
    unittest.main()
