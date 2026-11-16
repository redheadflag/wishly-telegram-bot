import random
from datetime import datetime

from aiogram.utils.markdown import hide_link

from bot.bot_instance import get_wishlist_link
from bot.db.models import Item, User, Wishlist


class AddItemStages:
    ITEM_DESCRIPTION = "item_description"
    ITEM_PHOTO = "item_photo"

BIRTHDAY_PURPOSE = "День рождения"
NEW_YEAR_PURPOSE = "Новый год"
MARRIAGE_PURPOSE = "Свадьба"
FOR_FUN_PURPOSE = "Просто так"
OTHER_PURPOSE = "Другое"

WISHLIST_PURPOSES = [
    BIRTHDAY_PURPOSE,
    NEW_YEAR_PURPOSE,
    MARRIAGE_PURPOSE,
    FOR_FUN_PURPOSE,
    OTHER_PURPOSE
]

RANDOM_TITLES = {
    NEW_YEAR_PURPOSE: [
        "Ёлочные сокровища 🎄🎁",
        "Новогодний коктейль мечтаний 🤪🍸",
        "Шарики с пожеланиями ✨",
        "Подарочная Хватка 😼",
        "Мои новогодние желания 🤍",
        "Каталог новогодних капризулек 🥴",
        "Купон на новогоднее волшебство 🪄",
        "Волшебство нового года 🧙🔮",
        "Список новогодних хотелок ☃️",
        "Мои ёлочные желания 🎄",
        "Снежные фантазии ❄️",
        "Праздник к нам приходит 🎊",
        "Джингл беллз 🔔❄️"
    ],
    BIRTHDAY_PURPOSE: [
        "Когда в душе 18, то паспорт врет однозначно 😜",
        "Билет на счастливое завтра 🎟(или хотя бы на подарок)",
        "Кекси-праздник 🧁😋",
        "Пир в честь сластёныша 🎂",
        "Идеальные подарки 🎁",
        "С днём рождения меня! 🥳",
        "Мои праздничные пожелания 📄",
        "Мои хотелки на ДР 🥰",
        "Рецепт моего счастья ☺️",
    ]
}


create_wishlist = "📝 Создать вишлист"
create_wishlist_new = "Хочу свой вишлист!"
create_wishlist_inline_button = "➕ Создать вишлист"
my_wishlists = "📚 Мои вишлисты"
gift_ideas = "🎁 Идеи для подарка"
find_friends_wishlist = "🫶 Вишлисты друзей"
find_wishlist = "🔎 Найти вишлист"
settings = "⚙️ Настройки"
gifts = "🎁 Подарки"
start_event_button = "⚡Начать игру️"
add_gift_to_my_wishlist = "➕Подарок в свой вишлист"
change_title_button_text = "Изменить название"
go_back_without_changes = "🔙 Вернуться без изменений"
write_new_title = "Напишите новое название вишлиста, которое будет отображаться у всех. " \
                  "Название не должно превышать длину в 64 символа. " \
                  f"Если вы не хотите его менять, нажмите кнопку «<b>{go_back_without_changes}</b>»"
you_cant_gift_yourself = "Вы не можете подарить подарок самому себе :)"
change_date_button_text = "Изменить дату праздника"

gift_ideas_button_text = "💡Идеи для подарка"

game_has_already_started = "Похоже, что игра уже началась! Вы не можете ее начать сначала"


def start_text(user_first_name: str):
    text = f"👋 Добрый день, <b>{user_first_name}</b>!\n\nПри помощи <b>Wishly</b> вы можете создать " \
           f"свой список подарков для любого праздника или посмотреть вишлисты своих друзей и выбрать им подарок!"
    return text


not_logged_user = "Для того, чтобы продолжить, перейдите в бота!"
first_log_in = "Нажмите, чтобы продолжить"


enter_wishlist_title_1 = "Замечательно! Теперь нужно выбрать название для твоего вишлиста"

def enter_wishlist_title_2(wl_purpose: str) -> str:
    text_parts = list()
    if wl_purpose in RANDOM_TITLES.keys():
        text_parts.append(f"Чтобы не писать скучное название «{wl_purpose}», "
                          "предлагаю тебе несколько других вариантов (нажми, чтобы скопировать!):")
        text_parts.append('\n'.join([f"<code>{x}</code>" for x in random.sample(RANDOM_TITLES[wl_purpose], 5)]))
        text_parts.append("Или ты можешь придумать свое собственное название")
    text_parts.append("Выбери название и пришли его мне")
    return '\n\n'.join(text_parts)

how_old_are_you_1 = ("Прекрасно! День рождения – это замечательный праздник, "
                     "отличный повод встретиться со своими друзьями и получить от них подарки! А в этом тебе помогу я – Вишли 🥰")
how_old_are_you_2 = ("Сколько лет тебе исполняется? Твой ответ поможет мне подобрать идеальные подарки для тебя!")

enter_age_error = "Я не понимаю тебя :( Пожалуйста, повтори попытку. Сколько лет тебе исполняется?"

go_to_wishlist = "Перейти в вишлист"
delete_item = "❌ Удалить подарок из вишлиста"
item_successfully_deleted = "Подарок успешно удалён из вишлиста"
wishlist_title_too_long = "Это название слишком длинное. Пожалуйста, введите заголовок, длиной менее 64 символов"
enter_expire_date = "Последний шаг! Осталось выбрать дату твоего праздника. Выбери нужный день в календаре!"

choose_wishlist_purpose_1 = "Самое время для создания нового вишлиста!"
choose_wishlist_purpose_2 = "Для какого праздника ты хочешь создать вишлист? Для ответа используй кнопки ниже:"

enter_user_limit = ("<b>Введите максимальное количество участников тайного списка</b>"
                    "\n\nЭто может быть число от 3 до 100")


def enter_new_expire_date(current_date: datetime.date):
    return "Введите новую дату праздника в формате дд.мм.гггг" \
           f"\n\nТекущая дата: {current_date.strftime('%d.%m.%Y')}"


go_to_bot = "Перейти в меню бота"
past_date_error = "Эта дата уже в прошлом. Введите дату, которая находится в будущем" \
                  f"\n\nНапример: <i>24.11.2027</i>"
cant_parse_int_error = ("Ваше сообщение должно содержать только число участников. Например: 15."
                        "\n\nПопробуйте снова:")
incorrect_int_error = "Вы ввели некорректное число участников\n\nВведите число участников от 3 до 100:"
hide_wishlist_items = "Скрыть список подарков"
hide_gift_ideas = "Скрыть список идей для подарков"
wishlist_list_was_closed = "Список подарков был скрыт"
return_to_list_ideas = "Показать список «%s»"
no_items_in_wishlist = "Здесь пока нет ни одного подарка!"
date_value_error = "Вы ввели дату в неправильном формате. " + enter_expire_date
title_successfully_changed = "Название вишлиста успешно изменено!"
date_successfully_changed = "Дата события успешно изменена!"

add_wishlist_to_gift_ideas = "Добавить вишлист в идеи для подарков"
wishlist_successfully_added_as_gift_ideas = "Вишлист успешно стал списком идей для подарков"


def your_wishlist_is_still_empty(wishlist_title: str) -> str:
    text = f"Ваш вишлист «{wishlist_title}» до сих пор пуст! Вы не добавили ни одного подарка 😕" \
           f"\n\nДобавьте подарки и поделитесь вишлистом с друзьями и знакомыми, чтоб они знали, что вам подарить 😉"
    return text


def your_wishlist_is_full(wishlist_title: str) -> str:
    return (f"Ваш вишлист «{wishlist_title}» полон! Вы можете добавить еще несколько подарков, "
            f"чтобы новые пользователи могли их отметить и подарить вам!")


def you_havent_selected_any_item_in_wishlist(wishlist_title: str) -> str:
    return (f"Вы не отметили ни одного подарка в вишлисте вашего друга «{wishlist_title}» 😔"
            f"\n\nУ пользователя еще остались неотмеченные подарки в вишлисте. "
            f"Нажмите на кнопку снизу, чтобы посмотреть их!")


def wishlist_successfully_created(wishlist: Wishlist):
    return f"Вишлист «<b>{wishlist.title}</b>» успешно создан! " \
           f"Он доступен по ссылке:\n{get_wishlist_link(wishlist.hashcode)}" \
           "\n\nТеперь добавь подарки, которые ты хочешь получить, " \
           "а затем отправь эту ссылку друзьям или выложи её в свои соцсети, " \
           "чтобы все знали, что тебе подарить!"


add_item_to_wishlist = "➕ Добавить свой подарок"
delete_wishlist = "🗑 Удалить вишлист"
enter_item_title = "<b>Добавляем подарок в вишлист</b>" \
                   "\n\n1. Введите название подарка. Важно: оно не должно превышать 64 символа"
skip_stage = "Пропустить ⏭"
item_title_too_long = "Название подарка слишком длинное. Пожалуйста, используйте название не длиннее 64 символов"
item_description = "2. Введите <b>текстовое</b> описание вашего подарка, если это необходимо. " \
                   f"Если нет, нажмите кнопку <b>{skip_stage}</b>" \
                   "\nДлина описания не должна превышать 512 символов"

item_description_too_long = "Описание подарка слишком длинное. Пожалуйста, придумайте описание не длиннее 512 символов"
attach_item_photo = f"Отправьте фото подарка. Если фотография не требуется, нажмите кнопку {skip_stage}"
edit_wishlist_button_text = "✏️ Редактировать вишлист"


def item_info_text(title: str, description: str | None):
    text = str()
    text += f"<b>{title}</b>"
    if description:
        text += '\n\n' + description
    return text


participant_was_deleted = "Пользователь %s покинул бота и был исключен из тайного списка"

def formatted_user_string(user: User):
    return f"{user.name}" + (f" @{user.username}" if user.username else str())


reply_item_info_example = "Вот так выглядит карточка вашего подарка. Добавить его в список или удалить?"
apply_adding_to_wishlist = "✅ Добавить"
discard_adding_to_wishlist = "❌ Удалить"
creating_item_discard = "Создание карточки подарка успешно отменено"
creating_item_apply = "<b>Подарок успешно добавлен в вишлист</b>! " \
                      "Вы можете добавить еще подарок или вернуться в главное меню"
add_one_more_item = "Добавить еще один подарок 🎁"
main_menu = "В главное меню 🏠"


def wishlist_found_in_deep_link(wishlist: Wishlist, creator_user: User):
    text = f"Я обнаружил вишлист «<b>{wishlist.title}</b>» от пользователя {creator_user.name} в вашей ссылке!" \
           f"\n\nВы желаете перейти в этот вишлист?"
    return text


wishlist_not_found = "Похоже, что вишлист, к которому вы хотели перейти, не существует или был удален :("

go_to_friend_wishlist = "Перейти в вишлист друга"
your_wishlists = ("Ниже находится список вишлистов вас и ваших друзей"
                  "\n\nВаши вишлисты отмечены знаком 💎")

we_cant_delete_item = ("Похоже, что этот подарок уже кто-то выбрал в качетсве подарка, "
                       "и я не могу его удалить")

item_status = {
    'free': '🟢',
    'owned': '🔴',
}

items_list = f"<b>Чтобы показать список подарков, нажмите на кнопку ниже</b>" \
             "\nЕсли рядом с подарком стоит галочка (✅), значит эту вещь уже подарит кто-то другой"

go_back = "🔙 Назад"
i_will_gift_this_item = "Я подарю это!"
someone_else_gift_it = "Этот подарок дарит кто-то другой"
item_already_deleted = "Этот подарок уже удалён"
item_gifted = "Успешно!"
item_limit = "К сожалению, пока что вы не можете отметить больше трёх подарков в одном вишлисте 😟"

max_gifts_limit_reached = ("К сожалению, вы больше не можете добавить подарки в свой вишлист, "
                           "так как достигли лимита подарков: %i")

show_items_list = "Открыть список подарков 🎁"
my_gifts = "Мои подарки"
share_wishlist = "📨 Отправить вишлист друзьям"
hide_wishlist = "🙈 Скрыть вишлист"
wishlist_was_hide = "Вишлист был скрыт из списка"

add_to_my_wishlist = "➕ Добавить в свой вишлист"

firstly_create_wishlist = "❗️Для добавления подарка в вишлист вам нужно создайть свой первый вишлист, используя кнопку ниже"
choose_wishlist_to_add_gift_idea = "Выберите вишлист для добавления подарка:"

gift_ideas_categories = ("🎁 Идеи для подарка\n\n"
                         "В этом разделе вы можете найти подарки на любой вкус и бюджет, а потом добавить их в вишлист!"
                         "\n\nВыберите желаемую категорию:")

no_gifts_yet = ("Вы еще не выбрали ни один подарок в вишлисте! "
                "Нажмите на кнопку ниже и выберите подарок, а затем нажмите на кнопку \"Я подарю это!\"")

your_gifts_list = "Ваши подарки находятся ниже. Чтобы <b>убрать подарок из списка</b>, нажмите на него"
error_happened = "Упс! Произошла какая-то ошибка. Мы обязательно ее исправим! Попробуйте выполнить действие позже"


def gift_successfully_deleted(gift_title: str):
    return f"Подарок \"{gift_title}\" убран из вашего списка подарков"


def gift_ideas_for_this_category(category_name: str):
    return (f'Вы выбрали категорию {category_name}'
            f'\n\nНажмите на подарок, чтобы посмотреть более подробную информацию о нем')


gift_idea_successfully_added_to_wishlist = "Подарок успешно добавлен в ваш вишлист!"


def wishlist_detailed_information(wishlist: Wishlist, wishlist_owner: User):
    text = f"Вишлист «{wishlist.title}» #{wishlist.hashcode}" \
           f"\nДата события: {wishlist.expiration_date.strftime('%d.%m.%Y')}" \
           f"\nАвтор: <b>{wishlist_owner.name}</b>"
    if wishlist_owner.username:
        text += f" @{wishlist_owner.username}"
    text += f"\n\n<b>Чтобы показать список подарков, нажмите на кнопку ниже</b>" \
            "\nЕсли рядом с подарком стоит галочка (✅), значит эту вещь уже подарит кто-то другой"
    text += f"\n\nСсылка на вишлист:\n{get_wishlist_link(wishlist.hashcode)}" \
            f"\n(Отправьте эту ссылку друзьям или выложите в соцсети, чтобы все могли посмотреть этот вишлист)"
    return text


gift_limit_reached = "Лимит подарков достигнут! " \
                     "К сожалению, на данный момент вы не можете добавить больше 50 подарков в вишлист 😔"
settings_menu = "Вы находитесь в меню настроек. Здесь вы можете поменять отображаемое имя"
change_visible_name = "Изменить отображаемое имя: "


def visible_name_button_text(user_name: str):
    return change_visible_name + user_name


user_hasnt_added_any_items = "Здесь пока нет ни одного подарка ☹️"
what_you_want_to_do_with_wishlist = "Что вы хотите сделать с вишлистом? Выберите из списка"
are_you_sure_to_delete_wishlist = "Вы уверены, что хотите удалить вишлист?"
yes_delete = "Да, удалить 🗑"
no_delete = "Оставить"
delete_cancel = "Удаление вишлиста отменено"
delete_successful = "Вишлист успешно удалён"
send_new_name = "Отправьте в чат новое имя. " \
                "Оно будет отображаться у всех пользователей, " \
                "которые откроют ваши вишлисты. Длина имени должна быть от 1 до 64 символов"
name_too_long = "Имя, которое вы придумали, слишком длинное. Придумайте другое и напишите его в чат:"
name_successfully_changed = "Имя успешно изменено"
friends_wishlists_below = "Ниже находятся вишлисты ваших друзей 🤗\n\n" \
                          "Если вы хотите найти другой вишлист, нажмите на кнопку " + find_wishlist
enter_hashcode = "Введите хэш вишлиста друга.\n\nНапример: #ABCD1" \
                 "\n\nВажно: вы также можете найти вишлист друга, попросив у него ссылку и просто перейдя по ней"
cant_find_wishlist = "Я не могу найти этот вишлист. Пожалуйста, введите хэш в правильном формате " \
                     "(например #ABCD) или попросите ссылку у друга"
found_wishlist = "Мы нашли этот вишлист!"
seems_that_someone_gift_it = "Похоже, что этот подарок уже дарит кто-то другой 🫠" \
                             "\n\nВыберите другой подарок из списка"


def get_inline_query_message_text(
        title: str,
        description: str | bool = None,
        photo_link: str | bool = None
) -> str:
    text_parts = list()

    text_parts.append(
        f"<b>{title}</b>" + hide_link(photo_link)
    )
    if description:
        text_parts.append(
            "\n\n" + description
        )

    return "".join(text_parts)


def party_soon(
        wishlist: Wishlist,
        owner: User,
        items: list[Item],
) -> str:
    text = f"Привет! Совсем скоро состоится праздник у пользователя <b>{owner.name}</b> " \
           f"{('@' + owner.username) if owner.username else ''}!" \
           f"\nДата события: {wishlist.expiration_date.strftime('%d.%m.%Y')}"
    if items:
        text += " Вы уже успели приобрести подарки?" \
                "\n\nВот список ваших подарков:"
        counter = 0
        for item in items:
            counter += 1
            text += f"\n{counter}. {item.title}"
    else:
        text += "\n\n<b>Вы не выбрали ни одного подарка из вишлиста ☹️.</b> " \
                "Для того, чтобы отметить свой подарок, вам нужно выбрать его в списке, нажать на него, " \
                "а потом тыкнуть на кнопку «Я подарю это!», и только тогда все остальные увидят, " \
                "что вы подарите его! Не ленитесь нажимать кнопку, чтобы два человека не купили " \
                "один и тот же подарок 😊" \
                "Скорее переходите в вишлист и выбирайте, что подарить!"
    text += "\n\n<b>Поторопитесь, пока не поздно 😉</b>"
    return text


def wishlist_owner_party_soon(
        owner: User,
        wishlist: Wishlist,
        related_users: list,
        gifted_items: list,
        non_gifted_items: list,
):
    gifted_items_quantity = len(gifted_items)
    non_gifted_items_quantity = len(non_gifted_items)
    total_gifts_quantity = gifted_items_quantity + non_gifted_items_quantity
    gifted_total_relate_percents = round(gifted_items_quantity / total_gifts_quantity * 100)
    text = f"Привет, {owner.name}! Совсем скоро состоится Ваш праздник «{wishlist.title}» " \
           f"({wishlist.expiration_date.strftime('%d.%m.%Y')}) 🥳" \
           f"\n\nПо вашей пригласительной ссылке перешло около {len(related_users)} человек." \
           f"\nВ вишлисте было отмечено {gifted_items_quantity} из {total_gifts_quantity} подарков 🎁 " \
           f"({gifted_total_relate_percents} %)"

    if (0 <= gifted_total_relate_percents < 50 and total_gifts_quantity <= 6) \
            or (gifted_total_relate_percents <= 30 and total_gifts_quantity > 6):
        text += "\n\nОсталось много неотмеченных подарков 😟 " \
                "Попробуйте распространить ссылку среди большего количества своих друзей, " \
                "и тогда, возможно, количество ваших подарков пополнится!"
    elif gifted_total_relate_percents == 100:
        text += "\n\nВы полностью заполнили ваш вишлист, ура!!!"
    else:
        text += "\n\nВы на верном пути! Однако остались подарки, которые никто не отметил." \
                " Попробуйте распространить ссылку среди большего количества своих друзей, " \
                "и тогда, вероятно, количество ваших подарков пополнится!"
    # if gifted_items_quantity != 0:
    #     text += "\n\nПодарки, отмеченные вашими знакомыми, как те, которые они подарят:"
    #     for i, item in enumerate(gifted_items):
    #         text += f'\n{i}. {item.title}'
    #
    # if non_gifted_items_quantity != 0:
    #     text += "\n\nПодарки, которые еще никто не отметил:"
    #     for i, item in enumerate(non_gifted_items):
    #         text += f'\n{i}. {item.title}'

    text += f"\n\n🍀 Ссылка на ваш вишлист: {get_wishlist_link(wishlist.hashcode)}"
    return text
