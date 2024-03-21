#  browsing history : prev / next 
class WebPage:
    def __init__(self,url, title) -> None:
        self.url = url 
        self.title = title

class Node: 
    def __init__(self, data) -> None:
        self.data  = data
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self) -> None:
        self.head = None
        # tag for current active node 
        self.current_page = None
    
    def visit_page(self, webpage):
        new_node = Node(webpage)
        if not self.head:
            self.head = new_node
            self.current_page = new_node
            return
        self.current_page.next = new_node
        new_node.prev = self.current_page
        self.current_page = new_node

    def display_history_forward(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data.title} - {current_node.data.url}")
            current_node = current_node.next

    def display_history_backward(self):
        current_node = self.current_page
        while current_node:
            print(f"{current_node.data.title} - {current_node.data.url}")
            current_node = current_node.prev


#  test 
history = BrowserHistory()
page1 = WebPage("www.google.com" , "Google")
page2 = WebPage("baraza.moringaschool.com" , "Mattermost Moringa")
page3 = WebPage("moringa.instructure.com" , "Canvas Moringa")
history.visit_page(page1)
history.visit_page(page2)
history.visit_page(page3)
print("Forward History")
history.display_history_forward()
print("Backward History")
history.display_history_backward()
    
