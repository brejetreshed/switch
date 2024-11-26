
def Recent_Call_Logs(calls,k):
    if calls:
        return calls[-k:]
    else:
        return []


def Inventory_Shelf_Arrangement(book_ids):
    books_stack = []
    for book in book_ids:
        books_stack.append(book)
    reversed_books = []
    while books_stack:
        reversed_books.append(books_stack.pop())
    return reversed_books


def Undo_Feature_in_Text_Editor(actions, undo_steps):
    if(undo_steps <= len(actions)):
        return actions[:-undo_steps]
    else:
        return []
    

def Daily_Temperature_Analysis(daily_temp):
    n = len(daily_temp)
    result = n*[0] 
    stack = []

    for current_day in range(n):

        while stack and daily_temp[current_day] > daily_temp[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = current_day - previous_day

        stack.append(current_day)

    return result
    

def Ticket_Counter_Simulation(customers):
    served_customers = []
    while customers:
        served_customers.append(customers.pop(0))  
    return served_customers
    

def Family_Tree_Search(tree, root, target_name):
    from collections import deque

    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        current = queue.popleft()
        if current == target_name:  # Check if the current node matches the target
            return True
        queue.extend(tree.get(current, []))  # Add children to the queue

    return False

def Directory_Size_Calculation(node):
    for name in node:
        size, children = node[name]
        total_size = size
        for child in children:
            total_size += Directory_Size_Calculation(child)
    return total_size


from collections import deque
def Check_Tree_Symmetry(root):
    if not root:
        return True 
    
    #check pairs!
    queue = deque([(root.left, root.right)])  

    while queue:
        t1, t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2 or t1.value != t2.value:
            return False
        queue.append((t1.left, t2.right))  
        queue.append((t1.right, t2.left))  

    return True





