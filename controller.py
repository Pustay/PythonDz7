import model
import view


def start():
    choice = ''
   # while choice != 8:
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.information('\nФайл успешно открыт\n')
            case 2:
                model.sev_file
                view.information('\nФайл успешно сохранён\n')
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.information(f'\nКонтакт {new_contact[0]} создан\n')
            case 5:
                #clear = view.delete_contact()
                #result = model.remove_contact(clear)
                #del_name = view.delete_contact()
                del_name = view.select_contact('Введите удаляемый контакт: ')
                contact = model.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        model.delete_contact(contact[0])
                        view.information(f'\nКонтакт {contact[0][0]} удалён\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_contact('Введите изменяемый контакт: ')
                contact = model.get_contact(name)
                if contact:
                    change_contact = view.change_contact()
                    model.chenge_contact(contact[0][1], list(change_contact))
                    view.information(f'\nКонтакт {contact[0][0]} изменён\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.maiy_request()
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                view.end_program()
            case _:
                view.input_error()
                break
            
