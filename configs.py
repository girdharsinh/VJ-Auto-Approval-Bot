# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21956753"))
    API_HASH = getenv("API_HASH", "c7a1e49d8e51bf0c6bfc4590644932b2")
    BOT_TOKEN = getenv("BOT_TOKEN", "8285593662:AAG1MtG-OX-h1jN3stZwtcO8ULeKJqXQvAM")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1003188691331")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7892623050 6868089702").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sarvaiyagirdharsinh_db_user:sarvaiya999@cluster0.ufhhv44.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
