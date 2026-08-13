import shutil

RESET = "\033[0m"
BOLD = "\033[1m"

WHITE = "\033[97m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RED = "\033[91m"


# Call at start and get how user want to talk
def input_type():

    width = min(96, shutil.get_terminal_size().columns - 2)

    print()

    print(f"{MAGENTA}{'═'*width}{RESET}")

    print(f"{BOLD}{WHITE}{'✨ CHOOSE YOUR MUVIO EXPERIENCE ✨'.center(width)}{RESET}")
    print(f"{CYAN}{'Talk Naturally • Discover Movies • Enjoy Cinema'.center(width)}{RESET}")

    print(f"{MAGENTA}{'═'*width}{RESET}\n")

    left = [
        "💬 CHAT MODE",
        "",
        "⌨️  Type naturally",
        "Ask about movies",
        "Fast keyboard interaction",
        "",
        f"{GREEN}Press [1]{RESET}"
    ]

    right = [
        "   🎙️  VOICE MODE",
        "",
        "    🎤 Speak naturally",
        "    Hands-free conversation",
        "    Real-time AI interaction",
        "",
        f"{GREEN}     Press [2]{RESET}"
    ]

    CARD = 38

    top = f"{CYAN}╭{'─'*CARD}╮{RESET}"
    mid = f"{CYAN}{RESET}"
    bottom = f"{CYAN}╰{'─'*CARD}╯{RESET}"

    print(f"{top}    {top}")

    for l, r in zip(left, right):

        l_plain = l.replace(RESET,"").replace(GREEN,"")
        r_plain = r.replace(RESET,"").replace(GREEN,"")

        print(
            f"{mid} {WHITE}{l}{RESET}"
            + " "*(CARD-len(l_plain)-1)
            + f"{CYAN}{RESET}   "
            + f"{mid} {WHITE}{r}{RESET}"
            + " "*((CARD-len(r_plain)))
            + f"{CYAN}{RESET}"
        )

    print(f"{bottom}    {bottom}")

    print()

    print(f"{GRAY}{'─'*width}{RESET}")

    print(f"{YELLOW}💡 Tip:{RESET} Tell the name of your favourite movie so that Muvio Suggest Similar.")

    print(f"{GRAY}{'─'*width}{RESET}")


    while True:
        print()

        choice = input(f"{BOLD}{CYAN}🎯 Select Mode {GRAY}› {RESET}")

        if choice == "1":

            print()

            print(f"{GREEN}╭──────────────────────────────────────────────────────────────╮{RESET}")
            print(f"{GREEN}│{RESET}  ✅  Chat Mode Activated                                     {GREEN}│{RESET}")
            print(f"{GREEN}│{RESET}  ⌨️  Ready to receive your movie requests.                    {GREEN}│{RESET}")
            print(f"{GREEN}╰──────────────────────────────────────────────────────────────╯{RESET}\n")

            return False

        elif choice == "2":

            print()

            print(f"{GREEN}╭──────────────────────────────────────────────────────────────╮{RESET}")
            print(f"{GREEN}│{RESET}  ✅  Voice Mode Activated                                    {GREEN}│{RESET}")
            print(f"{GREEN}│{RESET}  🎙️  Speak naturally with Muvio AI.                           {GREEN}│{RESET}")
            print(f"{GREEN}╰──────────────────────────────────────────────────────────────╯{RESET}\n")

            return True

        else:

            print()

            print(f"{RED}╭──────────────────────────────────────────────────────────────╮{RESET}")
            print(f"{RED}│{RESET}  ❌  Invalid Selection                                       {RED}│{RESET}")
            print(f"{RED}│{RESET}  Please press 1 or 2.                                        {RED}│{RESET}")
            print(f"{RED}╰──────────────────────────────────────────────────────────────╯{RESET}\n")
