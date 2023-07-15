# Hacker News Article Scraper

This project is a Python script that scrapes articles from Hacker News and displays the best articles based on the number of votes. It utilizes the `requests` library to fetch the HTML content of the web pages and the `BeautifulSoup` library to parse and extract relevant information from the HTML. The scraped articles are then sorted by the number of votes and displayed using the `pprint` module.

## Dependencies

To run this script, you need to have Python installed.

The project relies on the following Python libraries:

- `requests`: You can install it by running `pip install requests`.
- `beautifulsoup4`: You can install it by running `pip install beautifulsoup4`.
- `pprint`: It is a built-in module in Python.

Make sure to install these dependencies before running the script.

## Usage

1. Open the Python script file `scrape_hacker_news.py` in your preferred IDE or text editor.
2. Configure the number of pages you want to scrape by modifying the `pages` variable.
3. Run the script using the following command:

```
python scrape_hacker_news.py
```

4. Enter the number of pages you want to scrape when prompted.
5. The script will scrape the articles, sort them by votes, and display the best articles.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request in this repository.

