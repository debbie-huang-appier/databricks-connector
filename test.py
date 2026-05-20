from databricks.sdk import WorkspaceClient
from databricks_mcp import DatabricksMCPClient

ws = WorkspaceClient(
    host="https://1005657065394160.0.gcp.databricks.com",
    client_id="32b93186-4dd1-47ba-811f-ca11f9d77f45",
    client_secret="dose40fb98ab446bda2a0526592b7980d17a",
)

mcp = DatabricksMCPClient(
    server_url=f"{ws.config.host}/api/2.0/mcp/functions/system/ai",
    workspace_client=ws
)

tools = mcp.list_tools()

print(tools)