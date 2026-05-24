class AIRules:
    def __init__(self):
        self.rules = {
            "no_sudo": "Never execute sudo commands",
            "no_rm_rf": "Never use rm -rf commands",
            "no_curl_bash": "Never execute curl | bash commands",
            "no_malware": "Never generate or execute malware",
            "no_secret_exposure": "Never expose secrets or sensitive information"
        }

    def validate_prompt(self, prompt):
        for rule in self.rules.values():
            if rule.lower() in prompt.lower():
                return False
        return True