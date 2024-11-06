import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Cosmos DB connection details
url = os.getenv('COSMOS_DB_URL')
key = os.getenv('COSMOS_DB_KEY')  
database_name = "MoviesDB"
container_name = "Movies"

# Initialize the Cosmos client
client = CosmosClient(url, credential=key)

# Create or get the database
database = client.get_database_client(database_name)

# Create or get the container
container = database.get_container_client(container_name)

# Movie data to insert
movies = [
    {
        "id": "1",
        "title": "Inception",
        "releaseYear": "2010",
        "genre": "Science Fiction, Action",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (1).png"
    },
    {
        "id": "2",
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (2).png"
    },
    {
        "id": "3",
        "title": "Interstellar",
        "releaseYear": "2014",
        "genre": "Adventure, Drama, Sci-Fi",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (3).png"
    },
    {
        "id": "4",
        "title": "Parasite",
        "releaseYear": "2019",
        "genre": "Bong Joon-ho, Drama, Thriller",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (4).png"
    },
    {
        "id": "5",
        "title": "Forrest Gump",
        "releaseYear": "1994",
        "genre": "Drama, Romance",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (5).png"
    },
    {
        "id": "6",
        "title": "The Matrix",
        "releaseYear": "1999",
        "genre": "Action, Sci-Fi",
        "coverUrl": "https://moviesapistracc.blob.core.windows.net/movie-coverpages/1 (6).png"
    }
]

# Insert each movie into the container
for movie in movies:
    container.upsert_item(movie)
    print(f"Movie: {movie['title']}")

print("All movies have been inserted.")