import os
from dotenv import load_dotenv
load_dotenv()

from llama_index import VectorStoreIndex, SimpleDirectoryReader


documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("""
I am writing an E2E test in Python using Playwright. 
Write the Python code to open the homepage, click the "Accessibility" link, 
click on the Telecommunications Products link, and verify the webpage has
moved to the correct page.
""")
print(response)


# from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch()
#     context = browser.new_context()
#     page = context.new_page()

#     # Open the homepage
#     page.goto("https://government.github.com/")

#     # Click the "Accessibility" link
#     page.click('a[href="/accessibility/"]')

#     # Click on the "Telecommunications Products" link
#     page.click('a[href="/accessibility/telecommunications-products/"]')

#     # Verify the webpage has moved to the correct page
#     assert page.url == "https://government.github.com/accessibility/telecommunications-products/"

#     # Close the browser
#     context.close()
#     browser.close()
