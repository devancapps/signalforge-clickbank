import pandas as pd
from typing import List, Dict
import os
from notion_client import Client
from dotenv import load_dotenv

def export_csv(offers: List[Dict], output_path: str) -> None:
    """
    Export offers to CSV file.
    
    Args:
        offers: List of offer dictionaries
        output_path: Path to save the CSV file
    """
    df = pd.DataFrame(offers)
    df.to_csv(output_path, index=False)
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
                    "Description": {"rich_text": [{"text": {"content": offer.get("description", "")}}]},
                    "Commission": {"number": float(offer.get("commission", 0))},
                    "Gravity": {"number": float(offer.get("gravity", 0))},
                    "Potential Score": {"number": float(offer.get("potential_score", 0))},
                    "Content": {"rich_text": [{"text": {"content": offer.get("generated_content", "")}}]}
                }
            )
        except Exception as e:
            print(f"Failed to export offer to Notion: {e}")
    
    print(f"Exported {len(offers)} offers to Notion database") 