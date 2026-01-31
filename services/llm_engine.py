from google import genai
from services.search_engine import get_live_products
from core.config import GOOGLE_API_KEY

class CustomEcommerceAgent:
    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
    
        self.model_name = "gemini-3-flash-preview" 

    def run(self, query):
        """
        Returns: 
        1. recommendation_text (str)
        2. main_raw_data (json/str)
        3. accessory_list (list)
        """
        
        # 1. Prompt with Guardrails
        # We perform the check INSIDE the prompt instructions
        prompt = f"""
        You are a specialized E-Commerce Shopping Assistant.
        
        USER REQUEST: "{query}"
        
        STRICT OFF-TOPIC RULE:
        If the user request is NOT related to buying products, comparing prices, or looking for shopping advice (e.g., "Who is the president?", "Write code for me", "How to cook"), you must REFUSE.
        
        If Refusing:
        - Output exactly: "I am designed to help with shopping and product comparisons only. Please ask me about a product!"
        - Do NOT output the ---ACCESSORIES--- section.
        
        If Shopping Related:
        1. I have provided market data below. Analyze it and give a recommendation.
        2. Identify exactly 2 related accessories.
        
        MARKET DATA: 
        {get_live_products(query)} 
        
        STRICT OUTPUT FORMAT (For Shopping Queries Only):
        [Your Recommendation Text]
        ---ACCESSORIES---
        [Accessory 1], [Accessory 2]
        """

        # 2. Call Gemini
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            full_text = response.text
            
            # 3. Parsing Logic
            # Case A: Shopping Query (Has accessories)
            if "---ACCESSORIES---" in full_text:
                parts = full_text.split("---ACCESSORIES---")
                recommendation = parts[0].strip()
                accessories_text = parts[1].strip()
                accessory_list = [item.strip() for item in accessories_text.split(",")]
               
                # Let's do it efficiently:
                raw_data = get_live_products(query) 

            # Case B: Off-Topic (No accessories section)
            else:
                recommendation = full_text # Contains the "I am designed..." refusal
                raw_data = None # No cards to show
                accessory_list = [] # No accessories to show

        except Exception as e:
            recommendation = f"Gemini Error: {str(e)}"
            raw_data = None
            accessory_list = []
        
        return recommendation, raw_data, accessory_list

def get_ecommerce_agent():
    return CustomEcommerceAgent()