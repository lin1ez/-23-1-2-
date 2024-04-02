def examine_room():
    print("1. Открыть дверь")
    print("2. Заглянуть под кровать")
    print("3. Открыть ящик в углу комнаты")
    print("4. Открыть вентиляцию")
    print("5. Взглянуть на тумбочку")
    print("6. Взглянуть на статую рядом с дверью")

def examine_under_bed(player_name):
    print(f"{player_name}, вы заглянули под кровать и нашли первый артефакт: ключ от ящика.")

def examine_drawer(player_name):
    print(f"{player_name}, вы открыли ящик и нашли отмычку от двери.")

def examine_ventilation(player_name):
    print(f"{player_name}, вы пытались открыть вентиляцию, но она не поддается.")

def examine_nightstand(player_name):
    print(f"{player_name}, вы взглянули на тумбочку и нашли третий артефакт: фигурку для активации статуи.")

def activate_statue(player_name):
    print(f"{player_name}, вы активировали статую и получили второй артефакт: ключ от ящика.")

def escape(player_name):
    print(f"{player_name}, вы успешно сбежали!")


def main():
    player_name = input("Введите имя персонажа: ")

    while True:
        print(f"\n{player_name}, вы просыпаетесь в комнате и пытаетесь вспомнить свое имя.")
        examine_room()
        choice = input("Выберите действие: ")

        if choice == '1':
            examine_drawer(player_name)
            activate_statue(player_name)
            examine_ventilation(player_name)
            examine_nightstand(player_name)
            examine_drawer(player_name)
            escape(player_name)
            break
        elif choice == '2':
            examine_under_bed(player_name)
        elif choice == '3':
            examine_drawer(player_name)
        elif choice == '4':
            examine_ventilation(player_name)
        elif choice == '5':
            examine_nightstand(player_name)
        elif choice == '6':
            activate_statue(player_name)
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
