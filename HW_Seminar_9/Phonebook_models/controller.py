import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
                pass
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                request = view.enter_keyword()
                result = model.find_contact(request)
                view.show_contacts(result, txt.no_result)
            case 6:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    model.edit_contact(edited_contact)
                    view.print_info(
                        txt.successful_edited(edited_contact[1].get("name"))
                    )
            case 7:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete(pb[index - 1].get("name"))):
                        view.print_info(txt.delete_contact(model.remove_contact(index)))
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()
