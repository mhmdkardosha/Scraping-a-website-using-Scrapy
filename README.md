# bookscraper

A Scrapy project to scrape book data from [books.toscrape.com](https://books.toscrape.com).

## Features

- Crawls all book listings
- Extracts title, description, price, star rating, category, tax, availability, and number of reviews
- Outputs data as CSV

## Requirements

- Python 3.8+
- Scrapy

## Setup

1. Install dependencies:

   ```bash
   pip install scrapy
   ```

2. Navigate to the project directory:

   ```bash
   cd bookscraper
   ```

3. Run the spider:

   ```bash
   scrapy crawl bookspider -o output.csv
   ```

## Output

- The spider outputs book data to a CSV file (e.g., `output.csv`).

## License

See [LICENSE](LICENSE).
