from random import shuffle


def create_data_from_txt(
        save_to: str,
        convert_from: str,
        list_name: str = "list_of",
        count_data: int = 300
) -> None:
    with open(save_to, "w+") as titles:
        with open(f"{convert_from}", 'r') as title_list:
            titles.write(f"{list_name} = [")
            data_list = title_list.readlines()
            shuffle(data_list)
            data_list = data_list[:count_data]
            for title in data_list:
                title = title.split("\n")[0]
                title = f'"{title}",'
                titles.write(title)
            titles.write("]")
