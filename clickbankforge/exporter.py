import pandas as pd
import csv
from typing import List, Dict
import os
from notion_client import Client
from dotenv import load_dotenv

def export_csv(offers: List[Dict], output_path: str = "output/promos.csv") -> None:
    """
    Export offers to CSV file with specific fields.
    
    Args:
        offers: List of offer dictionaries
        output_path: Path to save the CSV file
    """
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Define the fields we want to export
    keys = ["title", "category", "commission", "gravity", "promo"]
    
    # Write to CSV
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(offers)
    
    print(f"Exported {len(offers)} offers to {output_path}")

def export_notion(offers: List[Dict], database_id: str) -> None:
    """
    Export offers to Notion database.
    
    Args:
        offers: List of offer dictionaries
        database_id: Notion database ID
    """
    load_dotenv()
    notion = Client(auth=os.getenv("NOTION_TOKEN"))
    
    for offer in offers:
        try:
            notion.pages.create(
                parent={"database_id": database_id},
                properties={
                    "Title": {"title": [{"text": {"content": offer.get("title", "")}}]},
                    "Category": {"rich_text": [{"text": {"content": offer.get("category", "")}}]},
                    "Commission": {"number": float(offer.get("commission", 0))},
                    "Gravity": {"number": float(offer.get("gravity", 0))},
                    "Promo": {"rich_text": [{"text": {"content": offer.get("promo", "")}}]}
                }
            )
        except Exception as e:
            print(f"Failed to export offer to Notion: {e}")
    
    print(f"Exported {len(offers)} offers to Notion database") 