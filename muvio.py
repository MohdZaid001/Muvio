import shutil
import textwrap
from typing import Optional, List
from google import genai
from google.genai import types
from config import GEMINI_API_KEY
from prompts import behavior_prompts
from movie_search_algorithm import movie_Suggest_Reply, start_movie_search_session
from speaking import speak
from listning import voice_input
from talking_type import input_type

# =========================
# COLORS
# =========================

RESET   = "\033[0m"
BOLD    = "\033[1m"

CYAN    = "\033[96m"
BLUE    = "\033[94m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"
RED      = "\033[91m"
GRAY     = "\033[90m"


# Client initializing
client = genai.Client(api_key=GEMINI_API_KEY)

isSpeak = input_type()

def search_movie_db(
    genre: Optional[str] = None, 
    language: Optional[str] = None, 
    length: Optional[int] = None, 
    min_rating: Optional[float] = None, 
    movie_name: Optional[str] = None, 
    actors: Optional[List[str]] = None, 
    producer: Optional[str] = None, 
    director: Optional[str] = None, 
    release_year: Optional[int] = None, 
    industry: Optional[str] = None
    ):
    
    r = movie_Suggest_Reply(
        genre=genre, 
        language=language, 
        length=length, 
        min_rating=min_rating, 
        movie_name=movie_name, 
        actors=actors, 
        producer=producer, 
        director=director,
        release_year=release_year,
        industry=industry
    )
    
    return r

my_config = types.GenerateContentConfig(
    system_instruction=behavior_prompts,
    temperature=0.5,
    tools=[search_movie_db],  
)

# Chat session start 
chat = client.chats.create(
    model='gemini-flash-lite-latest',
    config=my_config
)

start_movie_search_session()

while True:

    print(
        f"\n{CYAN}{'─'*82}{RESET}"
    )

    user_input = ""

    if isSpeak:
        print("listning...")
        user_input = voice_input()
        while not user_input.strip():
            user_input = voice_input()


        print(
        f"{BOLD}{CYAN}🎤 You {GRAY}› {RESET} {user_input}"
        )
    else:
        user_input = input(
        f"{BOLD}{CYAN}🎤 You {GRAY}› {RESET}"
        )        

    

    # =========================
    # EXIT LOGIC
    # =========================

    if user_input.lower().strip() in ("quit", "exit"):

        print()

        print(f"{GREEN}{BOLD}👋 Thank you for choosing Muvio!{RESET}")
        if isSpeak:
            speak("Thank you for choosing Muvio!")

        print(f"{CYAN}🍿 Enjoy your movie and see you again soon.{RESET}\n")

        break

    # =========================
    # EMPTY INPUT CHCKING
    # =========================

    if not user_input.strip():

        # print(
        #     f"{YELLOW}⚠ No input detected."
        # )
        # if isSpeak:        
        #     speak("Please, type or speak something to continue.")

        continue

    try:

        print(f"\n{MAGENTA}🧠 Muvio is thinking...{RESET}")

        response = chat.send_message(user_input)

        # Terminal Width
        terminal_width = shutil.get_terminal_size().columns

        # Maximum Box Width
        BOX_WIDTH = min(90, terminal_width - 4)

        # Content Width
        CONTENT_WIDTH = BOX_WIDTH - 4

        # Wrap text automatically
        lines = textwrap.wrap(response.text, width=CONTENT_WIDTH)
        

        print()

        print(f"{CYAN}╭{'─'*BOX_WIDTH}╮{RESET}")

        title = "🤖 Muvio"

        print(
            f"{CYAN}│ {BOLD}{WHITE}{title}{RESET}"
            + " "*(BOX_WIDTH-len(title)-2)
            + f"{CYAN}│{RESET}"
        )

        print(f"{CYAN}├{'─'*BOX_WIDTH}┤{RESET}")

        for line in lines:
            print(
                f"{CYAN}│ {WHITE}{line}{RESET}"
                + " "*(CONTENT_WIDTH-len(line)+3)
                + f"{CYAN}│{RESET}"
            )

        print(f"{CYAN}╰{'─'*BOX_WIDTH}╯{RESET}")

        if isSpeak:
            speak(response.text)

    except Exception as e:

        print()

        print(
            f"{RED}{BOLD}❌ Oops! Something went wrong.{RESET}"
        )
        if isSpeak:
            speak("Oops! Something went wrong.")

        print(
            f"{GRAY}Please try again in a moment.{RESET}"
        )
        if isSpeak:
            speak("Please try again in a moment.")

        # # Development only
        # print(
        #     f"{YELLOW}🔍 {e}{RESET}\n"
        # )


    
