"""Problem: Check if a password is 
"Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 
6-10 chars (Medium), >10 chars (Strong)."""

print("Enter your password")
password = input()

if len(password)< 6 :
    print("weak password")
elif len(password) < 10 and len(password) >6 :
    print("average password")
else :
    print("strong password")
    