import json
import shutil
import textwrap
import os
import time

with open('movies.json', 'r') as file:
    MOVIE_DATABASE = json.load(file).get("movies", [])

def print_premium_movie_cards(movies_list):

    if not movies_list:
        print("\n❌ No movies found.\n")
        return "Not found any movie"

    # ===== PREMIUM COLORS =====
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"

    term = shutil.get_terminal_size().columns
    WIDTH = min(88, term - 4)

    print()
    print(f"{MAGENTA}{'═'*WIDTH}{RESET}")
    print(
        f"{BOLD}{WHITE}"
        f"{'🎬 AI CURATED CINEMATIC COLLECTION 🎬'.center(WIDTH)}"
        f"{RESET}"
    )
    print(f"{MAGENTA}{'═'*WIDTH}{RESET}\n")

    for index, movie in enumerate(movies_list, 1):

        title = movie.get("title", "Unknown")
        year = movie.get("releaseYear", "----")
        rating = float(movie.get("rating", 0))
        length = movie.get("length", "N/A")
        industry = movie.get("industry", "N/A")
        
        # 👈 YAHAN CHANGES HUE HAIN: Lists ko comma se jodkar string bana diya
        language = ", ".join(movie.get("language", [])) or "N/A"
        director = ", ".join(movie.get("directors", [])) or "Unknown"
        genres = ", ".join(movie.get("genre", [])) or "N/A"
        actors = ", ".join(movie.get("actors", [])) or "N/A"

        # Rating Bar
        filled = int(round(rating))
        bar = "★ "*filled + "☆ "*(10-filled)

        print(f"{CYAN}╔{'═'*(WIDTH-2)}╗{RESET}")

        title_text = f"🎬 {title.upper()} ({year})"
        print(
            f"{CYAN}║{RESET}"
            f"{BOLD}{WHITE}{title_text.center(WIDTH-3)}{RESET}"
            f"{CYAN}║{RESET}"
        )

        print(f"{CYAN}╠{'═'*(WIDTH-2)}╣{RESET}")

        print(
            f"{CYAN}║{RESET} ⭐ Rating    "
            f"{YELLOW}{rating:.1f}/10{RESET} "
            f"{GREEN}{bar}{RESET}"
            + " "*max(0, (WIDTH-23-len(bar)))
            + f"{CYAN}║{RESET}"
        )

        # Agar language ya director ka text lamba ho, toh UI break na ho isliye max() ka use kiya hai
        print(
            f"{CYAN}║{RESET} 🌍 Language  {WHITE}{language[:WIDTH-20]}{RESET}"
            + " "*max(0, (WIDTH-16-len(language[:WIDTH-20])))
            + f"{CYAN}║{RESET}"
        )

        print(
            f"{CYAN}║{RESET} 🎞️  Industry  {WHITE}{industry}{RESET}"
            + " "*max(0, (WIDTH-16-len(industry)))
            + f"{CYAN}║{RESET}"
        )
        
        print(
            f"{CYAN}║{RESET} ⏱ Runtime   {WHITE}{length} mins{RESET}"
            + " "*max(0, (WIDTH-20-len(str(length))))
            + f"{CYAN}║{RESET}"
        )

        print(
            f"{CYAN}║{RESET} 🎥 Director  {MAGENTA}{director[:WIDTH-20]}{RESET}"
            + " "*max(0, (WIDTH-16-len(director[:WIDTH-20])))
            + f"{CYAN}║{RESET}"
        )

        print(f"{CYAN}╠{'─'*(WIDTH-2)}╣{RESET}")

        wrapped_genres = textwrap.wrap(genres, WIDTH-18)
        if not wrapped_genres: wrapped_genres = ["N/A"]

        print(
            f"{CYAN}║{RESET} 🎭 Genres    "
            f"{BLUE}{wrapped_genres[0]}{RESET}"
            + " "*max(0, (WIDTH-16-len(wrapped_genres[0])))
            + f"{CYAN}║{RESET}"
        )

        for line in wrapped_genres[1:]:
            print(
                f"{CYAN}║{RESET}             "
                f"{BLUE}{line}{RESET}"
                + " "*max(0, (WIDTH-14-len(line)))
                + f"{CYAN}║{RESET}"
            )

        print(f"{CYAN}╠{'─'*(WIDTH-2)}╣{RESET}")

        wrapped_actors = textwrap.wrap(actors, WIDTH-18)
        if not wrapped_actors: wrapped_actors = ["N/A"]

        print(
            f"{CYAN}║{RESET} 👥 Cast      "
            f"{WHITE}{wrapped_actors[0]}{RESET}"
            + " "*max(0, (WIDTH-16-len(wrapped_actors[0])))
            + f"{CYAN}║{RESET}"
        )

        for line in wrapped_actors[1:]:
            print(
                f"{CYAN}║{RESET}             "
                f"{WHITE}{line}{RESET}"
                + " "*max(0, (WIDTH-16-len(line)))
                + f"{CYAN}║{RESET}"
            )

        print(f"{CYAN}╠{'═'*(WIDTH-2)}╣{RESET}")

        footer = f"✨ Recommendation #{index}"
        print(
            f"{CYAN}║{RESET}"
            f"{GREEN}{footer.center(WIDTH-3)}{RESET}"
            f"{CYAN}║{RESET}"
        )

        print(f"{CYAN}╚{'═'*(WIDTH-2)}╝{RESET}\n")

    return f"movies found and shown to user. total movies is {len(movies_list)} yeh user ko bata dena."

def movie_Suggest_Reply(genre=None, language=None, length=None, min_rating=None, movie_name=None, actors=None, producer=None, director=None, release_year=None, industry=None):
    
    # Inputs ko lower case mein convert karna
    s_lang = language.lower() if language else None
    s_genre = genre.lower() if genre else None
    s_title = movie_name.lower() if movie_name else None
    s_prod = producer.lower() if producer else None
    s_dir = director.lower() if director else None
    s_industry = industry.lower() if industry else None
    
    # Agar actors list mein hain, toh usko pehle hi lowercase 'Set' bana lo
    s_actors = set(a.lower() for a in actors) if actors else None

    print("🔍 Movies search ho rahi hain...\n")
    matched_movies = []

    for movie in MOVIE_DATABASE:
        
        # 👈 YAHAN CHANGE HUA HAI: Ab language ek list hai, toh hum check kar rahe hain ki user ki manga hua language list ke andar hai ya nahi
        if s_lang and s_lang not in [l.lower() for l in movie.get("language", [])]:
            continue
            
        if s_genre and s_genre not in [g.lower() for g in movie.get("genre", [])]:
            continue
            
        if s_industry and movie.get("industry", "").lower() != s_industry:
            continue

        if min_rating and movie.get("rating", 0) < min_rating:
            continue
            
        if length and movie.get("length", 0) > length:
            continue
            
        if s_title and movie.get("title", "").lower() != s_title:
            continue
            
        if s_actors:
            # Movie ke actors ko set banakar intersection check karte hain
            m_actors = set(a.lower() for a in movie.get("actors", []))
            if not s_actors.intersection(m_actors): 
                continue
                
        if s_prod and s_prod not in [p.lower() for p in movie.get("producers", [])]:
            continue
            
        if s_dir and s_dir not in [d.lower() for d in movie.get("directors", [])]:
            continue
            
        if release_year and movie.get("releaseYear") != release_year:
            continue
            
        # Agar movie ne upar ki saari conditions pass kar li, toh usko list mein add kar do
        matched_movies.append(movie)


    return print_premium_movie_cards(matched_movies)


def start_movie_search_session():
    os.system("cls" if os.name == "nt" else "clear")

    # ===== COLORS =====
    RESET = "\033[0m"
    BOLD = "\033[1m"

    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"

    width = min(92, shutil.get_terminal_size().columns - 2)

    def line(char="═"):
        print(f"{MAGENTA}{char * width}{RESET}")

    def center(text, color=WHITE, bold=False):
        style = BOLD if bold else ""
        print(f"{style}{color}{text.center(width)}{RESET}")

    def loading(text):
        print(f"{GREEN}✓ {text}{RESET}")
        time.sleep(0.18)

    # ===========================
    # HEADER
    # ===========================

    line()

    center("🎬 M U V I O", WHITE, True)
    center("AI THAT KNOWS YOUR NEXT MOVIE", CYAN)
    center("Talk. Discover. Watch.", GRAY)

    line()

    print()

    # ===========================
    # INITIALIZATION
    # ===========================


    loading("Warming up the Muvio AI Core")
    loading("Activating Muvio Intelligence")
    loading("Initializing Muvio Conversation Engine")
    loading("Building Your Personalized Movie Profile")
    loading("Exploring Millions of Movie Possibilities")
    loading("Almost Ready... Your Next Favorite Movie Awaits")


    print()

    # ===========================
    # WELCOME PANEL
    # ===========================

    print(f"{CYAN}╭{'─'*(width-2)}╮{RESET}")

    print(
        f"{CYAN}│{RESET}"
        f"{BOLD}{WHITE}{'✨ Welcome to Muvio ✨'.center(width-4)}{RESET}"
        f"{CYAN}│{RESET}"
    )

    print(f"{CYAN}├{'─'*(width-2)}┤{RESET}")

    messages = [
        "🤖 Chat naturally about any movie.",
        "🎭 Tell me your mood, favorite genres or actors.",
        "🍿 Receive AI-powered personalized recommendations.",
        "⭐ Discover hidden gems and blockbuster hits instantly.",
        f"🚪 Type {YELLOW}'exit'{RESET}{CYAN} or {YELLOW}'quit'{RESET}{CYAN} anytime to end your cinematic journey."
    ]

    for msg in messages:
        visible = msg.replace(RESET, "").replace(CYAN, "").replace(YELLOW, "")
        padding = width - len(visible) - 5
        print(f"{CYAN}│{RESET} {msg}{' '*max(0,padding)} {CYAN}│{RESET}")

    print(f"{CYAN}╰{'─'*(width-2)}╯{RESET}")

    print()

    center("🍿 Ready to Find Your Next Favorite Movie!", GREEN, True)

    print()      
   