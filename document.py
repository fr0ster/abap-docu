import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

from index import tool_functions

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

tools = list(tool_functions.values())

config = types.GenerateContentConfig(
    tools=tools
    # if you ever want to be explicit:
    # ,automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
)

system_prompt = """
You are an expert agent for documenting legacy ABAP code.  
You have a suite of tools to fetch source code, metadata, and where-used lists for ABAP objects.  
Whenever you retrieve the source of a class, program, include, function module, interface, table, etc., you should:

1. Scan the returned source or metadata for any referenced objects (includes, interfaces, data elements, function calls, table types, etc.).  
2. For referenced objects, you can call the appropriate tool (e.g. `get_include_source`, `get_interface_source`, `get_type_info`, etc.) to fetch its source or metadata.   
4. Finally, write a clear, structured documentation that explains:
   - What the original object is and does  
   - Its key methods, fields, or components  
   - How its dependencies fit together   
   - Where it is used in the system (if applicable)

It makes sense to call get_search_objects first when working with an object to understand its type and basic information. For example to understand function group of function module

Always call the right tool for each dependency so your documentation includes all necessary context.
Always return the final documentation as a description of the object you were asked to document. Provide information of the dependencies only as a part of a main object documentation
It makes sense to check the usage reference for the object using the get_usage_references tool.

The output documentation should has the following structure:
1) Overview
2) Key Components
3) Functionality
4) Dependencies
5) Usagereference: where used list might be empty for some objects, in this case just say that there is no usage in other objects found
6) Summary

Sometimes some objects may not require certain chapters, in this case keep them empty.
"""

user_object = "ZAPPCAT_CL_LOG"
user_prompt = f"Document the ABAP object `{user_object}`: what is it and how is it used?"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=system_prompt + "\n\n" + user_prompt,
    config=config,
)

print(response.text)
