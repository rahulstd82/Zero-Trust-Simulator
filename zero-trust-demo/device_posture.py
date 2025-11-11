from datetime import datetime, timedelta

class DevicePostureChecker:
    def __init__(self):
        self.device_database = {
            "laptop-compliant": {
                "encryption_enabled": True,
                "firewall_active": True,
                "antivirus_updated": True,
                "os_patched": True,
                "last_seen": datetime.now() - timedelta(hours=2),
                "risk_score": 10
            },
            "laptop-non-compliant": {
                "encryption_enabled": False,
                "firewall_active": False,
                "antivirus_updated": False,
                "os_patched": False,
                "last_seen": datetime.now() - timedelta(days=30),
                "risk_score": 75
            },
            "mobile-compliant": {
                "encryption_enabled": True,
                "firewall_active": True,
                "antivirus_updated": True,
                "os_patched": True,
                "last_seen": datetime.now() - timedelta(hours=1),
                "risk_score": 15
            }
        }
    
    def check_device_compliance(self, device_id):
        if device_id not in self.device_database:
            return {
                "compliant": False,
                "risk_score": 100,
                "checks_failed": ["device_not_registered"],
                "last_check": datetime.now().isoformat()
            }
        
        device = self.device_database[device_id]
        failed_checks = []
        
        if not device["encryption_enabled"]:
            failed_checks.append("disk_encryption")
        if not device["firewall_active"]:
            failed_checks.append("firewall")
        if not device["antivirus_updated"]:
            failed_checks.append("antivirus")
        if not device["os_patched"]:
            failed_checks.append("os_updates")
        
        # Check if device seen recently
        if datetime.now() - device["last_seen"] > timedelta(days=7):
            failed_checks.append("device_inactive")
            device["risk_score"] += 20
        
        is_compliant = len(failed_checks) == 0
        
        result = {
            "device_id": device_id,
            "compliant": is_compliant,
            "risk_score": device["risk_score"] + (len(failed_checks) * 10),
            "checks_failed": failed_checks,
            "last_check": datetime.now().isoformat()
        }
        
        print(f"   📱 Device Posture: {device_id}")
        print(f"      Compliant: {is_compliant}, Risk Score: {result['risk_score']}")
        if failed_checks:
            print(f"      Failed Checks: {', '.join(failed_checks)}")
        
        return result