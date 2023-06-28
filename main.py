import os
import sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__) + '/functions')
    from functions import (create_dict, github_links, hundred_requests,
                           new_list, text_class)

    github_links.main()
    create_dict.main()
    new_list.main()
    text_class.main()
    hundred_requests.main()
    