import os
import json
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Zafiyetli MCP Sunucusu")

# Wazuh/SIEM entegrasyonu için log dosyası yolu
LOG_FILE = "/var/log/mcp/mcp_audit.log"

def log_action(action, target, status, output_length=0):
    """Gelen istekleri SOC log formatında (JSON) kaydeder."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "app_name": "mcp-server",
        "action": action,
        "payload": target,
        "status": status,
        "response_size": output_length
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

class ToolRequest(BaseModel):
    target: str

@app.post("/api/tools/network_diag")
async def network_diag(req: ToolRequest):
    # KASITLI ZAFİYET (Improper Output Handling): 
    command = f"ping -c 1 {req.target}"
    
    log_action("network_diag_called", req.target, "processing")
    
    try:
        # os.popen ile komutu doğrudan shell üzerinde çalıştırıyoruz
        output = os.popen(command).read()
        log_action("network_diag_executed", req.target, "success", len(output))
        return {"result": output}
    except Exception as e:
        log_action("network_diag_error", req.target, "error", 0)
        raise HTTPException(status_code=500, detail=str(e))