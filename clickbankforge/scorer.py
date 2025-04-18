from typing import List, Dict

def rank_by_potential(offers: List[Dict]) -> List[Dict]:
    """
    Rank offers by their monetization potential (gravity × commission).
    
    Args:
        offers: List of offer dictionaries
        
    Returns:
        List of offers sorted by potential score
    """
    # Calculate score for each offer
    for offer in offers:
        gravity = float(offer.get('gravity', 0))
        commission = float(offer.get('commission', 0))
        offer['potential_score'] = gravity * commission
    
    # Sort by potential score in descending order
    return sorted(offers, key=lambda x: x['potential_score'], reverse=True) 