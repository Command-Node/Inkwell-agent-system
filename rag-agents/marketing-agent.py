"""
Marketing Agent for InkWell AI Writing Agency
Handles book marketing strategy, audience analysis, and promotional planning
"""

import asyncio
from typing import Dict, List, Any
from dataclasses import dataclass
import importlib.util
import sys

# Import CrewAI integration
spec = importlib.util.spec_from_file_location("crew_ai_integration", "crew-ai-integration.py")
crew_ai_integration = importlib.util.module_from_spec(spec)
sys.modules["crew_ai_integration"] = crew_ai_integration
spec.loader.exec_module(crew_ai_integration)

@dataclass
class MarketingStrategy:
    target_audience: str
    key_messaging: List[str]
    promotional_channels: List[str]
    launch_timeline: Dict[str, str]
    budget_allocation: Dict[str, float]

class MarketingAgent:
    """
    Marketing Agent - David "Buzz" Martinez
    Creates comprehensive marketing strategies for books
    """
    
    def __init__(self):
        self.crew_ai = crew_ai_integration.CrewAIIntegration()
        self.personality = self.crew_ai.get_agent_personality("marketing")
        self.knowledge_base = self._load_marketing_knowledge()
        
    def _load_marketing_knowledge(self) -> Dict[str, Any]:
        """Load marketing knowledge base"""
        return {
            "audience_segments": [
                "Young Adult (13-18)", "New Adult (18-25)", "Adult (25-45)", 
                "Mature Adult (45+)", "Academic", "Professional"
            ],
            "marketing_channels": [
                "Social Media (Instagram, TikTok, Twitter)", "Book Bloggers", 
                "Influencer Partnerships", "Book Clubs", "Libraries", 
                "Bookstores", "Online Ads", "Email Marketing"
            ],
            "genre_marketing": {
                "Fantasy": ["Fantasy conventions", "Gaming communities", "Cosplay groups"],
                "Romance": ["Romance book clubs", "Dating apps", "Wedding blogs"],
                "Mystery": ["True crime podcasts", "Detective forums", "Puzzle communities"],
                "Business": ["LinkedIn", "Professional associations", "Industry conferences"]
            }
        }
    
    def create_marketing_strategy(self, book_info: Dict[str, Any]) -> MarketingStrategy:
        """
        Create a comprehensive marketing strategy for a book
        """
        print(f"\n*adjusts marketing hat and pulls out analytics dashboard*")
        print(f"Hey there! I'm {self.personality.name}, and I'm excited to create a killer marketing strategy for your book!")
        print(f"{self.personality.personality}")
        
        # Analyze book and create strategy
        target_audience = self._analyze_target_audience(book_info)
        key_messaging = self._create_key_messaging(book_info)
        promotional_channels = self._select_promotional_channels(book_info)
        launch_timeline = self._create_launch_timeline()
        budget_allocation = self._allocate_budget(promotional_channels)
        
        print(f"\n*consults marketing playbook*")
        print(f"Perfect! I've created a comprehensive marketing strategy that targets {target_audience}.")
        print(f"✅ Marketing strategy created successfully!")
        
        return MarketingStrategy(
            target_audience=target_audience,
            key_messaging=key_messaging,
            promotional_channels=promotional_channels,
            launch_timeline=launch_timeline,
            budget_allocation=budget_allocation
        )
    
    def _analyze_target_audience(self, book_info: Dict[str, Any]) -> str:
        """Analyze and determine target audience"""
        genre = book_info.get("genre", "General")
        tone = book_info.get("tone", "Neutral")
        
        if genre == "Fantasy":
            return "Young Adult (13-18) and Adult (25-45) fantasy enthusiasts"
        elif genre == "Romance":
            return "Adult (25-45) romance readers, primarily female audience"
        elif genre == "Business":
            return "Professional (25-45) business professionals and entrepreneurs"
        else:
            return "General Adult (25-45) readers"
    
    def _create_key_messaging(self, book_info: Dict[str, Any]) -> List[str]:
        """Create key marketing messages"""
        genre = book_info.get("genre", "General")
        tone = book_info.get("tone", "Neutral")
        
        messages = [
            f"Discover a {tone.lower()} {genre.lower()} story that will keep you turning pages",
            f"Perfect for readers who love {genre.lower()} with {tone.lower()} elements",
            f"A must-read for {genre.lower()} enthusiasts"
        ]
        
        return messages
    
    def _select_promotional_channels(self, book_info: Dict[str, Any]) -> List[str]:
        """Select appropriate promotional channels"""
        genre = book_info.get("genre", "General")
        
        base_channels = ["Social Media", "Book Bloggers", "Email Marketing"]
        genre_channels = self.knowledge_base["genre_marketing"].get(genre, [])
        
        return base_channels + genre_channels
    
    def _create_launch_timeline(self) -> Dict[str, str]:
        """Create launch timeline"""
        return {
            "Pre-launch (4 weeks)": "Social media teasers, influencer outreach",
            "Launch week": "Major promotional push, book blogger reviews",
            "Post-launch (2 weeks)": "Sustained social media, reader engagement",
            "Ongoing": "Community building, reader feedback integration"
        }
    
    def _allocate_budget(self, channels: List[str]) -> Dict[str, float]:
        """Allocate marketing budget across channels"""
        total_budget = 100.0
        allocations = {}
        
        for channel in channels:
            if "Social Media" in channel:
                allocations[channel] = 30.0
            elif "Influencer" in channel:
                allocations[channel] = 25.0
            elif "Ads" in channel:
                allocations[channel] = 20.0
            else:
                allocations[channel] = 15.0
        
        return allocations

# Test the marketing agent
if __name__ == "__main__":
    agent = MarketingAgent()
    
    test_book = {
        "genre": "Fantasy",
        "tone": "Epic",
        "title": "The Dragon's Call",
        "description": "A young wizard discovers their destiny"
    }
    
    strategy = agent.create_marketing_strategy(test_book)
    print(f"\n🎯 Target Audience: {strategy.target_audience}")
    print(f"📢 Key Messages: {strategy.key_messaging}")
    print(f"📺 Promotional Channels: {strategy.promotional_channels}")
