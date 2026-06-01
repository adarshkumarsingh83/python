# agent 
* create .vscode dir 
* create mcp.json under .vscode dir 
* add the configuraiton for sse mcp server in mcp.json 
```
{
	"servers": {
		"my-mcp-server-0654fe0a": {
			"url": "http://localhost:8090/sse",
			"type": "sse"
		}
	},
	"inputs": []
}
```

