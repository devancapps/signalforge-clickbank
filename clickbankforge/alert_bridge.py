import os
import requests
from dotenv import load_dotenv

def notify_core(message: str) -> bool:
    """
    Send notification to Telegram via signalforge-core.
    
    Args:
        message: The message to send
        
    Returns:
        bool: True if notification was sent successfully
    """
    load_dotenv()
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        print("Telegram credentials not found. Skipping notification.")
        return False
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        
        response = requests.post(url, data=data)
        response.raise_for_status()
        return True
        
    except Exception as e:
        print(f"Failed to send Telegram notification: {e}")
        return False 