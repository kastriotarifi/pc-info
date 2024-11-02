import socket
import platform
import psutil
import requests
import streamlit as st

def get_user_ip():
    try:
        # Get the user's external IP address
        external_ip = requests.get('https://api.ipify.org').text
        return external_ip
    except Exception as e:
        return f"Could not get IP address: {e}"

def get_system_info():
    # Note: This will show the server's system info
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "RAM": get_ram_info()
    }
    
    return system_info

def get_ram_info():
    # Get total and available RAM
    ram = psutil.virtual_memory()
    return {
        "Total": ram.total,
        "Available": ram.available,
        "Used": ram.used,
        "Percentage": ram.percent
    }

def display_info(user_ip, system_info):
    st.title("User System Information")
    st.subheader("User IP Address")
    st.write(f"External IP Address: {user_ip}")

    st.subheader("System Information (Server Side)")
    for key, value in system_info.items():
        if isinstance(value, dict):
            st.subheader(key)
            for sub_key, sub_value in value.items():
                if "Total" in sub_key or "Used" in sub_key or "Available" in sub_key:
                    st.write(f"  {sub_key}: {sub_value / (1024 ** 3):.2f} GB")
                else:
                    st.write(f"  {sub_key}: {sub_value}")
        else:
            st.write(f"{key}: {value}")

if __name__ == "__main__":
    user_ip = get_user_ip()
    system_info = get_system_info()
    display_info(user_ip, system_info)
