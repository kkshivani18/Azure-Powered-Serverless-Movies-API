# Azure-Powered-Serverless-Movies-API  

**Overview and Workflow of the Project**

## Overview
The Serverless Movies API is a capstone project that showcases a serverless architecture to provide movie information through various API endpoints. Using cloud-based resources like a NoSQL database, cloud storage, and serverless functions, this project delivers movie data, including details, cover images, and AI-generated summaries.

## Project Structure
This API includes the following serverless functions:

- **GetMovies**: Fetches a list of all movies, including their details and cover image URLs.
- **GetMoviesByYear**: Retrieves a list of movies based on a specified release year.
- **GetMovieSummary**: Provides an AI-generated summary for a specific movie.

## Steps

### 1. Create Your Cloud Infrastructure
- **Set up your SDK**: Use the SDK of your cloud provider (e.g., AWS SDK, Azure SDK, Google Cloud SDK) to configure your infrastructure.  
- **NoSQL Database**: Create a NoSQL database (e.g., Cosmos DB on Azure, DynamoDB on AWS, or Firestore on Google Cloud).  
- **Cloud Storage**: Set up cloud storage (e.g., Azure Blob Storage, Amazon S3, or Google Cloud Storage) for storing movie cover images.  

- **Serverless Functions**: Configure serverless functions for each endpoint:
  - **GetMovies**
  - **GetMoviesByYear**
  - **GetMovieSummary** (For AI summaries)
  

  > **Note**: Check for additional setup steps based on your cloud provider, such as configuring permissions, setting up API Gateway, or obtaining necessary keys.

### 2. Prepare Your Data  
- **Movie Data**: Gather or create a dataset of movies with relevant information, such as title, release year, genre, etc.  
- **Cover Images**: Upload movie cover images to your cloud storage. Ensure each movie has a unique URL for its cover image.

### 3. Create Serverless Functions
Each serverless function is created to handle a specific request for movie information:

- **GetMovies**  
  - **Description**: Retrieves a JSON list of all movies stored in the NoSQL database.  
  - **Response**: Includes details such as title, genre, release year, and a cover image URL for each movie.

- **GetMoviesByYear**  
  - **Description**: Fetches a list of movies released in a specified year.  
  - **Parameters**:  
    - `year` (query parameter): Specifies the release year of the movies.  
  - **Response**: Returns a JSON list of movies that match the specified year.

- **GetMovieSummary**  
  - **Description**: Returns an AI-generated summary for a specified movie.  
  - **Parameters**:  
    - `title` (query parameter): Specifies the title of the movie for which the summary is requested.  
  - **Response**: A summary generated using AI for the requested movie title.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/serverless-movies-api.git
   cd serverless-movies-api

2. Install SDK dependencies based on the cloud provider.  

3.  Deploy Cloud Resources: Use your SDK or cloud console to deploy the NoSQL database, storage, and serverless functions.

## Usage
Once deployed, the API provides the following endpoints:
- GetMovies: GET /movies  
- GetMoviesByYear: GET /movies?year={year}  
- GetMovieSummary: GET /movie-summary?title={title}  
Replace {year} and {title} with the specific year or title for your query.

**-------------------------------------------------------------------------------------------------------------------------------------------------------------**

## Step-by-step guide for building the project

### 1. **Set Up Project Environment**  

  Python: Make sure you have Python 3.8 or 3.9 installed.  
  ```python
     python -m venv ./<your-venv>
  ```
  Local Development: Set up your Python environment locally, installing necessary packages (azure-functions, azure-cosmos, azure-storage-blob).   
  ![Installing packages for 3 SDKs](https://github.com/user-attachments/assets/726cf252-8e19-4ea9-955f-f7d202dd5e84) 

  Azure Functions Core Tools: For local function development.  
   ```bash
    npm install -g azure-functions-core-tools@3 --unsafe-perm true
   ```
### 2. **Create resources on Azure** (storage-account, cosmosdb, function-app)

> **Note**: Before creating any resource in Azure, always create the resource group for the project. It helps in organizing all the resources required for the project. 

   ```bash
   az login
  ```

  You can Azure CLI or Azure portal.  
  
  ##### Create Resource Group:  
  
  ```bash
  az group create --name <ResourceGroupName> --location <Location>
  ```
  ![image](https://github.com/user-attachments/assets/f1c0c9b5-1cf7-4e0f-bafc-b35c4b8524f8)  

  ##### Create Storage account:  
  
  ![moviesstacc](https://github.com/user-attachments/assets/55483a02-5935-44ba-8e02-aed529730257)  

  ##### Azure Function App: Create an Azure Function App in the Azure Portal (or using Azure CLI) to host your serverless functions.  
  
  ![function app](https://github.com/user-attachments/assets/c7779ee0-ffd0-4781-a6ba-05fb24b61df7)  

  ![function app created](https://github.com/user-attachments/assets/cc542856-32e7-43a6-b4b9-336ec3a74fa1)  

  ##### Create Cosmosdb

  ![moviesdb_creation](https://github.com/user-attachments/assets/54d116d2-2917-4cef-8636-e8a1292b1564)  

  ![moviesdb](https://github.com/user-attachments/assets/fdef0a4f-74a4-4c8a-a603-1020984723dc)  

  




 
