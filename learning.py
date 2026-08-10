Has_account=True
Email_verified=False

can_login=Has_account and Email_verified
email=" g@example.com"
is_email_valid="@" in email

user_age= 17
is_age_valid= user_age >= 18
can_login_final = (
    Has_account
    and Email_verified
    and is_email_valid
    and is_age_valid)

print("can_login:",can_login)
print("is_email_valid:",is_email_valid)
print("is_age_valid:",is_age_valid)
print("can_loging_final:",can_login_final)
print("Has_account is true:",Has_account is True)