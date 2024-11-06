import azure.functions as func
from azure.cosmos import CosmosClient
import json
import logging
import os
import requests
import google.generativeai as genai

# credentials
COSMOSDB_URI = os.getenv('COSMOS_DB_URL')
COSMOSDB_KEY = os.getenv('COSMOS_DB_KEY')
DATABASE_NAME = "MoviesDB"
CONTAINER_NAME = "Movies"

# Initialize Cosmos DB client
cosmos_client = CosmosClient(COSMOSDB_URI, COSMOSDB_KEY)
database = cosmos_client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Configure the Gemini API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

app = func.FunctionApp()

# @app.route(route="GetMovies", auth_level=func.AuthLevel.FUNCTION)
# def GetMovies(req: func.HttpRequest) -> func.HttpResponse:
    
# @app.route(route="GetMoviesByYear", auth_level=func.AuthLevel.FUNCTION)
# def GetMoviesByYear(req: func.HttpRequest) -> func.HttpResponse:
    

# @app.route(route="GetMovieSummary", auth_level=func.AuthLevel.FUNCTION)
# def GetMovieSummary(req: func.HttpRequest) -> func.HttpResponse:
    



@app.route(route="GetTheMovies", auth_level=func.AuthLevel.FUNCTION)
def GetTheMovies(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing GetMovies request.') 

    try:
        # Query all movies in the Cosmos DB container
        movies = list(container.read_all_items())
        # Format movies data with title, releaseYear, genre, coverUrl
        movies_data = [
            {
                "title": movie["title"],
                "releaseYear": movie.get("releaseYear"),
                "genre": movie.get("genre"),
                "coverUrl": movie.get("coverUrl")
            } for movie in movies
        ]
        
        # JSON response with all movies
        return func.HttpResponse(
            json.dumps(movies_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error fetching movies: {e}")
        return func.HttpResponse(
            "Error fetching movies from the database.",
            status_code=500
        )


@app.route(route="GetTheMovieByYear", auth_level=func.AuthLevel.FUNCTION)
def GetTheMovieByYear(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing GetMoviesByYear request.')
    year = req.params.get('year')
    if not year:
        return func.HttpResponse(
            "Please provide a year as a query parameter.",
            status_code=400
        )

    try:
        query = "SELECT * FROM c WHERE c.releaseYear = @year"
        movies = list(container.query_items(
            query=query,
            parameters=[{"name": "@year", "value": year}],
            enable_cross_partition_query=True
        ))
        movies_data = [{"title": movie["title"], "releaseYear": movie["releaseYear"], "genre": movie["genre"], "coverUrl": movie["coverUrl"]} for movie in movies]
        return func.HttpResponse(
            json.dumps(movies_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error fetching movies by year: {e}")
        return func.HttpResponse(
            "Error fetching movies by year from the database.",
            status_code=500
        )

@app.route(route="GetTheMovieSummary", auth_level=func.AuthLevel.FUNCTION)
def GetTheMovieSummary(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing GetMovieSummary request.')
    title = req.params.get('title')
    if not title:
        return func.HttpResponse(
            "Please provide a movie title as a query parameter.",
            status_code=400
        )

    try:
        # Query the Cosmos DB for the specified movie title
        query = "SELECT * FROM c WHERE c.title = @title"
        movie = list(container.query_items(
            query=query,
            parameters=[{"name": "@title", "value": title}],
            enable_cross_partition_query=True
        ))

        # Check if the movie exists
        if not movie:
            return func.HttpResponse(
                f"No movie found with the title '{title}'.",
                status_code=404
            )

        # Extract movie details
        movie = movie[0]  # Assuming the title is unique
        release_year = movie.get("releaseYear")
        genre = movie.get("genre")
        cover_url = movie.get("coverUrl")

        # GenerativeModel instance for the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Prompt for the movie summary
        prompt = f"Provide a summary for the movie titled '{title}'."

        # content generation
        response = model.generate_content(prompt)

        # summary from the response and formatted summary
        summary = response.text.strip()
        summary = summary.replace("\\n", "").replace("\n\n", "").replace('\"', "").replace("\\", "")

        data = {
            "title": title,
            "releaseYear": release_year,
            "genre": genre,
            "coverUrl": cover_url,
            "summary": summary
        }

        return func.HttpResponse(
            json.dumps(data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return func.HttpResponse(
            "Error generating movie summary.",
            status_code=500
        )
    