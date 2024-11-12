# PrioritySetter
PrioritySetter is a lightweight GUI tool that lets you set custom CPU, IO, and Page priorities for specific processes. 
By modifying registry entries, PrioritySetter ensures that when these processes launch, they run with the specified priorities set by the user.




### Features
1. Set CPU Priority: Specify how much CPU attention a process should receive.
2. Set IO Priority: Control a process's disk access speed.
3. Set Page Priority: Adjust the memory page importance for a process.
4. User-Friendly Interface: Easily select and prioritize processes.
5. Automated Registry Update: Applies settings automatically in the registry, so they’re ready at process startup.


![PrioritySetter](https://github.com/user-attachments/assets/b4eadb4d-5622-4236-b8ca-d2ae066d6c72)




### Requirements
OS: Windows 10 or Higher (requires registry access)

Python version: 3.10 or higher

Libraries: Customtkinter (for GUI), winreg (for registry management)


### Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/PrioritySetter.git
cd PrioritySetter
```
Install required packages:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python prioritysetter.py
```




### Usage
1. Launch PrioritySetter.
2. Choose CPU, IO, and Memory priority levels.
3. Click Set EXE Priority to save changes to the registry.
4. When the process starts, it will automatically run with the selected priorities.
5. To uninstall priority settings click the remove button and select the exe.


### Priority Levels
1. CPU Priority: Real-time, High, Normal, Idle.
2. IO Priority: Critical, High, Normal, Low, Very Low.
3. Page Priority: Normal, Below Normal, Medium, Low, Very Low.


### License

PrioritySetter is released under the MIT License. See the [LICENSE](https://github.com/7gxycn08/PrioritySetter/blob/main/LICENSE) file for more details.
