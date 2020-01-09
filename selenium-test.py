import pdb; pdb.set_trace()
from selenium import webdriver
import pdb; pdb.set_trace()
download_dir = "/pathToDownloadDir"
chrome_options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory": download_dir,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
}
chrome_options.add_experimental_option("prefs", preferences)
import pdb; pdb.set_trace()
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"./chromedriver")
import pdb; pdb.set_trace()
