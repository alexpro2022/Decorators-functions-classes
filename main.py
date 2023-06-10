import os
import sys


if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__) + '/functions')
    from functions import (
        create_dict, github_links, hundred_requests, new_list, text_class)

    github_links.main(github_links.__doc__)
    create_dict.main(create_dict.__doc__)
    new_list.main(new_list.__doc__)
    text_class.main(text_class.__doc__)
    hundred_requests.main(hundred_requests.__doc__)
