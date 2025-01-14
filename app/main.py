from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.scraper import es

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/query/")
async def query(request: Request):
    data = await request.json()
    user_query = data.get("query")
    cdp = data.get("cdp").lower()

    index_map = {
        "segment": "segment_docs",
        "mparticle": "mparticle_docs",
        "lytics": "lytics_docs",
        "zeotap": "zeotap_docs"
    }
    index_name = index_map.get(cdp)
    if not index_name:
        return {
            "response": "I'm specialized in helping with Segment, mParticle, Lytics, and Zeotap. Please specify one of these."
        }

    query_body = {
        "query": {
            "match": {
                "content": user_query
            }
        }
    }
    response = es.search(index=index_name, body=query_body)
    if response['hits']['hits']:
        top_match = response['hits']['hits'][0]['_source']
        content_preview = " ".join(
            top_match["content"].strip().split()[:50]
        ) + "..."  # Truncate to 50 words

        return {
            "response": {
                "title": "Relevant Documentation",
                "snippet": content_preview,
                "link": top_match["url"]
            }
        }
    else:
        return {"response": "No relevant information was found. Try rephrasing your query or specifying more details."}
