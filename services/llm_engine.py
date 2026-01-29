from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from services.search_engine import get_live_products
from core.config import GOOGLE_API_KEY

class CustomEcommerceAgent:
    def __init__(self):
        # Using gemini-3-flash-preview (latest, Long Context)
        self.chat_model = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.1
        )

    def run(self, query):
        """
        Executes the Search -> Analyze -> Answer loop.
        """
        # Step 1: Perform the Search
        try:
            raw_data = get_live_products(query)
        except Exception as e:
            raw_data = f"Error fetching data: {str(e)}"

        # Step 2: Define Formatting Rules (Optimized for Gemini)
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    You are an expert Shopping Assistant.
                    
                    STRICT FORMATTING RULES:
                    1. Start with a clear recommendation (e.g., "The best option is...").
                    2. Use **Bold** for product names and prices.
                    3. Use Bullet Points (•) to list pros/cons.
                    4. Do NOT write long paragraphs. Keep it readable.
                    5. Compare the options based on Price and Value.
                    """
                ),
                (
                    "user", 
                    """
                    SEARCH QUERY: "{query}"

                    LIVE MARKET DATA FOUND:
                    {product_data}
                    
                    Based on this data, which product should I buy? Compare them clearly.
                    """
                )
            ]
        )

        # Step 3: Run the Chain
        try:
            chain = prompt | self.chat_model | StrOutputParser()
            
            response = chain.invoke({
                "query": query,
                "product_data": raw_data
            })
        except Exception as e:
            response = f"Gemini Error: {str(e)}"
        
        # Return both the AI text AND the raw data (so main.py can show cards)
        return response, raw_data

def get_ecommerce_agent():
    return CustomEcommerceAgent()