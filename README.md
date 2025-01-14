# CDP Documentation Chatbot

A chatbot application that allows users to query documentation for various Customer Data Platforms (CDPs), including Segment, mParticle, Lytics, and Zeotap. The system scrapes relevant documentation from each platform's website and indexes it in Elasticsearch for fast querying. Users can interact with the chatbot via a simple interface to get quick answers from the documentation.

## Live Website

You can access the live chatbot at:  
[https://zeotap-chatbot-project.onrender.com](https://zeotap-chatbot-project.onrender.com)

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Frontend Structure](#frontend-structure)
- [Backend Structure](#backend-structure)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Features

- Query documentation for Segment, mParticle, Lytics, and Zeotap.
- Returns relevant documentation snippets with links to the full documentation.
- Chatbot interface with a simple form to enter queries.
- Seamless interaction with Elasticsearch for fast querying.
- Static files served for a responsive UI.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: FastAPI (Python)
- **Search Engine**: Elasticsearch (Hosted on Elastic Cloud)
- **Scraping**: BeautifulSoup (for scraping documentation)
- **Hosting**: Render (for both frontend and backend deployment)
- **CORS**: To enable cross-origin requests from the frontend to the backend

Usage

Open the live website at https://zeotap-chatbot-project.onrender.com.
Enter your query in the input field. For example:
"How to create a user profile in mParticle?"
Select the desired CDP (Segment, mParticle, Lytics, or Zeotap).
Click "Submit" to get the response, which will include a relevant snippet from the documentation and a link to the full documentation page.


