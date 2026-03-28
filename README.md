# 🔗 cyber-project-11-log-correlation-engine
Advanced log correlation engine for attack chain detection


## Context

Advanced SIEM systems correlate multiple events to detect complex attacks.

This project simulates attack chain detection through log correlation.

---

## Objective

* Correlate multiple security events
* Detect attack chains
* Simulate advanced SOC logic

---

## 🔍 Logs

```id="zzr4qb"
LOGIN FAILED - admin - 45.33.32.1
LOGIN FAILED - admin - 45.33.32.1
LOGIN SUCCESS - admin - 45.33.32.1
PRIVILEGE ESCALATION - admin
FILE ACCESS - sensitive_data.txt
```

---

## Detection Logic

* Failed logins → brute force
* Successful login → compromise
* Privilege escalation → attacker control
* File access → data breach

---

## Conclusion

Full attack chain detected:

* Initial access
* Privilege escalation
* Data access

---

## Key Takeaways

* Event correlation
* Attack chain detection
* Advanced SOC analysis

---

## 👨‍💻 Author

Part of my cybersecurity learning journey.
