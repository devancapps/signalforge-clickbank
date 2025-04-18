# signalforge-clickbank

Scans high-payout digital offers from ClickBank and auto-generates viral promo copy.

## Features
- Sort by gravity × commission
- GPT writes 2-liners or Reddit bait
- Telegram alert to core when finished

## Installation

1. Clone the repository:
```bash
git clone https://github.com/devancapps/signalforge-clickbank.git
cd signalforge-clickbank
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

## Usage

Run the main pipeline:
```bash
python main.py
```

## Project Structure
```
signalforge-clickbank/
├── main.py
├── clickbankforge/
│   ├── scraper.py                # Scrape top ClickBank offers
│   ├── scorer.py                 # Rank offers by monetization potential
│   ├── gpt_writer.py             # Write viral Reddit-style content
│   ├── alert_bridge.py          # Sends alert to Telegram/Slack via core
│   └── exporter.py              # Save output to CSV/Notion
├── offer_samples/top_products.json  # Static fallback for scraping
├── output/
│   └── offers.csv
├── .env.example
├── requirements.txt
└── README.md
```

## License
MIT License - See LICENSE file for details 