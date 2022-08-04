from neomodel import StructuredNode, StringProperty, ZeroOrMore, RelationshipTo
from diagram_chasing_games.settings import (MAX_NAME_LENGTH,)

class Namespace(StructuredNode):    
    identifier = StringProperty(max_length=MAX_NAME_LENGTH, required=True)
    contains = RelationshipTo('Model', 'CONTAINS', cardinality=ZeroOrMore)
    
    @staticmethod
    def create_namespace(identifier:str):
        if not identifier.isidentifier() or not identifier.replace('-', '_').isidentifier():
            raise ValueError(f'"{identifier}" is not a valid namespace identifier.')        
        return Namespace(identifier=identifier).save()
        
        
            
        
    
    