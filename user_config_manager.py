def add_setting(dict, tuple):
    key = str(tuple[0]).lower()
    value = str(tuple[1]).lower()
    
    if key in dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
                

def update_setting(dict, tuple):
    key = str(tuple[0]).lower()
    value = str(tuple[1]).lower()
    
    if key in dict:
        dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
                
def delete_setting(dict, key):
    key = key.lower()
        
    if key in dict:
        del dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    
def view_settings(dict):
    current_view = "Current User Settings:\n"
    if not dict:
        return "No settings available."
    else:
        for key, value in dict.items():
            current_view += f"{key.capitalize()}: {value}\n"
            # print(current_view)
        return current_view
               
test_settings = {}

print("--- Testing Add ---")
print(add_setting(test_settings, ("Theme", "Dark")))         # Thêm mới
print(add_setting(test_settings, ("theme", "light")))        # Trùng key
print(add_setting(test_settings, ("Notifications", "On")))   # Thêm mới

print("\n--- Testing View ---")
print(view_settings(test_settings))

print("\n--- Testing Update ---")
print(update_setting(test_settings, ("THEME", "Emerald")))   # Cập nhật thành công
print(update_setting(test_settings, ("Volume", "High")))      # Key không tồn tại

# print("\n--- Testing Delete ---")
# print(delete_setting(test_settings, "NOTIFICATIONS"))        # Xóa thành công
# print(delete_setting(test_settings, "Brightness"))           # Không tìm thấy

print("\n--- Final Settings ---")
print(view_settings(test_settings))

