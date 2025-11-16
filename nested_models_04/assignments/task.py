from pydantic import BaseModel
from typing import List, Optional
# import json

# TODO: Create Course model
# Each course has modules
# Each module has lessons

class Lesson(BaseModel):
    id: int
    title: str
    content: str

class Module(BaseModel):
    id: int
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    modules: List[Module]

# Example instantiation
lesson1 = Lesson(
    id=1,
    title="Introduction to Python",
    content="This lesson covers the basics of Python."
)
lesson2 = Lesson(
    id=2,
    title="Advanced Python",
    content="This lesson covers advanced topics in Python."
)

module = Module(
    id=1,
    title="Python Programming",
    lessons=[lesson1, lesson2]
)

course = Course(
    id=1,
    name="Complete Python Course",
    description="A comprehensive course on Python programming.",
    modules=[module]
)
# The above code defines a Course model with nested Module and Lesson models.

# print(course.model_dump_json(indent=4))
print(course) 
