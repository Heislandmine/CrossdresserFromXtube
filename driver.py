from selenium import webdriver


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Selenium Server に接続する
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=options.to_capabilities(),
            options=options,
        )
        self.driver = driver
