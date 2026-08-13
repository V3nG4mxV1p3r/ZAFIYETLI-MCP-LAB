# Zafiyetli MCP Laboratuvarı (Vulnerable MCP Lab)

Tarayıcı üzerinden çalışan, ajan (agent) tabanlı yapay zeka sistemlerindeki dolaylı istem enjeksiyonu (Indirect Prompt Injection) ve komut enjeksiyonu (Command Injection) risklerini pratik ettiren interaktif Docker laboratuvarı. 

Bu laboratuvar, sadece zafiyet sömürmeyi değil, aynı zamanda Mavi Takım (Blue Team) pratikleri için arka planda SIEM/Wazuh tespit kurallarının test edilmesini de hedefler.

---

## Özellikler

* Gerçekçi Saldırı Yüzeyi: LLM girdilerinin yetersiz temizlenmesi (Improper Output Handling) sonucu oluşan zafiyetleri simüle eder.
* Konteynerize Mimari: MCP sunucusu ve Ajan istemcisi izole Docker konteynerlerinde çalışır.
* Tehdit Avcılığı (Threat Hunting): Olayları SOC analizi için JSON formatında yapılandırılmış olarak /var/log/mcp/mcp_audit.log dizinine yazar.
* Hazır Tespit Kuralları: MITRE ATT&CK (T1059) destekli Wazuh kural seti (wazuh-rules/mcp_threat_rules.xml) ile entegre çalışır.

---

## Kurulum ve Kullanım

## 1. Laboratuvarı Ayağa Kaldırma
Bilgisayarınızda Docker ve Docker Compose kurulu olduğundan emin olun. Repoyu klonladıktan sonra ana dizinde şu komutu çalıştırın:

`bash
docker compose up --build -d
`

---
## 2. Kırmızı Takım: Sistemi Sömürme
**Ajan konteynerinin içine girerek saldırı senaryosunu başlatın:**

`bash
docker exec -it mcp-agent-client python client.py
`
* Normal Kullanım (Zararsız İstek): 127.0.0.1

* Zafiyet Tetikleme (Zararlı Payload): 127.0.0.1; cat /etc/passwd veya 127.0.0.1; ls -la

---

## 3. Mavi Takım: Log İnceleme ve Tespit
**Saldırı sonrası, sunucunun arka planda ürettiği güvenlik loglarını inceleyin:**

`bash
docker exec -it vulnerable-mcp-server cat /var/log/mcp/mcp_audit.log
`

*Zararlı payload sisteme ulaştığında, projede bulunan kural seti sayesinde loglar SIEM üzerinde Level 12 (Kritik) alarm üretecek şekilde tasarlanmıştır.*

---

## Sistemi Temizleme
**Laboratuvarı kapatmak ve üretilen logları (volume dahil) temizlemek için:**

`bash
docker compose down -v
`
