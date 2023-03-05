from pydantic import BaseModel

class MySchema(BaseModel):
    """schema class
    
    """
    name: str
    description: str





class Worker():
    def __init__(self, schema: MySchema):
        self.name = schema.name
        self.description = schema.description
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


def get_schema():
    schema = MySchema(name="or", description="developer")
    return schema


def get_worker(schema: MySchema):
    worker = Worker(schema)
    return worker

schema = get_schema()
worker = get_worker(schema)

print(worker.get_name())
print(worker.get_description())

