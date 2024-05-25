import os
from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint

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
            verbose=False
        )

        # Reading HTML file
        with open(filepath, 'r', encoding='utf-8') as file:
            html = file.read()

        # Response from LLM
        llm_response = conv(
            {"html": f"{html}"}
        )

        # Strictly JSON 
        template2 = """
        <|sys|>
        Strictly parse the given text in JSON format.
        </sys>
        <|user|>
        String: {response1}
        </user>
        <|sys|>
        JSON: 
        </sys>
        """
        prompt2 = PromptTemplate.from_template(template2)

        conv2 = LLMChain(
            llm=llm,
            prompt=prompt2,
            verbose=True
        )

        fin_response = conv2(
            {"response1": f"{llm_response['text']}"}
        )
    
        out_response = fin_response['text']
        
        return out_response

    except Exception as e:
        print(f"Error occurred while parsing the HTML content: {e}")