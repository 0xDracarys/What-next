# Import the required libraries
import requests

# Define the function to get the tool name
def get_tool_name(attack_name):
  # Set the URL of the online tool database
  url = "https://toolswatch.org/cyber-tools-list/"

  # Send the GET request to the tool database
  response = requests.get(url)

  # Check the response status code
  if response.status_code == 200:
    # Search for the attack name in the response text
    if attack_name in response.text:
      # Print the tool name if found
      print(f"Tool name: {tool_name}")
    else:
      # Print a message if no tool was found
      print(f"No tool found for attack '{attack_name}'")
  else:
    # Print an error message if the request failed
    print(f"Request failed with status code {response.status_code}")


