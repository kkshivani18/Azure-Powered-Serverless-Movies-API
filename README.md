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

  You can do it through Azure CLI or Azure portal.  
  
  #### Create Resource Group:  
  
  ```bash
  az group create --name <ResourceGroupName> --location <Location>
  ```
  ![image](https://github.com/user-attachments/assets/f1c0c9b5-1cf7-4e0f-bafc-b35c4b8524f8)  

 
  #### Create Storage account:  

  In your Serverless Movies API project, the storage account (specifically, Blob Storage within it) is used to store movie cover images. These image URLs are then saved in    your Cosmos DB and referenced in the API responses, allowing clients to access and display the cover images.  

  - Search for Storage Accounts in Azure portal: In the search bar at the top, type "Storage Accounts" and select it.
  - Click 'Create': Select "Create" to start setting up a new storage account.
  - Choose Subscription and Resource Group: Select the current subscription and the above created resource group.
  - Provide a Storage Account Name: This must be unique across Azure and use only lowercase letters and numbers.
  - Choose Region: Select the region closest to your users for optimized latency.
  - Select Performance and Redundancy: Choose the performance tier (Standard or Premium) and redundancy option.
  - Review and Create: Click "Review + Create" to verify settings, then "Create" to deploy the storage account.

  > Note - Choose the same location for Storage account, CosmosDB account and Functions app. 

  
  ![moviesstacc](https://github.com/user-attachments/assets/55483a02-5935-44ba-8e02-aed529730257)  

 
  #### Azure Function App: Create an Azure Function App in the Azure Portal (or using Azure CLI) to host your serverless functions.  

  - Search for Function App from Azure portal: Type "Function App" in the search bar and select it.
  - Click 'Create': Start the process of creating a new Function App.
  - Select Subscription and Resource Group: Choose the above created resource group. 
  - Enter Function App Name: Provide a globally unique name for the Function App.
  - Choose Runtime Stack: Select the runtime stack (e.g., Python, Node.js) and the version.
  - Select Region: Choose a region where the Function App will be hosted.
  - Choose Hosting Plan: Under "Hosting Plan," select "Consumption (Serverless)" for pay-per-execution billing.
  - Configure Storage: Select the above created storage account where all the images of the movie coverpages is stored. 
  - Review and Create: Review the settings, then click "Create" to deploy the Function App.
  This setup allows your function to scale automatically and minimizes costs, as you’re only billed for the actual execution time.
  
  > While creating function-app, select Consumption plan for this project. In the storage section, select the storage account you created earlier. It is recommended to          create all the resources in the same region to avoid some trouble later. In Monitoring sections, enable Application Insights, select yes.
  
  ![function app](https://github.com/user-attachments/assets/c7779ee0-ffd0-4781-a6ba-05fb24b61df7)  

  ![function app created](https://github.com/user-attachments/assets/cc542856-32e7-43a6-b4b9-336ec3a74fa1)  

  
  #### Create Cosmosdb

  ![moviesdb_creation](https://github.com/user-attachments/assets/54d116d2-2917-4cef-8636-e8a1292b1564)  

  ![cosmosdbacc](https://github.com/user-attachments/assets/9d8e48bb-89be-451b-9ae3-b6acc75e3813)

  ![moviesdb](https://github.com/user-attachments/assets/fdef0a4f-74a4-4c8a-a603-1020984723dc)  

  > **Note**: Store your Cosmos DB connection string and Blob Storage connection string in environment variables for secure access.

 
### 3. Configuring Blob Storage and CosmosDB

  While displaying the serverless function output , we have to include the coverpage URLs of the movies. We have to store the images in blob storage in storage                account to get the URL for CosmosDB.   

  #### Upload Images to Azure Blob Storage  
  
  Upload it from local directory to Container on Storage Account.  
  
  ![image](https://github.com/user-attachments/assets/3e5d0c92-491c-433b-bd7a-78e684c03162)

  #### Using OMDB API for Movies
  Implement API calls to the OMDB API to fetch movie details. Store the relevant data in your Azure Cosmos DB.  

  #### Configure CosmosDB

  After uploading the images on blob, you can access the URLs. You can manually add data to cosmosdb or add via code and deploy the data on CosmosDB. 
  I used code for deployment. You can access my code uploaded in the repository. 

  ![movies_inserted_to_cosmodb](https://github.com/user-attachments/assets/4d81eb02-5541-43f1-960b-e4d439ffdc4a)

  ![movies_added_cosmodb](https://github.com/user-attachments/assets/5fb7a09f-aec1-4d25-8950-886a396fee2e)


### 4. Configuring Function app  

  1. Set Up Local Development Environment

   ```bash
   mkdir MoviesApi

   cd MoviesApi

   func init --python
   ```

  ![func_init](https://github.com/user-attachments/assets/773f980d-8d21-41a1-bc4e-dc2e3b107173)

  2. Ensure, you have already installed required libraries. Else, you can install the Azure SDKs for Function app Cosmos DB and Blob Storage with the below command.
     ```bash
     pip install azure-functions azure-cosmos azure-storage-blob
     ```
     
3. **Create Individual Functions**: For each API endpoint, create an HTTP-triggered function

     ```bash
     func new
     ```
    Choose the HTTP trigger template and name your functions:
     - GetMovies
     - GetMoviesByYear
     - GetMovieSummary

    After running the command 'func new', select the HTTP Trigger, then enter the name of the Function
    ![func_new_create](https://github.com/user-attachments/assets/6aec5317-1811-4100-84e1-a60a15bf5e5d)

    Once, you do the above for all the functions, it means you have created HTTP Trigger for the function.

   > An HTTP trigger in Azure Functions is a type of trigger that allows your serverless function to be invoked via an HTTP request. When you set up an HTTP-triggered           function, it becomes accessible through an endpoint URL, allowing you to interact with it directly over the web using standard HTTP methods like GET, POST, PUT, and         DELETE. This makes it ideal for building RESTful APIs or webhooks.

   Now, implement the function logic for each function. The function_app.py is included in the repository. After appending the function logic to the file. Run the below        command to test the function locally.

   ```bash
   func start
   ```

   ![func_start](https://github.com/user-attachments/assets/3f6e0a08-ec90-47ab-95c6-bbdd0e894e3b)

   The below image shows that once, you access your functions at http://localhost:7071/api/<FunctionName> to confirm they’re correctly recognized as HTTP triggers locally.     The terminal keeps track of the log. 

   ![func_start_testing](https://github.com/user-attachments/assets/5208ec4b-5b4e-4a76-bb62-80bb5bc71bec)

  #### GetMovies

  ![GetMovies](https://github.com/user-attachments/assets/2a650567-6d87-411c-baa2-a133e1b6d3fa)  

  #### GetMoviesByYear

  ![GetMovieByYear](https://github.com/user-attachments/assets/360e5736-0069-4438-bb39-164dffffb0ae)  

  #### GetMovieSummary  

  ![GetMovieSummary](https://github.com/user-attachments/assets/98d8ce63-a31d-41bf-9dcc-0335d7c1ff15)  


  After testing locally, you can now deploy it on the Azure functions-app service with the below command 

  ![deploying_funcson_azure](https://github.com/user-attachments/assets/c5c541e7-4158-4657-b4ea-dde912c53337)

  The below images confirms that the functions are deployed on Azure

  ![deploy_funcs_done](https://github.com/user-attachments/assets/4d45109d-30a6-44a1-9071-fa74064facff)

  ![deploy_func_azure](https://github.com/user-attachments/assets/b495f171-cb05-4c80-8af6-227ef82ee5c3)

  To access your functions via Azure, you have to access your function which will be added at the end. Since, we have set the AuthLevel to Function. 
  
  ![func_key_azure](https://github.com/user-attachments/assets/d752003e-df49-40a2-8be8-02c2b9b58e29)


  ### Testing each function deployed on Azure
  #### GetMovies Function

  ![Screenshot 2024-11-04 155447](https://github.com/user-attachments/assets/618215bb-26c6-45e2-976f-a75a1add4076)

  #### GetMovieByYear

  ![image](https://github.com/user-attachments/assets/15f6cfb0-3c2d-47e8-8dc9-7876ee9ff13d)

  #### GetMovieSummary

  ![image](https://github.com/user-attachments/assets/6e21df2e-59c3-483b-a786-144a20c535c0)
  
  
  Therefore, this completes the API logic for each function in your Serverless Movies API
   
