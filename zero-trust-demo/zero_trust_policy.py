from datetime import datetime

class ZeroTrustEngine:
    def __init__(self):
        self.policies = self._load_policies()
    
    def _load_policies(self):
        return {
            "hr_system": {
                "min_user_trust": 0.8,
                "require_device_compliance": True,
                "allowed_roles": ["employee", "manager"],
                "max_risk_score": 30,
                "blocked_locations": ["high_risk_country"],
                "require_mfa": True
            },
            "financial_system": {
                "min_user_trust": 0.9,
                "require_device_compliance": True,
                "allowed_roles": ["manager", "finance"],
                "max_risk_score": 20,
                "blocked_locations": ["high_risk_country", "public_wifi"],
                "require_mfa": True,
                "time_restrictions": {"start": 6, "end": 18}
            },
            "intern_portal": {
                "min_user_trust": 0.5,
                "require_device_compliance": True,
                "allowed_roles": ["intern", "employee", "manager"],
                "max_risk_score": 70,
                "require_mfa": False
            }
        }
    
    def evaluate_access(self, user_identity, device_status, app_name, risk_context):
        if app_name not in self.policies:
            return self._create_decision(False, f"Application {app_name} not found in policies")
        
        policy = self.policies[app_name]
        
        # Check user role
        if user_identity["role"] not in policy["allowed_roles"]:
            return self._create_decision(False, f"Role {user_identity['role']} not allowed for {app_name}")
        
        # Check device compliance
        if policy["require_device_compliance"] and not device_status["compliant"]:
            return self._create_decision(False, "Device compliance check failed")
        
        # Check user trust score
        if user_identity["trust_score"] < policy["min_user_trust"]:
            return self._create_decision(False, f"User trust score too low: {user_identity['trust_score']}")
        
        # Check risk score
        total_risk = risk_context["user_risk"] + risk_context["device_risk"]
        if total_risk > policy["max_risk_score"]:
            return self._create_decision(False, f"Total risk score too high: {total_risk}")
        
        # Check location
        if risk_context["location"] in policy.get("blocked_locations", []):
            return self._create_decision(False, f"Access blocked from location: {risk_context['location']}")
        
        # Check time restrictions
        if "time_restrictions" in policy:
            current_hour = risk_context["time_of_day"]
            restrictions = policy["time_restrictions"]
            if not (restrictions["start"] <= current_hour <= restrictions["end"]):
                return self._create_decision(False, "Access outside allowed hours")
        
        # Check threat intelligence
        if risk_context["threat_intel"]["is_malicious"]:
            return self._create_decision(False, "Threat intelligence match detected")
        
        # All checks passed - grant access with appropriate level
        return self._create_decision(True, "All Zero Trust checks passed", risk_level=total_risk)
    
    def _create_decision(self, granted, reason, risk_level=0):
        risk_category = "low" if risk_level < 30 else "medium" if risk_level < 70 else "high"
        
        decision = {
            "access_granted": granted,
            "reason": reason,
            "risk_level": risk_category,
            "timestamp": datetime.now().isoformat(),
            "session_timeout": 3600 if risk_category == "low" else 900,  # 1 hour or 15 minutes
            "allowed_actions": ["read", "write"] if granted and risk_category == "low" else ["read"] if granted else []
        }
        
        if granted:
            print(f"✅ ACCESS GRANTED (Risk: {risk_category.upper()}): {reason}")
        else:
            print(f"❌ ACCESS DENIED: {reason}")
            
        return decision