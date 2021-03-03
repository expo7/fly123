import pyotp
totp  = pyotp.TOTP("X332CR3PQSYGYOF7").now()
print("Current OTP:", totp)