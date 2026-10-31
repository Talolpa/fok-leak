console.print("  [cyan]0[/cyan]  Выход\n")
        choice = Prompt.ask("[bold yellow]Твой выбор[/bold yellow]",
                            choices=["1","2","3","4","5","0"], default="1")
        if choice == "1":
            v = Prompt.ask("Email")
            check_email(v)
        elif choice == "2":
            v = Prompt.ask("Телефон")
            check_phone_cmd(v)
        elif choice == "3":
            v = Prompt.ask("Пароль", password=True)
            check_password(v)
        elif choice == "4":
            v = Prompt.ask("Email или телефон")
            watch_add(con, v)
        elif choice == "5":
            watch_run(con)
        elif choice == "0":
            banner()
            console.print("[dim]Пока. Заходи в канал:[/dim]")
            console.print(f"[bold cyan]{CHANNEL}[/bold cyan]\n")
            break
        input("\n[dim]Enter чтобы вернуться...[/dim]")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    cmd = args[0]
    if cmd == "check" and len(args) > 1:
        q = args[1]
        if "@" in q:
            check_email(q)
        else:
            check_phone_cmd(q)
    elif cmd == "password" and len(args) > 1:
        check_password(args[1])
    elif cmd == "watch" and len(args) > 2 and args[1] == "add":
        con = init_db()
        watch_add(con, args[2])
    elif cmd == "watch" and len(args) == 1:
        con = init_db()
        watch_run(con)
    else:
        console.print(f"[red]Неизвестная команда: {cmd}[/red]")

if name == "main":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[dim]Прервано.[/dim]")
        sys.exit(0)
