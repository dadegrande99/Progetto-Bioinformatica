# Alignment-Free Sequence to Graph

This project, named "Alignment-Free Sequence to Graph", is a Python-based application that focuses on converting alignment-free sequences into a graph representation. The primary use case of this project is in the field of bioinformatics, where sequences of DNA, RNA, or proteins are often represented as graphs for further analysis.

The project utilizes the Neo4j graph database for storing and managing the graph data. Neo4j is a highly scalable, native graph database that excels at managing and querying highly connected data. It is a popular choice for projects that require efficient handling of complex relationships between data points.
This project is about creating an alignment-free

## Table of Contents

- [Alignment-Free Sequence to Graph](#alignment-free-sequence-to-graph)
  - [Table of Contents](#table-of-contents)
  - [Database](#database)
  - [Feature](#feature)
    - [Graph Database Manager](#graph-database-manager)
    - [Alignment-Free Sequence](#alignment-free-sequence)
    - [Interface](#interface)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Usage of Neo4J with Docker](#usage-of-neo4j-with-docker)
  - [Contributors](#contributors)
  - [License](#license)

## Database

The database management system (DBMS) used in this project is Neo4j. Neo4j is a highly scalable, native graph database that excels at managing and querying highly connected data. It is a popular choice for projects that require efficient handling of complex relationships between data points.

## Feature

The project is structured around two main classes: `DBManager` and `AlignmentFreeGraph`.

### Graph Database Manager

The `DBManager` class is responsible for managing the connection and queries to the Neo4j database. It provides methods for connecting to the database, checking the connection, uploading data from a JSON file, executing queries, and more. This class is essential for the interaction between the Python application and the Neo4j database.

### Alignment-Free Sequence

The `AlignmentFreeGraph` class extends the `DBManager` class and implements the logic for converting an alignment-free sequence to a graph. It works with Direct Acyclic Graphs (DAGs) and uses a k-mer based approach, where k is a parameter that can be set by the user. This class is the core of the project, where the conversion of sequences to graph representations happens.

### Interface

The interface of the "Alignment-Free Sequence to Graph" application is built using the `customtkinter` and `tkinter` libraries in Python. It provides a graphical user interface (GUI) for users to interact with the application.

The main window of the interface is titled "Alignment-Free Sequence to Graph". It contains a button labeled "New Connection" which, when clicked, opens a new window for creating a connection to the Neo4j database. This new window provides fields for entering the location, database name, username, and password for the database connection. It also provides an option to connect using a configuration file.

**Graph and hashtable** : The interface also provides a frame for displaying the graph representation of the alignment-free sequence. The graph is displayed using the `matplotlib` library. There are buttons for refreshing the graph, deleting all nodes, and adding nodes from a JSON file.

There is also a section for setting the value of `k` for the k-mer based approach used in the conversion of sequences to graph representations. The value of `k` can be changed by entering a new value in the provided entry field and pressing the "Enter" key.

The hashtable in the "Alignment-Free Sequence to Graph" application is used to store the k-mers and their corresponding nodes in the graph. The hashtable is implemented as a Python dictionary, where the keys are the k-mers and the values are the nodes in the graph.

The hashtable is displayed in the interface in a treeview, which is a widget that displays a hierarchical collection of items. Each item in the treeview corresponds to a key-value pair in the hashtable. The keys and values are displayed in separate columns, labeled "Key" and "Value", respectively.

The hashtable is updated whenever the value of `k` is changed, a sequence is added from a JSON file, or all nodes are deleted from the graph. The `show_hashtable` function is responsible for updating the display of the hashtable in the treeview. This function first destroys any existing widgets in the hashtable frame, then creates a new treeview and populates it with the current contents of the hashtable.

The `show_hashtable` function is called in the `change_k`, `add_from_json`, and `delete_all_nodes` functions, which handle changing the value of `k`, adding nodes from a JSON file, and deleting all nodes, respectively. This ensures that the hashtable displayed in the interface is always up-to-date with the current state of the graph.

**Sequence search** : Another section of the interface provides an entry field for entering a sequence to search for in the graph. The result of the search is displayed in the same section.

Finally, there is an "Exit" button at the bottom of the interface which closes the application when clicked.

## Installation

To install the project, clone the repository and install the required Python packages.

```bash
git clone https://github.com/dadegrande99/alignment-free-sequence-to-graph.git
cd alignment-free-sequence-to-graph
pip install -r requirements.txt
```

The installation of Neo4j for the "Alignment-Free Sequence to Graph" project can be done in two ways:

1. Direct Download: You can directly download Neo4j from the official website. Here is the [link](https://neo4j.com/download-center/#community) to the download center. After downloading, follow the instructions provided by Neo4j to install it on your system.

2. Docker Image: If you prefer using Docker, you can pull the Neo4j image from Docker Hub and run it as a container. Here is the command to pull the image:

```bash
docker pull neo4j
```

After pulling the image, you can run the container with the following command:

```bash
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j
```

In both cases, ensure that the Neo4j server is running and accessible at the specified location before trying to connect to it from the application.

Please note that the exact commands and steps might vary depending on your operating system and setup. Always refer to the official documentation for the most accurate and up-to-date information.

## Usage

To use the project, you create an instance of the `DBManager` class with the necessary parameters for connecting to your Neo4j database.

```python
from dbmanager import DBManager

db_manager = DBManager(location='your_database_location', db_name='your_database_name', username='your_username', password='your_password')

# otherwise
db_manager = DBManager(configuration='your_secret_credentials.json')
```

Or, you can utilize the functionalities of Alignment-Free Sequence to Graph with an instance of the `AlignmentFreeGraph` class in this way

```python
from dbmanager import DBManager
from alignmentfreegraph import AlignmentFreeGraph

alignment_free_graph = AlignmentFreeGraph(location='your_database_location', db_name='your_database_name', username='your_username', password='your_password', k=3)

# otherwise
alignment_free_graph = AlignmentFreeGraph(configuration='your_secret_credentials.json', k=3)
```

To use the interface, run the `interface.py` file.

```bash
python interface.py
```

You can update the `README.md` file with the actual usage of Docker as follows:

### Usage of Neo4J with Docker

Docker is a platform that allows you to automate the deployment, scaling, and management of applications using containerization. In this project, we provide a Dockerfile and a docker-compose.yml file that you can use to build a Docker image of the application and run it as a Docker container.

- *There are some problems with running the interface, you should run the interface without docker*

Here are the steps to use this project with Docker:

1. **Start the Neo4j Docker container**

   You can start the Neo4j Docker container using the docker-compose.yml file provided in the project. Navigate to the project directory and run the following command:

   ```bash
   docker-compose up
   ```

   This command starts the Neo4j service defined in the `docker-compose.yml` file. The Neo4j server will be accessible at `localhost:7474` and `localhost:7687`.

2. **Connect to the Neo4j Docker container**

   After starting the Neo4j Docker container, you can connect to it from the application. Create an instance of the `DBManager` or `AlignmentFreeGraph` class with the necessary parameters for connecting to your Neo4j database. The location should be `bolt://localhost:7687`, and the username and password should be as defined in the `docker-compose.yml` file.

   ```python
   from dbmanager import DBManager

   db_manager = DBManager(location='bolt://localhost:7687', db_name='neo4j', username='neo4j', password='testtest1')
   ```

   Or, you can utilize the functionalities of Alignment-Free Sequence to Graph with an instance of the `AlignmentFreeGraph` class in this way

   ```python
   from dbmanager import DBManager
   from alignmentfreegraph import AlignmentFreeGraph

   alignment_free_graph = AlignmentFreeGraph(location='bolt://localhost:7687', db_name='neo4j', username='neo4j', password='testtest1', k=3)
   ```

   To use the interface, run the `interface.py` file.

   ```bash
   python interface.py
   ```

Please note that you need to have Docker and Docker Compose installed on your system to use these features. You can install Docker from the [official website](https://docs.docker.com/get-docker/) and Docker Compose from the [official documentation](https://docs.docker.com/compose/install/).

This section provides a brief introduction to Docker and Docker Compose, and explains how to start a Neo4j Docker container, connect to it from the application, and use the application's interface.

## Contributors

- [Davide Grandesso](mailto:d.grandesso@campus.unimib.it)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) - see the [LICENSE](LICENSE) file for details.
