# Website_URL_CHECKER
print("🔍Website URL CHECKER🔍")
url=input("\n💻Enter the URL:")

if url.startswith("https://"):
    print("🔐This Website uses HTTPS (secure)")
elif url.startswith("http://"):
    print("🔓This Website uses HTTP (Not secure)")
else:
    print("❌It dose not look like complete URL")