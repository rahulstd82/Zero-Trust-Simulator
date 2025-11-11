from datetime import datetime, timedelta

class UserIdentityService:
    def __init__(self):
        self.user_database = {
            "employee245": {
                "name": "Vivek Shasi",
                "role": "employee",
                "department": "Engineering",
                "trust_score": 0.9,
                "last_login": datetime.now() - timedelta(hours=2),
                "mfa_enabled": True,
                "risk_factors": []
            },
            "intern001": {
                "name": "Rahul ",
                "role": "intern",
                "department": "HR",
                "trust_score": 0.7,
                "last_login": datetime.now() - timedelta(days=1),
                "mfa_enabled": False,
                "risk_factors": ["new_account"]
            },
            "manager101": {
                "name": "Pratap",
                "role": "manager",
                "department": "Finance",
                "trust_score": 0.95,
                "last_login": datetime.now() - timedelta(minutes=30),
                "mfa_enabled": True,
                "risk_factors": []
            }
        }
    
    def verify_user(self, user_id):
        if user_id not in self.user_database:
            return {
                "authenticated": False,
                "risk_score": 100,
                "reason": "User not found"
            }
        
        user = self.user_database[user_id]
        
        # Calculate risk score based on various factors
        risk_score = 0
        
        # Account age risk
        if "new_account" in user["risk_factors"]:
            risk_score += 25
        
        # Login recency
        login_recency = datetime.now() - user["last_login"]
        if login_recency > timedelta(days=30):
            risk_score += 30
        elif login_recency > timedelta(days=7):
            risk_score += 15
        
        # MFA status
        if not user["mfa_enabled"]:
            risk_score += 20
        
        result = {
            "authenticated": True,
            "user_id": user_id,
            "name": user["name"],
            "role": user["role"],
            "department": user["department"],
            "trust_score": user["trust_score"],
            "risk_score": risk_score,
            "mfa_required": user["mfa_enabled"],
            "last_login": user["last_login"].isoformat()
        }
        
        print(f"   👤 User Identity: {user['name']} ({user['role']})")
        print(f"      Trust Score: {user['trust_score']}, Risk Score: {risk_score}")
        
        return result