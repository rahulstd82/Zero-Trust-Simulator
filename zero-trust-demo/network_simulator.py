class NetworkSimulator:
    def __init__(self):
        self.threat_intel_database = {
            "malicious_ips": ["192.168.1.100", "10.0.0.99"],
            "suspicious_users": ["hacker123"],
            "compromised_devices": ["device-malware-001"]
        }
    
    def check_threat_intelligence(self, user_id, device_id):
        # Simulate threat intelligence lookup
        is_malicious = (
            user_id in self.threat_intel_database["suspicious_users"] or
            device_id in self.threat_intel_database["compromised_devices"]
        )
        
        result = {
            "is_malicious": is_malicious,
            "threat_types": [],
            "confidence_score": 0.95 if is_malicious else 0.05
        }
        
        if is_malicious:
            result["threat_types"] = ["suspicious_activity", "potential_breach"]
            print(f"   🚨 Threat Intel: MALICIOUS activity detected!")
        
        return result