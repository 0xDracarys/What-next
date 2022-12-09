# <h3>What-next</h3>
Python script that prints the name of a tool to use based on the name of an attack

<h3># Example usage<br>
get_tool_name("SQL injection")</h3>
This program uses the requests library to send a GET request to the online tool database at https://toolswatch.org/cyber-tools-list/, 
and then searches the response text for the attack name.
If the attack name is found, the name of the associated tool is printed.
If no tool is found, a message is printed. If the request fails, an error message is printed.
