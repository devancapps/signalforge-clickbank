from clickbankforge.scraper import load_top_clickbank_products
from clickbankforge.scorer import rank_by_potential
from clickbankforge.gpt_writer import generate_promos
from clickbankforge.exporter import export_csv
from clickbankforge.alert_bridge import notify_core
import os
from dotenv import load_dotenv

def main():
    print("[ClickBank] Running offer pipeline...")
    
    # Load environment variables
    load_dotenv()
    
    # Load and process offers
    offers = load_top_clickbank_products("offer_samples/top_products.json")
    ranked = rank_by_potential(offers)
    
    # Generate promotional content
    promos = generate_promos(ranked)
    
    # Export results
    os.makedirs("output", exist_ok=True)
    export_csv(promos, "output/promos.csv")
    
    # Send notification if enabled
    if os.getenv("SEND_ALERTS", "true").lower() == "true":
        notify_core(f"✅ Clickbank promos generated for {len(promos)} offers!")

if __name__ == "__main__":
    main() 