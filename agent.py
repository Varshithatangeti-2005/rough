#Example for tool creation,tool description,tool calling

# from google.adk.agents import Agent
# from datetime import datetime


# def get_time():--tool creation
#     """Returns the current system time."""
#     return str(datetime.now())


# root_agent = Agent(
#     model="gemini-2.0-flash",
#     name="root_agent",
#     description="Helpful assistant",---tool description
#     instruction="""
#     You are a helpful assistant.
#     If user asks about current time, ALWAYS use get_time tool.
#     """,
#     tools=[get_time] -- tool calling
# )


#Chunking practice
# from google.adk.agents import Agent
# text=''' Python is a programming language.
# It is easy to learn.
# Machine learning uses python.
# AI applications are growing rapidly.
# '''
# #Split into words
# words=text.split()

# #Chunk size
# chunk_size=5

# chunks=[]
# for i in range(0,len(words),chunk_size):
#     chunk=" ".join(words[i:i + chunk_size])
#     chunks.append(chunk)
    
# #print chunks
# for index, chunk in enumerate(chunks, start=1):
#     print(f"Chunk {index}:")
#     print(chunk)
#     print()


#RAG FLOW EXAMPLE
document = """
Python is a programming language.

Machine Learning uses data to train models.

Artificial Intelligence helps machines make decisions.
"""

# Step 1: Chunking
chunks = document.strip().split("\n\n")

# User Question
query = "What uses data to train models?"

# Step 2: Simple Retrieval
for chunk in chunks:
    if "train models" in chunk:
        print("Retrieved Chunk:")
        print(chunk)