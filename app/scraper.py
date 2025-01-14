import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from urllib.parse import urljoin  # For handling relative URLs

# Initialize Elasticsearch
es = Elasticsearch(
    "https://my-elasticsearch-project-c7a9cf.es.us-east-1.aws.elastic.cloud:443",
    api_key="NF9yX1lwUUJoM2tOTnpBLUNUa186OVV4N1VrYmJUTENYb0R6b1hDdEFpUQ=="
)

# Function to scrape the documentation pages
def scrape_docs(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)

    docs = []
    for link in links:
        href = link['href']
        
        # Skip invalid URLs like '#' or '#content'
        if href.startswith('#') or href == '/':
            continue

        # Convert relative URLs to absolute URLs
        href = urljoin(base_url, href)
        
        try:
            doc_resp = requests.get(href)
            doc_soup = BeautifulSoup(doc_resp.content, "html.parser")
            text = doc_soup.get_text()
            docs.append({"url": href, "content": text})
        except Exception as e:
            print(f"Failed to scrape {href}: {e}")
    
    return docs

# Function to index the scraped documentation into Elasticsearch
def index_docs(index_name, docs):
    for i, doc in enumerate(docs):
        try:
            es.index(index=index_name, id=i, body=doc)
            print(f"Successfully indexed document {i} in {index_name}")
        except Exception as e:
            print(f"Error indexing document {i}: {e}")


# Scrape and index Segment documentation
segment_docs = scrape_docs("https://segment.com/docs/?ref=nav")
index_docs("segment_docs", segment_docs)

# Scrape and index mParticle documentation
mparticle_docs = scrape_docs("https://docs.mparticle.com")
index_docs("mparticle_docs", mparticle_docs)

# Scrape and index Lytics documentation
lytics_docs = scrape_docs("https://docs.lytics.com")
index_docs("lytics_docs", lytics_docs)

# Scrape and index Zeotap documentation
zeotap_docs = scrape_docs("https://docs.zeotap.com/home/en-us/")
index_docs("zeotap_docs", zeotap_docs)
