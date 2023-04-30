import view
import text_fieldes as txt 
from classes import Contact, PhoneBook


def start_pb():
    phonebook = PhoneBook('Phonebook_class\sample.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                phonebook.open()
                view.print_info(txt.load_successful)                     
            case 2:
                phonebook.save()
                view.print_info(txt.save_successful)
            case 3:
                pb = phonebook.get()
                view.show_contacts(pb, txt.no_contact_or_file)                
            case 4:
                new_contact = view.new_contact()
                phonebook.add(new_contact)  
                view.print_info(txt.contact_saved(new_contact.name))    
            case 5:
                word = view.enter_keyword()
                result = phonebook.find(word)   
                view.show_contacts(result, txt.not_found(word))         
            case 6:
                pb = phonebook.get()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view.print_info(txt.successful_edited(edited_contact[1].name))
            case 7:
                pb = phonebook.get()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete(pb[index - 1].name)):
                        view.print_info(txt.delete_contact(phonebook.remove(index)))
            case 8:
                if phonebook.save_on_exit():
                    if view.confirm(txt.is_changed):
                        phonebook.save()
                view.print_info(txt.bye_bye)
                exit()

    
