

#choice 1
class Tab:
    def __init__(self,title,url):
        self.title = title
        self.url = url
        self.children = []
    
#for tab list
class TabManager:
    def __init__(self):
        self.tabs=[]
    
    def add_tab(self,title,url):
        new_tab = Tab(title, url)
        self.tabs.append(new_tab)
        print("Tab",title,"with url",url,"added successfully.")
    
    #choice 2    
    def close_tab(self,index=None):
       if index is None or not (0 <= index < len(self.tabs)):
           closed_tab = self.tabs.pop()
           print(f"Closed tab '{closed_tab.title}' with URL '{closed_tab.url}'.")
       else:
           closed_tab = self.tabs.pop(index)
           print(f"Closed tab '{closed_tab.title}' with URL '{closed_tab.url}'.")
           
    #choice 3       
    def display_tab_content(self, index=None):
            if not self.tabs:
                print("No tabs to display.")
                return
    
            if index is None or not (0 <= index < len(self.tabs)):
                # If no index provided or the index is out of range, display the content of the last opened tab
                tab_to_display = self.tabs[-1]
            else:
                tab_to_display = self.tabs[index]
                
                         
    def print_all_tabs(self,tabs=None,indent=""):
        if tabs is None:
            tabs = self.tabs
        
        for tab in tabs:
            print(indent+tab.title)
            if tab.children:
                self.print_all_tabs(tab.children,indent + " ")

tab_manager = TabManager()    

while True:
    print("Options:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    choice = input("Enter your choice (1-9): ")
    if choice is None:
        continue
    
    if choice == '1':
        title = input("Enter the title:")
        url = input("Enter url:")
        tab_manager.add_tab(title, url)
    elif choice == '2':
        index_input = input("Enter the index:")
        if index_input:
            try:
                index = int(index_input)
                tab_manager.close_tab(index)
            except ValueError:
                print("Invalid Input.")
    elif choice == '3':
        index_input=input("Enter the index:")
        if index_input:
           try:
              index = int(index_input)
              tab_manager.display_tab_content(index)
           except ValueError:
              print("Invalid input. Please enter a valid index.")
        else:
              tab_manager.display_tab_content()
    elif choice == '4':
        tab_manager.print_all_tabs()
    elif choice == '5':
        print()
    elif choice == '6':
        print("Exiting the program.")
    elif choice == '7':
        print()
    elif choice == '8':
        print()
    elif choice == '9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9 .")

