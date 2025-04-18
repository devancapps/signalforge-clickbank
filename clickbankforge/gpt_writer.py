import os
from typing import List, Dict
import openai
from dotenv import load_dotenv

def generate_promos(offers: List[Dict]) -> List[Dict]:
    """
    Generate viral Reddit-style promotional content for each offer using GPT.
    
    Args:
        offers: List of offer dictionaries
        
    Returns:
        List of offers with generated promotional content
    """
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    for offer in offers:
        prompt = f"""
        Create a 2-3 sentence Reddit-style promotional post for:
        Product: {offer.get('title', '')}
        Category: {offer.get('category', '')}
        Commission: {offer.get('commission', 0)}%
        Gravity: {offer.get('gravity', 0)}
        
        Pitch this to people looking for high-paying affiliate products.
        Make it snappy, persuasive, and curious — no hard selling.
        Use Reddit-style formatting and tone.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a skilled Reddit marketer who creates viral, engaging posts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            content = response.choices[0].message.content.strip()
            offer['promo'] = content
            
        except Exception as e:
            print(f"Error generating content for {offer.get('title')}: {e}")
            offer['promo'] = f"GPT ERROR: {e}"
    
    return offers 