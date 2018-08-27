import fileinput

HEADER_SYMBOL = '*'
ITEM_SYMBOL = '.'
header_prefix_list = []

def process_headers(header_line):
    header_txt = ' '.join(header_line.split()[1:])
    header_line_prefix = header_line.split()[0]
    global header_prefix_list
    len_curr_header_prefix_list = header_line_prefix.count(HEADER_SYMBOL)
    len_prev_header_prefix_list = len(header_prefix_list)
    if len_prev_header_prefix_list  == len_curr_header_prefix_list:
        header_prefix_list[-1] += 1
    elif len_prev_header_prefix_list > len_curr_header_prefix_list:
        header_prefix_list = header_prefix_list[0:len_curr_header_prefix_list]
        header_prefix_list[-1] += 1
    else:
        header_prefix_list.append(1)
    header_prefix = '.'.join(map(str, header_prefix_list))
    print('{0} {1}'.format(header_prefix, header_txt))


def process_sub_items(sub_items):
    i = 0
    len_sub_items = len(sub_items)
    while i < len_sub_items:
        if not sub_items[i].startswith(ITEM_SYMBOL):
            curr_txt = sub_items[i]
            item_prefix = ' '
            print('{0}{1} {2}'.format(' ' * len_curr_prefix, item_prefix, curr_txt))
        else:
            curr_prefix = sub_items[i].split()[0]
            next_prefix = sub_items[i+1].split()[0] if i+1 < len_sub_items else ''
            len_curr_prefix = len(curr_prefix)
            len_next_prefix = len(next_prefix) if next_prefix else 0
            curr_txt = ' '.join(sub_items[i].split()[1:])
            item_prefix = '+' if len_next_prefix > len_curr_prefix else '-'
            print('{0}{1} {2}'.format(' '*len_curr_prefix, item_prefix , curr_txt))
        i += 1


sub_items = []
for line in fileinput.input():
    current_line = line.strip()
    if not current_line:
        continue
    # print('<< : {0}'.format(current_line))
    if current_line.startswith('*'):
        process_sub_items(sub_items)
        sub_items = []
        process_headers(current_line)
    else:
        sub_items.append(current_line)
process_sub_items(sub_items)
