import traceback
try:
    from groq import Groq
    import os
    print("Groq imported")
    client = Groq(api_key="gsk_test")
    print("Client initialized")
except Exception:
    traceback.print_exc()
