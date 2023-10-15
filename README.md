# OneDrive Always Keep on Device

Check this post first: https://support.microsoft.com/zh-cn/office/%E4%BF%AE%E5%A4%8D-macos-12-1-%E6%88%96%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E4%B8%8A%E7%9A%84-onedrive-%E6%96%87%E4%BB%B6%E6%8C%89%E9%9C%80%E9%97%AE%E9%A2%98-8c99b82e-bf6e-4bb1-a3df-d0cc5bcbff93

To summary, for OneDrive on macOS > 12.1, the "Always keep on device" will not have the ready before the `open` system call is invoked. This will cause problem when you are using services such as SMB to access the files.

This script will help you to keep the files **truly** always on device. It is essentially just walking through the directory and invoke open system call and read the first 1KB of the file to make sure it is ready periodically.

## Usage

```bash
ONEDRIVE_REFRESH_PATH=/path/to/onedrive/folder ONEDRIVE_REFRESH_INTERVAL=60 python3 main.py
```
