# 🔗 Advanced Log Correlation Engine

# Simulated logs (attack sequence)
logs = [
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "PRIVILEGE ESCALATION - admin",
    "FILE ACCESS - sensitive_data.txt"
]

# Flags to track attack stages
failed_attempts = 0
successful_login = False
privilege_escalation = False
data_access = False

# Process logs
for log in logs:

    # Detect failed login attempts
    if "LOGIN FAILED" in log:
        failed_attempts += 1

    # Detect successful login
    elif "LOGIN SUCCESS" in log:
        successful_login = True

    # Detect privilege escalation
    elif "PRIVILEGE ESCALATION" in log:
        privilege_escalation = True

    # Detect sensitive data access
    elif "FILE ACCESS" in log:
        data_access = True

# Display report
print("=== Correlation Engine Report ===\n")

# Correlation logic (attack chain detection)
if failed_attempts >= 2 and successful_login:
    print("[STAGE 1] Brute force attack detected")

if successful_login and privilege_escalation:
    print("[STAGE 2] Privilege escalation detected")

if privilege_escalation and data_access:
    print("[STAGE 3] Data access detected")

# Final verdict
if failed_attempts >= 2 and successful_login and privilege_escalation and data_access:
    print("\n[CRITICAL ALERT] Full attack chain detected")
