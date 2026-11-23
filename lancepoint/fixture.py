class FixtureApp:
    """Simulated AI application. patched=True closes every exposure."""
    def __init__(self, patched=False): self.patched=patched
    def get(self, path):
        if self.patched:
            protected={"/v1/models","/debug","/mcp","/admin","/metrics","/v1/chat/completions"}
            if path in protected: return {"status":401,"body":"unauthorized"}
            return {"status":200,"body":"ok"}
        table={
          "/v1/models":{"status":200,"body":'{"data":[{"id":"model-a"}]}'},
          "/debug":{"status":200,"body":"debug enabled: config and routes listed"},
          "/mcp":{"status":200,"body":'{"tools":[{"name":"run_shell"}]}'},
          "/admin":{"status":200,"body":"admin panel: user management"},
          "/metrics":{"status":200,"body":"llm_tokens_total 12345 prompt_store_entries 8"},
          "/v1/chat/completions":{"status":200,"body":'{"choices":[{"message":{"content":"hello"}}]}'},
        }
        return table.get(path, {"status":404,"body":"not found"})
