import os
from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceEndpoint

# Loading environment variables
load_dotenv(find_dotenv())
key = os.environ["HF_KEY"]

def llm_html_parsing(filepath):

    try:
        # Loading LLM
        llm = HuggingFaceEndpoint(
            repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1",
            huggingfacehub_api_token = key
        )

        # Assigning prompt
        template = """
        <|sys|>
        You are an expert in Web Scraping of e-commerce website, so you are capable to find the information of product(s) in HTML and label them accordingly. 
        Please return the final result in JSON following the format below:
        product: Name of the product
        product_tag: CSS selectors or Xpaths associated with product
        price: Price of the product
        price_tag: CSS selectors or Xpaths associated with price
        desc: Description about the product
        desc_tag: CSS selectors or Xpaths associated with description of product
        img: Images associated with the product
        img_tag: CSS selectors or Xpaths associated with image
        </sys>
        <|user|>
        HTML: {html}
        </user>
        <|sys|>
        JSON:
        </sys>        
        """
        prompt = PromptTemplate.from_template(template)

        # Assigning conversation chain
        conv = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True
        )

        # Reading HTML file
        with open(filepath, 'r', encoding='utf-8') as file:
            html = file.read()

        # Response from LLM
        llm_response = conv(
            {"html": f"{html}"}
        )

        return llm_response['text']

    except Exception as e:
        print(f"Error occurred while parsing the HTML content: {e}")