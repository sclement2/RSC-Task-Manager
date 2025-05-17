def run_cli():
    from .cli_ui import run
    run()

def run_gui():
    from .gui_ui import run_gui
    run_gui()

def main():
    print("Choose Interface:")
    print("1. Text Menu (CLI)")
    print("2. GUI Menu (Tkinter)")
    choice = input("Enter choice (1/2): ")
    if choice == '2':
        run_gui()
    else:
        run_cli()

if __name__ == "__main__":
    main()
