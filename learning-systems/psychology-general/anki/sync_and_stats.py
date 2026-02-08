#!/usr/bin/env python3
"""
Sync Annie's Anki collection from AnkiWeb and extract learning statistics
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta

def get_ankiweb_credentials():
    """Read AnkiWeb credentials"""
    config_file = Path(__file__).parent / '.ankiweb_config'
    if not config_file.exists():
        return None
    
    with open(config_file) as f:
        config = json.load(f)
    
    return config.get('username'), config.get('password')

def sync_collection():
    """Sync collection from AnkiWeb"""
    # This requires ankisyncd or direct AnkiWeb sync
    # For now, we'll need to check if there's a local collection
    print("⚠️ Direct AnkiWeb sync requires Anki desktop to be running")
    print("   Checking for local collection...")
    return None

def analyze_local_collection():
    """Analyze local Anki collection if available"""
    try:
        from anki.collection import Collection
        
        # Try to find collection in common locations
        possible_paths = [
            Path.home() / '.local/share/Anki2/User 1/collection.anki2',
            Path.home() / 'Documents/Anki2/User 1/collection.anki2',
            Path(__file__).parent / 'collection.anki2'
        ]
        
        col_path = None
        for path in possible_paths:
            if path.exists():
                col_path = str(path)
                break
        
        if not col_path:
            return {
                'status': 'error',
                'message': 'No local Anki collection found'
            }
        
        # Open collection
        col = Collection(col_path)
        
        # Get deck info
        decks = col.decks.all()
        
        stats = {
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'decks': []
        }
        
        for deck in decks:
            deck_id = deck['id']
            deck_name = deck['name']
            
            # Filter to Psychology deck
            if 'Psychology' not in deck_name:
                continue
            
            # Get card counts
            card_counts = col.sched.deck_due_tree()
            
            # Get statistics
            deck_stats = {
                'name': deck_name,
                'total_cards': col.card_count(),
                'new_cards': len(col.find_cards(f'"deck:{deck_name}" is:new')),
                'learning_cards': len(col.find_cards(f'"deck:{deck_name}" is:learn')),
                'review_cards': len(col.find_cards(f'"deck:{deck_name}" is:review')),
                'suspended': len(col.find_cards(f'"deck:{deck_name}" is:suspended'))
            }
            
            stats['decks'].append(deck_stats)
        
        col.close()
        return stats
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error analyzing collection: {str(e)}'
        }

def check_ankiconnect():
    """Check if AnkiConnect is available"""
    import requests
    
    try:
        response = requests.post('http://localhost:8765', json={
            'action': 'version',
            'version': 6
        }, timeout=2)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'available': True,
                'version': data.get('result')
            }
    except:
        pass
    
    return {'available': False}

def get_stats_via_ankiconnect():
    """Get statistics via AnkiConnect API"""
    import requests
    
    def invoke(action, **params):
        response = requests.post('http://localhost:8765', json={
            'action': action,
            'version': 6,
            'params': params
        })
        return response.json()
    
    try:
        # Get deck names
        decks = invoke('deckNames')['result']
        
        # Filter Psychology decks
        psych_decks = [d for d in decks if 'Psychology' in d or 'psychology' in d]
        
        stats = {
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'decks': []
        }
        
        for deck_name in psych_decks:
            # Get deck stats
            deck_stats = invoke('getDeckStats', deck=deck_name)['result']
            
            # Get card counts
            cards = invoke('findCards', query=f'"deck:{deck_name}"')['result']
            new_cards = invoke('findCards', query=f'"deck:{deck_name}" is:new')['result']
            learning = invoke('findCards', query=f'"deck:{deck_name}" is:learn')['result']
            review = invoke('findCards', query=f'"deck:{deck_name}" is:review')['result']
            
            stats['decks'].append({
                'name': deck_name,
                'total_cards': len(cards),
                'new_cards': len(new_cards),
                'learning_cards': len(learning),
                'review_cards': len(review),
                'deck_stats': deck_stats
            })
        
        return stats
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'AnkiConnect error: {str(e)}'
        }

def main():
    print("🔍 Checking Anki progress tracking options...\n")
    
    # Check AnkiConnect
    ankiconnect = check_ankiconnect()
    
    if ankiconnect['available']:
        print(f"✅ AnkiConnect is available (version {ankiconnect['version']})")
        print("   Fetching statistics via AnkiConnect...\n")
        
        stats = get_stats_via_ankiconnect()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return 0
    
    print("❌ AnkiConnect is not available")
    print("   (Anki desktop needs to be running with AnkiConnect plugin installed)\n")
    
    # Try local collection
    print("🔍 Checking for local Anki collection...")
    stats = analyze_local_collection()
    
    if stats['status'] == 'success':
        print("✅ Found local collection\n")
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return 0
    
    print(f"❌ {stats['message']}\n")
    
    # Show instructions
    print("📋 To enable automatic progress tracking:\n")
    print("Option 1: AnkiConnect (Recommended)")
    print("  1. Install Anki Desktop on your computer")
    print("  2. Install AnkiConnect add-on (code: 2055492159)")
    print("  3. Keep Anki Desktop running in background")
    print("  4. I can then query your progress anytime\n")
    
    print("Option 2: Manual sync")
    print("  1. Export your collection from Anki")
    print("  2. Share the collection.anki2 file with me")
    print("  3. I'll analyze it manually\n")
    
    print("Option 3: Manual reporting")
    print("  - Just tell me your stats when we do weekly check-ins")
    print("  - Simplest but requires your input\n")
    
    return 1

if __name__ == '__main__':
    sys.exit(main())
