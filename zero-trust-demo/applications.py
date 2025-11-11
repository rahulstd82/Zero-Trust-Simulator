class ApplicationManager:
    def __init__(self):
        self.applications = {
            "hr_system": {
                "name": "Human Resources Portal",
                "sensitivity": "high",
                "data_classification": "confidential",
                "required_clearance": "employee"
            },
            "financial_system": {
                "name": "Financial Management System",
                "sensitivity": "very_high",
                "data_classification": "restricted",
                "required_clearance": "manager"
            },
            "intern_portal": {
                "name": "Intern Resources Portal",
                "sensitivity": "low",
                "data_classification": "internal",
                "required_clearance": "intern"
            },
            "file_share": {
                "name": "Corporate File Share",
                "sensitivity": "medium",
                "data_classification": "internal",
                "required_clearance": "employee"
            }
        }
    
    def get_application_info(self, app_name):
        return self.applications.get(app_name, {})