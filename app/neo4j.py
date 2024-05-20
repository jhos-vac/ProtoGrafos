import os
import neo4j

NEO4J_HOST = os.environ.get("NEO4J_HOST", "127.0.0.1")
NEO4J_PORT = os.environ.get("NEO4J_PORT", 7687)
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "password")

def __init__(self):
    uri = f"bolt://{NEO4J_HOST}:{NEO4J_PORT}"
    self.driver = GraphDatabase.driver(uri, auth=(NEO4J_USER, NEO4J_PASSWORD))

def close(self):
    self.driver.close()