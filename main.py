import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ReviewScraper:
	def __init__(self, url: str):
		self.url = url
		self.driver = webdriver.Chrome()
		self.data = []

	def clean_text(self, text: str) -> str:
		"""Cleans the input text by stripping whitespace and removing newlines."""
		return text.replace('\n', ' ').strip()

	def get_review_data(self, container) -> dict[str, str]:
		"""Extracts review data from a given container."""
		try:
			username = container.find('span', class_='name').text
			ulasan = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text if container.find('span', attrs={'data-testid': 'lblItemUlasan'}) else ""
			rating = container.find('div', attrs={'data-testid': 'icnStarRating'}).get('aria-label').split(' ')[1]
			waktu_komentar = container.find('p', class_='css-1dfgmtm-unf-heading').text

			"""Extracts media URLs from the review container."""
			media = [img.get('src') for img in container.find_all("img", attrs={'data-testid': 'imgItemPhotoulasan'})]
			
			return {
				'Username': username,
				'Review': self.clean_text(ulasan),
				'Media': ', '.join(media),
				'Rating': rating,
				'Date': waktu_komentar
			}
		except AttributeError:
			return None

	def load_all_reviews(self) -> list[dict]:
		"""Loads all reviews from the specified URL."""
		page_number = 1

		while True:
			time.sleep(3)
			try:
				buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.css-89c2tx")
				for button in buttons:
					button.click()
					time.sleep(1)
			except Exception as e:
				pass
				# Uncomment this line if you want to see the error message
				# print("Error loading more reviews:", e)

			soup = BeautifulSoup(self.driver.page_source, "html.parser")
			containers = soup.find("section", attrs={'id': 'review-feed'}).find_all("article")

			for container in containers:
				review_data = self.get_review_data(container)
				if review_data:
					self.data.append(review_data)

			print(f'Page {page_number} Loaded {len(self.data)} reviews')
			page_number += 1

			try:
				time.sleep(2)
				next_button = WebDriverWait(self.driver, 10).until(
					EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']"))
				)
				next_button.click()
			except Exception as e:
				print("Maximum page reached.")
				break

		return self.data

	def run(self) -> None:
		self.driver.get(self.url)
		self.driver.minimize_window()

		review_data = self.load_all_reviews()
		self.driver.quit()

		df = pd.DataFrame(review_data)
		df.to_csv('tokopedia_review.csv', index=False)
		print("Reviews saved to 'tokopedia_review.csv'.")

def main() -> None:
	url = "https://www.tokopedia.com/project1945/project-1945-sunset-in-sumba-perfume-edp-parfum-unisex-100ml-2-0-e8aa9/review"
	scraper = ReviewScraper(url)
	scraper.run()

if __name__ == "__main__":
	main()