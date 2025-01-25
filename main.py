import json
import re

import requests


def fetch_remote_m3u(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_m3u(content):
    channels = {}
    lines = content.splitlines()
    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            channel_name = lines[i].split(",")[1].strip()
            channel_url = lines[i + 1].strip()
            channels[channel_name] = channel_url
    return channels


def replace_placeholders(local_m3u, remote_m3us):
    pattern = re.compile(r"\{fetch_from:(\w+):([\w\s]+)\}")
    lines = local_m3u.splitlines()
    for i in range(len(lines)):
        match = pattern.search(lines[i])
        if match:
            key, channel_name = match.groups()
            if key in remote_m3us and channel_name in remote_m3us[key]:
                lines[i] = remote_m3us[key][channel_name]
    return "\n".join(lines)


def main():
    with open("out.m3u", "r") as file:
        local_m3u = file.read()

    with open("config.json", "r") as file:
        remote_m3u_urls = json.loads(file.read())

    remote_m3us = {}
    for key, url in remote_m3u_urls.items():
        remote_m3u_content = fetch_remote_m3u(url)
        remote_m3us[key] = parse_m3u(remote_m3u_content)

    updated_m3u = replace_placeholders(local_m3u, remote_m3us)

    with open("updated_out.m3u", "w") as file:
        file.write(updated_m3u)


if __name__ == "__main__":
    main()
