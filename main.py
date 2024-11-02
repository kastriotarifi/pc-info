import socket
import platform
import psutil
import streamlit as st

def get_system_info():
    # Get basic system information
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "IP Address": get_ip_address(),
        "RAM": get_ram_info()
    }
    
    return system_info

def get_ip_address():
    try:
        # Get the hostname and then the IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Could not get IP address: {e}"

def get_ram_info():
    # Get total and available RAM
    ram = psutil.virtual_memory()
    return {
        "Total": ram.total,
        "Available": ram.available,
        "Used": ram.used,
        "Percentage": ram.percent
    }

def display_info(info):
    st.title("System Information")
    for key, value in info.items():
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
    system_info = get_system_info()
    display_info(system_info)
