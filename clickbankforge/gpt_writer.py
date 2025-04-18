import os
from typing import List, Dict
import openai
from dotenv import load_dotenv

def generate_promos(offers: List[Dict]) -> List[Dict]:
    """
    Generate promotional content for each offer using GPT.
    
    Args:
        offers: List of offer dictionaries
        
    Returns:
        List of offers with generated content
    """
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    for offer in offers:
        prompt = f"""
        Create a viral Reddit-style post for this ClickBank offer:
        Title: {offer.get('title', '')}
        Description: {offer.get('description', '')}
        Commission: {offer.get('commission', 0)}%
        Gravity: {offer.get('gravity', 0)}
        
        Generate:
        1. A catchy Reddit post title
        2. A 2-line hook
        3. A short Reddit-style post (2-3 paragraphs)
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a skilled copywriter specializing in viral Reddit posts."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = response.choices[0].message.content
            offer['generated_content'] = content
            
        except Exception as e:
            print(f"Error generating content for {offer.get('title')}: {e}")
            offer['generated_content'] = "Content generation failed"
    
    return offers 