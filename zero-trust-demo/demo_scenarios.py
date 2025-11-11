#!/usr/bin/env python3
"""
Advanced Demo Scenarios for Zero Trust Simulation
Provides comprehensive testing and visualization capabilities
"""

import time
import json
from datetime import datetime
from main import ZeroTrustSimulation

class DemoScenarios:
    def __init__(self):
        self.simulation = ZeroTrustSimulation()
        self.scenario_results = []
    
    def run_comprehensive_demo(self):
        """Run all demonstration scenarios with detailed analysis"""
        print("\n" + "=" * 70)
        print("🎯 COMPREHENSIVE ZERO TRUST DEMONSTRATION SUITE")
        print("=" * 70)
        
        # Run all scenario categories
        self.run_employee_scenarios()
        self.run_device_risk_scenarios() 
        self.run_location_based_scenarios()
        self.run_role_based_scenarios()
        self.run_threat_scenarios()
        
        # Generate comprehensive report
        self.generate_demo_report()
    
    def run_employee_scenarios(self):
        """Test various employee access patterns"""
        print("\n👥 EMPLOYEE ACCESS SCENARIOS")
        print("-" * 50)
        
        scenarios = [
            {
                "name": "Standard Employee - HR Access",
                "user": "employee123",
                "device": "laptop-compliant", 
                "app": "hr_system",
                "location": "office",
                "expected": "GRANTED"
            },
            {
                "name": "Manager - Financial System", 
                "user": "manager789",
                "device": "laptop-compliant",
                "app": "financial_system",
                "location": "office", 
                "expected": "GRANTED"
            },
            {
                "name": "Employee - After Hours Access",
                "user": "employee123",
                "device": "laptop-compliant",
                "app": "financial_system", 
                "location": "office",
                "expected": "DENIED",
                "note": "Time-based restrictions"
            }
        ]
        
        for scenario in scenarios:
            self._run_single_scenario(scenario)
    
    def run_device_risk_scenarios(self):
        """Test device compliance impact on access"""
        print("\n📱 DEVICE COMPLIANCE SCENARIOS")
        print("-" * 50)
        
        scenarios = [
            {
                "name": "Compliant Mobile Device",
                "user": "employee123",
                "device": "mobile-compliant",
                "app": "intern_portal",
                "location": "office",
                "expected": "GRANTED"
            },
            {
                "name": "Non-compliant Laptop - Basic App",
                "user": "employee123", 
                "device": "laptop-non-compliant",
                "app": "intern_portal",
                "location": "office",
                "expected": "DENIED",
                "note": "Device compliance required for all apps"
            },
            {
                "name": "Unregistered Device Attempt",
                "user": "employee123",
                "device": "unknown-device-001", 
                "app": "hr_system",
                "location": "office",
                "expected": "DENIED",
                "note": "Unregistered devices automatically blocked"
            }
        ]
        
        for scenario in scenarios:
            self._run_single_scenario(scenario)
    
    def run_location_based_scenarios(self):
        """Test geographic and network location policies"""
        print("\n🌐 LOCATION-BASED ACCESS SCENARIOS")
        print("-" * 50)
        
        scenarios = [
            {
                "name": "Coffee Shop WiFi Access",
                "user": "employee123",
                "device": "laptop-compliant",
                "app": "hr_system", 
                "location": "public_wifi",
                "expected": "DENIED",
                "note": "Sensitive apps blocked on public networks"
            },
            {
                "name": "High-Risk Country Access",
                "user": "manager789",
                "device": "laptop-compliant", 
                "app": "financial_system",
                "location": "high_risk_country",
                "expected": "DENIED",
                "note": "Geographic restrictions for sensitive data"
            },
            {
                "name": "Remote Employee - Basic Access",
                "user": "employee123", 
                "device": "laptop-compliant",
                "app": "intern_portal",
                "location": "home_network",
                "expected": "GRANTED",
                "note": "Basic apps allowed from trusted remote locations"
            }
        ]
        
        for scenario in scenarios:
            self._run_single_scenario(scenario)
    
    def run_role_based_scenarios(self):
        """Test role-based access control (RBAC)"""
        print("\n👤 ROLE-BASED ACCESS SCENARIOS") 
        print("-" * 50)
        
        scenarios = [
            {
                "name": "Intern - HR System Attempt",
                "user": "intern456",
                "device": "laptop-compliant",
                "app": "hr_system",
                "location": "office", 
                "expected": "DENIED",
                "note": "Role-based access control enforcement"
            },
            {
                "name": "Intern - Portal Access",
                "user": "intern456",
                "device": "laptop-compliant",
                "app": "intern_portal", 
                "location": "office",
                "expected": "GRANTED",
                "note": "Appropriate access for role"
            },
            {
                "name": "Employee - Financial System Attempt", 
                "user": "employee123",
                "device": "laptop-compliant",
                "app": "financial_system",
                "location": "office",
                "expected": "DENIED", 
                "note": "Manager-level access required"
            }
        ]
        
        for scenario in scenarios:
            self._run_single_scenario(scenario)
    
    def run_threat_scenarios(self):
        """Test threat intelligence and risk detection"""
        print("\n🚨 THREAT DETECTION SCENARIOS")
        print("-" * 50)
        
        # Note: These would integrate with real threat intelligence in production
        scenarios = [
            {
                "name": "Suspicious User Behavior",
                "user": "employee123", 
                "device": "laptop-compliant",
                "app": "hr_system",
                "location": "office",
                "expected": "GRANTED",  # Would be denied with real threat intel
                "note": "Simulation - would integrate with UEBA systems"
            },
            {
                "name": "Compromised Device Access", 
                "user": "employee123",
                "device": "laptop-compliant", 
                "app": "financial_system",
                "location": "office",
                "expected": "GRANTED",  # Would be denied with real threat intel
                "note": "Simulation - would check device reputation feeds"
            }
        ]
        
        for scenario in scenarios:
            self._run_single_scenario(scenario)
    
    def _run_single_scenario(self, scenario):
        """Execute a single test scenario"""
        print(f"\n🎭 Scenario: {scenario['name']}")
        print(f"   Config: {scenario['user']} → {scenario['app']} via {scenario['device']} from {scenario['location']}")
        
        if 'note' in scenario:
            print(f"   Note: {scenario['note']}")
        
        # Execute the access request
        result = self.simulation.simulate_access_request(
            user_id=scenario['user'],
            device_id=scenario['device'], 
            app_name=scenario['app'],
            location=scenario['location']
        )
        
        # Record results
        scenario_result = {
            'scenario_name': scenario['name'],
            'expected': scenario['expected'],
            'actual': "GRANTED" if result['access_granted'] else "DENIED",
            'match': scenario['expected'] == ("GRANTED" if result['access_granted'] else "DENIED"),
            'reason': result['reason'],
            'risk_level': result.get('risk_level', 'unknown'),
            'timestamp': datetime.now().isoformat()
        }
        
        self.scenario_results.append(scenario_result)
        
        # Show validation
        if scenario_result['match']:
            print(f"   ✅ EXPECTED RESULT: {scenario_result['actual']}")
        else:
            print(f"   ❌ UNEXPECTED: Expected {scenario['expected']}, Got {scenario_result['actual']}")
    
    def generate_demo_report(self):
        """Generate comprehensive demonstration report"""
        print("\n" + "=" * 70)
        print("📊 ZERO TRUST DEMONSTRATION REPORT")
        print("=" * 70)
        
        total_scenarios = len(self.scenario_results)
        successful_matches = sum(1 for r in self.scenario_results if r['match'])
        access_granted = sum(1 for r in self.scenario_results if r['actual'] == "GRANTED")
        access_denied = total_scenarios - access_granted
        
        print(f"\n📈 EXECUTIVE SUMMARY:")
        print(f"   • Total Scenarios Tested: {total_scenarios}")
        print(f"   • Policy Accuracy: {successful_matches}/{total_scenarios} ({successful_matches/total_scenarios*100:.1f}%)")
        print(f"   • Access Granted: {access_granted} ({access_granted/total_scenarios*100:.1f}%)")
        print(f"   • Access Denied: {access_denied} ({access_denied/total_scenarios*100:.1f}%)")
        print(f"   • Zero Trust Enforcement Rate: {access_denied/total_scenarios*100:.1f}%")
        
        print(f"\n🔒 SECURITY EFFECTIVENESS:")
        print(f"   • Device Compliance Blocks: {self._count_blocks_by_reason('device')}")
        print(f"   • Role Violation Blocks: {self._count_blocks_by_reason('role')}")
        print(f"   • Location Policy Blocks: {self._count_blocks_by_reason('location')}")
        print(f"   • Risk Threshold Blocks: {self._count_blocks_by_reason('risk')}")
        
        print(f"\n🎯 KEY ZERO TRUST DEMONSTRATIONS:")
        demonstrations = [
            "✓ Continuous verification across multiple dimensions",
            "✓ Least privilege access enforcement", 
            "✓ Device health compliance checking",
            "✓ Geographic and network location policies",
            "✓ Role-based access control (RBAC)",
            "✓ Dynamic risk-based decision making",
            "✓ Assume-breach mentality in all decisions"
        ]
        for demo in demonstrations:
            print(f"   {demo}")
        
        print(f"\n📋 DETAILED SCENARIO RESULTS:")
        for i, result in enumerate(self.scenario_results, 1):
            status = "✅" if result['match'] else "❌"
            print(f"   {i:2d}. {status} {result['scenario_name']}")
            print(f"        Result: {result['actual']} (Expected: {result['expected']})")
            print(f"        Reason: {result['reason']}")
            print(f"        Risk Level: {result['risk_level']}")
    
    def _count_blocks_by_reason(self, reason_type):
        """Count access denials by specific reason categories"""
        denial_reasons = {
            'device': ['device', 'compliance', 'encryption', 'firewall', 'antivirus'],
            'role': ['role', 'intern', 'manager', 'unauthorized'],
            'location': ['location', 'country', 'geographic', 'network'], 
            'risk': ['risk', 'threshold', 'score']
        }
        
        if reason_type not in denial_reasons:
            return 0
        
        count = 0
        for result in self.scenario_results:
            if result['actual'] == "DENIED":
                reason_lower = result['reason'].lower()
                if any(keyword in reason_lower for keyword in denial_reasons[reason_type]):
                    count += 1
        
        return count
    
    def run_interactive_demo(self):
        """Allow interactive testing of custom scenarios"""
        print("\n🎮 INTERACTIVE ZERO TRUST DEMO")
        print("=" * 50)
        print("Test your own scenarios! Available options:")
        print("Users: employee123, intern456, manager789")
        print("Devices: laptop-compliant, laptop-non-compliant, mobile-compliant")
        print("Apps: hr_system, financial_system, intern_portal, file_share")
        print("Locations: office, home_network, public_wifi, high_risk_country")
        print("-" * 50)
        
        while True:
            try:
                print("\nEnter scenario details (or 'quit' to exit):")
                user_id = input("User ID: ").strip()
                if user_id.lower() == 'quit':
                    break
                
                device_id = input("Device ID: ").strip()
                app_name = input("Application: ").strip() 
                location = input("Location: ").strip()
                
                if not all([user_id, device_id, app_name, location]):
                    print("❌ Please fill all fields")
                    continue
                
                print(f"\n🚀 Testing: {user_id} → {app_name} via {device_id} from {location}")
                result = self.simulation.simulate_access_request(user_id, device_id, app_name, location)
                
                print(f"\n📋 RESULT: {'✅ ACCESS GRANTED' if result['access_granted'] else '❌ ACCESS DENIED'}")
                print(f"   Reason: {result['reason']}")
                print(f"   Risk Level: {result.get('risk_level', 'unknown')}")
                print(f"   Session Timeout: {result.get('session_timeout', 0)} seconds")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting interactive demo")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

def main():
    """Main function to run the demo scenarios"""
    demo = DemoScenarios()
    
    print("Zero Trust Demo Scenarios")
    print("1. Run Comprehensive Demo")
    print("2. Run Interactive Demo")
    print("3. Run Quick Basic Demo")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        demo.run_comprehensive_demo()
    elif choice == "2":
        demo.run_interactive_demo()
    elif choice == "3":
        # Run just the basic scenarios from main.py
        from main import main as basic_main
        basic_main()
    else:
        print("Running comprehensive demo...")
        demo.run_comprehensive_demo()

if __name__ == "__main__":
    main()