import os
import requests

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")

def call_network_diag(target_ip):
    url = f"{MCP_SERVER_URL}/api/tools/network_diag"
    payload = {"target": target_ip}
    
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("="*50)
    print("🔧 Zafiyetli MCP Ajan İstemcisine Hoş Geldiniz")
    print("="*50)
    print("Normal Kullanım örneği: 127.0.0.1")
    print("Saldırı Kullanımı (Command Injection): 127.0.0.1; whoami")
    print("="*50)
    
    while True:
        target = input("\nAğ tanılama için hedef IP girin (Çıkmak için 'q'): ")
        if target.lower() == 'q':
            break
        
        print(f"[*] MCP Sunucusuna İstek Gönderiliyor: {target}...")
        result = call_network_diag(target)
        
        print("[+] Sunucu Yanıtı:\n")
        print(result.get('result', result))