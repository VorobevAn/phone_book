import model
import view

def start():
    user_chois =0
    while user_chois != 8:
         user_chois = view.menu()

         match user_chois:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contact(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                change = view.change_contact()
                answer = model.change_phone_book(change)
                view.changeable_contact(answer)
                new_contakt = list(view.new_contact())
                model.change_contact_phone_book(new_contakt)

            case 6:
                neim = view.dell_contact()
                answer = model.dell_contact(neim)
                view.dellit_contakt(answer)

            case 7:
                secrch = view.find_contact()
                result = model.search_contact(secrch)
                view.show_contact(result)


