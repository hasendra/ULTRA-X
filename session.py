from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("")
print("""Wᴇʟᴄᴏᴍᴇ ᴛᴏ Captain Usᴇʀʙᴏᴛ Sᴛʀɪɴɢ Gᴇɴᴇʀᴀᴛᴏʀ ʙʏ @Thecaptain101""")
print("""Kɪɴᴅʟʏ ᴇɴᴇᴛᴇʀ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here Is Your String Session For Using UltraX Userbot\n(**Tap to copy it**)👇 \n\n `{session}` \n\n And Visit @Thecaptain101 For Any Help !"
   )

   print(
       "Thanks for Choosing Captain Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
   )
 except Exception as e:
  print(str(e))
  print(
      "\nWrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry"
  )
  print("")
  continue
 break
