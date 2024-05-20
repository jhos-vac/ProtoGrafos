import neo4j


def add_entity(self, entity_type, data):
    query = f"""
    CREATE (n:{entity_type})
    SET n = $props
    RETURN ID(n)
    """
    with self.driver.session() as session:
        result = session.write_transaction(self._execute_write, query, props=data)
        return result[0]["ID(n)"]

def get_entity(self, entity_type, entity_id):
    query = f"""
    MATCH (n:{entity_type}) WHERE ID(n) = $id
    RETURN n
    """
    with self.driver.session() as session:
        result = session.read_transaction(self._execute_read, query, id=entity_id)
        return result[0]["n"] if result else None

def get_all_entities(self, entity_type):
    query = f"""
    MATCH (n:{entity_type})
    RETURN n
    """
    with self.driver.session() as session:
        results = session.read_transaction(self._execute_read, query)
        return [record["n"] for record in results]

def update_entity(self, entity_type, entity_id, data):
    query = f"""
    MATCH (n:{entity_type}) WHERE ID(n) = $id
    SET n = $props
    RETURN n
    """
    with self.driver.session() as session:
        result = session.write_transaction(
            self._execute_write, query, id=entity_id, props=data
        )
        return result[0]["n"] if result else None

def delete_entity(self, entity_type, entity_id):
    query = f"""
    MATCH (n:{entity_type}) WHERE ID(n) = $id
    DETACH DELETE n
    """
    with self.driver.session() as session:
        session.write_transaction(self._execute_write, query, id=entity_id)
        return True

def create_relationship(self, entity_type1, entity_id1, relationship_type, entity_type2, entity_id2, data=None):
    query = f"""
    MATCH (n1:{entity_type1}) WHERE ID(n1) = $id1
    MATCH (n2:{entity_type2}) WHERE ID(n2) = $id2
    CREATE (n1)-[:{relationship_type}]{(data or {})}->(n2)
    """
    with self.driver.session() as session:
        session.write_transaction(self._execute_write, query, id1=entity_id1, id2=entity_id2, data=data)
        return True

def get_relationship(self, entity_type1, entity_id1, relationship_type, entity_type2, entity_id2):
    query = f"""
    MATCH (n1:{entity_type1}) WHERE ID(n1) = $id1
    MATCH (n2:{entity_type2}) WHERE ID(n2) = $id2
    MATCH (n1)-[:{relationship_type}]->(n2)
    RETURN n1, n2
    """
    with self.driver.session() as session:
        result = session.read_transaction(self)
