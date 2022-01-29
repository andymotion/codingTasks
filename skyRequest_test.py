import unittest
import skyMethods

#Returns a list of articles
sky_endpoint_one = 'https://5f99522350d84900163b8737.mockapi.io/tech-test/articles'

#Returns a single article
sky_endpoint_two = 'https://5f99522350d84900163b8737.mockapi.io/tech-test/articles/2'


class TestCallMethods(unittest.TestCase):

    #Test the POST method
    def test_post(self):
        self.assertEqual(skyMethods.post(sky_endpoint_one), 404)
        self.assertEqual(skyMethods.post(sky_endpoint_two), 404)

    #Test the PUT method
    def test_put(self):
        self.assertEqual(skyMethods.put(sky_endpoint_one), 404)
        self.assertEqual(skyMethods.put(sky_endpoint_two), 404)


    #Test the DELETE method
    def test_delete(self):
        self.assertEqual(skyMethods.delete(sky_endpoint_one), 404)
        self.assertEqual(skyMethods.delete(sky_endpoint_two), 404)


if __name__ == '__main__':
    unittest.main()