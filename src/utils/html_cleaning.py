import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
file_path = os.environ['filepath']

def cleaning_HTML(html_input: str):
    try:
        # Preprocessing the HTML block
        soup = BeautifulSoup(html_input, "html.parser")

        # Reducing HUGE TOKEN cost
        # Removing <head>, <script> and <style> tags and their content
        for tag in soup(["head", "script", "style"]):
            tag.extract()

        # Prettify the modified HTML
        prettified_html = soup.prettify()

        # Saving the formatted HTML in a temporary file
        filename = "temp.html"
        filepath = os.path.join(file_path, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(prettified_html)

        return filepath
    
    except Exception as e:
        print(f"Error occurred while parsing HTML content: {e}")
