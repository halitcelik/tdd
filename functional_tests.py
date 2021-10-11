from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_if_someone_can_start_a_list_and_retrieve_it(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")


if __name__ == "__main__":
    unittest.main()
