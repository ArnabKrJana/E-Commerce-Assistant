# 🛍️ ShopSmart AI – AI-Powered E‑Commerce Assistant

> **An intelligent shopping assistant that compares live prices, recommends the best deal, and suggests essential accessories using AI.**

---

## 🚀 Project Overview

**ShopSmart AI** is an AI-driven e‑commerce assistant built with **Streamlit**, **LangChain**, **Google Gemini**, and **SerpAPI**. It helps users:

* 🔍 Compare prices across multiple platforms (Amazon, Flipkart, Croma, etc.)
* 🤖 Get AI‑generated buying recommendations
* 🎒 Discover essential accessories related to the product
* ⚡ Save time and make informed purchase decisions

---

## 🎥 Live Demo

[![Streamlit Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://e-commerce-assistant-nohwquggh8fgjmbe7pm2uj.streamlit.app/)

---

## 🧠 How It Works

1. User enters a product query (e.g., *Gaming Laptop under 60k*)
2. Live market data is fetched using **SerpAPI (Google Shopping)**
3. Raw data is analyzed by **Google Gemini (LLM)**
4. AI returns:

   * Best buying recommendation
   * Exactly **2 related accessories**
5. App fetches live data again for accessories
6. Results are displayed using reusable UI components

---

## 🏗️ Project Architecture

```text
E-Commerce-Assistant/
│
├── main.py                     # Streamlit entry point
│
├── core/
│   └── config.py               # API keys & environment config
│
├── services/
│   ├── search_engine.py        # SerpAPI / Mock data logic
│   └── llm_engine.py           # Gemini AI agent logic
│
├── ui/
│   └── product_card.py         # Reusable product UI component
│
├── requirements.txt            # Project dependencies
└── .env                        # Environment variables (not committed)
```

---

## 🧩 Key Features

* ✅ Live price comparison
* ✅ AI‑powered recommendations
* ✅ Controlled LLM output parsing
* ✅ Accessory suggestions with validation
* ✅ Modular & scalable architecture
* ✅ Mock data mode to save API credits

---

## 🛠️ Tech Stack

* **Frontend / UI:** Streamlit
* **AI / LLM:** Google Gemini (via LangChain)
* **Search Engine:** SerpAPI (Google Shopping)
* **Backend Logic:** Python
* **Config Management:** python‑dotenv

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key
SERPAPI_API_KEY=your_serpapi_key
LANGCHAIN_API_KEY=your_langchain_key
```

---

## ▶️ Running the Project Locally

```bash
# Clone the repository
git clone https://github.com/ArnabKrJana/E-Commerce-Assistant.git
cd E-Commerce-Assistant

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
```

---

## 🧪 Development Tip (Mock Mode)

To avoid consuming API credits during development, enable mock data:

```python
USE_MOCK_DATA = True
```

This returns fake shopping results while keeping the UI fully functional.

---

## 📌 Design Decisions

* Modular folder structure for maintainability
* Strict LLM output format to avoid hallucination issues
* Fail‑fast configuration checks
* Reusable UI components
* Graceful error handling for external APIs

---

## 📈 Future Improvements

* User accounts & personalization
* Caching with Redis
* Backend using FastAPI
* Review‑based ranking
* Price history tracking

---

## 👨‍💻 Author

**Arnab Kumar Jana**
GitHub: [https://github.com/ArnabKrJana](https://github.com/ArnabKrJana)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!
