#!/usr/bin/env python3
"""
Zero Trust Architecture Simulation
Fully functional demo showing risk-based access control
"""

import time
import json
from datetime import datetime
from zero_trust_policy import ZeroTrustEngine
from device_posture import DevicePostureChecker
from user_identity import UserIdentityService
from applications import ApplicationManager
from network_simulator import NetworkSimulator

class ZeroTrustSimulation:
    def __init__(self):
        self.policy_engine = ZeroTrustEngine()
        self.device_checker = DevicePostureChecker()
        self.user_service = UserIdentityService()
        self.app_manager = ApplicationManager()
        self.network = NetworkSimulator()
        
        print("🚀 Zero Trust Simulation Initialized")
        print("=" * 50)
    
    def simulate_access_request(self, user_id, device_id, app_name, location="office"):
        """Simulate a complete Zero Trust access request"""
        print(f"\n🔍 Processing Access Request:")
        print(f"   User: {user_id}")
        print(f"   Device: {device_id}")
        print(f"   Application: {app_name}")
        print(f"   Location: {location}")
        print("-" * 40)
        
        # Step 1: Verify User Identity
        user_identity = self.user_service.verify_user(user_id)
        if not user_identity["authenticated"]:
            return self._deny_access("User authentication failed")
        
        # Step 2: Check Device Posture
        device_status = self.device_checker.check_device_compliance(device_id)
        
        # Step 3: Evaluate Risk Context
        risk_context = {
            "user_risk": user_identity["risk_score"],
            "device_compliant": device_status["compliant"],
            "device_risk": device_status["risk_score"],
            "location": location,
            "time_of_day": datetime.now().hour,
            "threat_intel": self.network.check_threat_intelligence(user_id, device_id)
        }
        
        # Step 4: Make Policy Decision
        policy_decision = self.policy_engine.evaluate_access(
            user_identity, device_status, app_name, risk_context
        )
        
        # Step 5: Log and Enforce
        self._log_access_attempt(user_id, app_name, policy_decision)
        
        return policy_decision
    
    def _deny_access(self, reason):
        decision = {
            "access_granted": False,
            "reason": reason,
            "allowed_actions": [],
            "session_duration": 0,
            "timestamp": datetime.now().isoformat()
        }
        print(f"❌ ACCESS DENIED: {reason}")
        return decision
    
    def _log_access_attempt(self, user_id, app_name, decision):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "application": app_name,
            "decision": "GRANTED" if decision["access_granted"] else "DENIED",
            "reason": decision.get("reason", "Policy evaluation"),
            "risk_level": decision.get("risk_level", "unknown")
        }
        print(f"📝 Security Log: {json.dumps(log_entry, indent=2)}")

def main():
    # Initialize the simulation
    simulation = ZeroTrustSimulation()
    
    # Run demonstration scenarios
    print("\n" + "=" * 60)
    print("🎭 ZERO TRUST DEMONSTRATION SCENARIOS")
    print("=" * 60)
    
    # Scenario 1: Compliant Employee Access
    print("\n1. ✅ Compliant Employee Accessing HR System")
    result1 = simulation.simulate_access_request(
        user_id="employee123",
        device_id="laptop-compliant",
        app_name="hr_system"
    )
    
    # Scenario 2: Non-compliant Device
    print("\n2. ❌ Employee with Non-compliant Device")
    result2 = simulation.simulate_access_request(
        user_id="employee123", 
        device_id="laptop-non-compliant",
        app_name="hr_system"
    )
    
    # Scenario 3: Intern Access
    print("\n3. 🔐 Intern Access to Sensitive System")
    result3 = simulation.simulate_access_request(
        user_id="intern456",
        device_id="laptop-compliant", 
        app_name="financial_system"
    )
    
    # Scenario 4: High-Risk Location
    print("\n4. 🌐 Access from High-Risk Geographic Location")
    result4 = simulation.simulate_access_request(
        user_id="employee123",
        device_id="laptop-compliant",
        app_name="hr_system", 
        location="high_risk_country"
    )
    
    # Display summary
    print("\n" + "=" * 60)
    print("📊 DEMONSTRATION SUMMARY")
    print("=" * 60)
    scenarios = [result1, result2, result3, result4]
    granted = sum(1 for r in scenarios if r["access_granted"])
    denied = len(scenarios) - granted
    
    print(f"Access Granted: {granted} scenarios")
    print(f"Access Denied:  {denied} scenarios")
    print(f"Zero Trust Enforcement: {denied/len(scenarios)*100:.1f}% of requests blocked")

if __name__ == "__main__":
    main()