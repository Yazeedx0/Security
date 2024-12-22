import hashlib
import hmac
import time

def create_message_with_mac(message, key):
    timestamp = str(int(time.time()))  # Timestamp for message freshness
    message_with_timestamp = f"{message}|{timestamp}"
    mac = hmac.new(key, message_with_timestamp.encode(), hashlib.sha256).hexdigest()
    return f"{message_with_timestamp}|{mac}"

def verify_message(message_with_mac, key):
    parts = message_with_mac.rsplit('|', 1)
    if len(parts) != 2:
        return False
    message, mac = parts
    expected_mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_mac, mac)