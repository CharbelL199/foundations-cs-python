
#FCS50 Midterm

#this import is used for web scraping
import requests
from bs4 import BeautifulSoup
#json is used to transmit and store data
import json


#choice 1
class Tab:
    def __init__(self,title,url,content=None):
        self.title = title
        self.url = url
        self.content = content
        self.children = []
    
#for tab list
class TabManager:
    def __init__(self):
        #creating a list of tabs
        self.tabs=[]
    
    def add_tab(self,title,url,content=None,parent_index=None):
        new_tab = Tab(title, url)
        self.tabs.append(new_tab)
        print("Tab",title,"with url",url,"added successfully.")
        #geeks for geeks 
        if parent_index is not None:
            parent_tab = self.tabs[parent_index]
            parent_tab.children.append(new_tab)

    #choice 2    
    def close_tab(self,index=None):
       if index is None or not (0 <= index < len(self.tabs)):
           #if the index is none or less than 0, it will remove the last index in the list
           closed_tab = self.tabs.pop()
           print("Closed tab ",closed_tab.title,"with URL",closed_tab.url,".")
       else:
           # it will close the tab that the user enters for index
           closed_tab = self.tabs.pop(index)
           print("Closed tab ",closed_tab.title,"with URL",closed_tab.url,".")
           
    #choice 3       
    # web scraping https://www.geeksforgeeks.org/python-web-scraping-tutoria
    def display_tab_content(self, index=None):
            if not self.tabs:
                # if there is no open tab
                print("No tabs to display.")
                return
    
            if index is None or not (0 <= index < len(self.tabs)):
                # If no index provided or the index is out of range, display the content of the last opened tab
                tab_to_display = self.tabs[-1]
            else:
                #displays the index of the users input
                tab_to_display = self.tabs[index]
            
            print("Tabs:",tab_to_display.title,",URL:",tab_to_display.url)
            try:
                # Fetch the HTML content from the URL using requests
                response = requests.get(tab_to_display.url)
                response.raise_for_status()
    
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
    
                # Print the parsed HTML content
                print(soup.prettify())

            except requests.exceptions.RequestException as e:
                print("Error fetching content:",e)
                print("Content",tab_to_display.content)
                
                        
    def print_all_tabs(self, tabs=None, indent=""):
        if tabs is None:
            tabs = self.tabs

        if not tabs:
            #tabs list is empty
            print("No tabs to display.")
            return

        for tab in tabs:
            print(indent + tab.title)
            if tab.children:
                self.print_all_tabs(tab.children, indent + "  ")
                
   
    def sortingTabs(self):
        if not self.tabs:
            #tabs list is empty
            print("No tabs to sort")
            return
        
        lengthTabs = len(self.tabs)
        for i in range(lengthTabs-1):
            for j in range(0,lengthTabs-i-1):
                if self.tabs[j].title > self.tabs[j+1].title:
                    #it will swap the tabs if they are not in order
                    self.tabs[j],self.tabs[j+1]= self.tabs[j+1],self.tabs[j]
        print("Your tabs have been sorted.")
        
    
    def save_tabs_to_file(self, file_path):
        if not self.tabs:
            print("No tabs to save.")
            return

        try:
            with open(file_path, 'w') as file:
                tabs_data = []

                # Helper function to recursively gather tab data
                def gather_tab_data(tab):
                    tab_data = {
                        'title': tab.title,
                        'url': tab.url,
                        'content': getattr(tab, 'content', None),  # Include content if available
                        'children': [gather_tab_data(child) for child in tab.children]
                    }
                    return tab_data

                # Gather data for each tab in self.tabs
                for tab in self.tabs:
                    tabs_data.append(gather_tab_data(tab))

                # Write the gathered tab data to the file in JSON format
                json.dump(tabs_data, file, indent=2)

            print("Tabs saved to",file_path,".")

        except Exception as e:
            print("Error saving tabs:",e)
    
    def import_tabs(self,file_path):
        try:
            with open(file_path,'r')as file:
                #load json file, r means read
                data = json.load(file)
            print("Tabs imported successfully.")
        except Exception as e:
            print("Error importing tab",e)
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
    
    if choice == '1':
        title = input("Enter the title:")
        url = input("Enter the url:")
        tab_manager.add_tab(title, url)
    elif choice == '2':
        index_input = input("Enter the index you want to close:")
        if index_input:
            try:
                index = int(index_input)
                tab_manager.close_tab(index)
            except ValueError:
                print("Invalid Input.")
    elif choice == '3':
        index_input=input("Enter the index you want to switch to:")
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
        parent_input = input("Enter the index of parent:")
        try:
            parent_index = int(parent_input)
            title = input("Enter the title of nested:")
            content = input("Enter the url of nested:")
            tab_manager.add_tab(title, content, parent_index)
        except ValueError:
            print("Invalid input.")
    elif choice == '6':
        tab_manager.sortingTabs()
    elif choice == '7':
        file_path = input("Enter the file path to save (with type of text e.g:txt file): ")
        tab_manager.save_tabs_to_file(file_path)
    elif choice == '8':
        print()
    elif choice == '9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9 .")

