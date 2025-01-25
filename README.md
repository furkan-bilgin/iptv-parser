# IPTV Parser

This script allows you to fetch remote M3U playlists, parse them, and replace placeholders in a local M3U file with the corresponding URLs from the remote playlists.

## Prerequisites

- Python 3.x
- `uv` for package management

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/iptv-parser.git
    cd iptv-parser
    ```

2. Install the required packages using `uv`:
    ```sh
    uv sync
    ```

## Usage

1. Prepare your `out.m3u` file with placeholders in the following format:
    ```
    {fetch_from:<key>:<channel_name>}
    ```

    Example:
    ```
    #EXTM3U
    #EXTINF:-1, Channel 2
    {fetch_from:remote1:Channel 1}
    #EXTINF:-1, Channel 2
    {fetch_from:remote2:Channel 2}
    ```

2. Create a `config.json` file with the URLs of the remote M3U playlists:
    ```json
    {
        "remote1": "http://example.com/remote1.m3u",
        "remote2": "http://example.com/remote2.m3u"
    }
    ```

3. Run the script:
    ```sh
    python main.py
    ```

4. The script will generate an `updated_out.m3u` file with the placeholders replaced by the actual URLs from the remote playlists.

## Example

Given the following `out.m3u` file:
```
#EXTM3U
#EXTINF:-1, Channel 1
{fetch_from:remote1:Channel 1}
#EXTINF:-1, Channel 2
{fetch_from:remote2:Channel 2}
```

And the following `config.json` file:
```json
{
    "remote1": "http://example.com/remote1.m3u",
    "remote2": "http://example.com/remote2.m3u"
}
```

If `remote1.m3u` contains:
```
#EXTM3U
#EXTINF:-1, Channel 1
http://stream1.example.com
```

And `remote2.m3u` contains:
```
#EXTM3U
#EXTINF:-1, Channel 2
http://stream2.example.com
```

The generated `updated_out.m3u` file will be:
```
#EXTM3U
#EXTINF:-1, Channel 1
http://stream1.example.com
#EXTINF:-1, Channel 2
http://stream2.example.com
```

## License

This project is licensed under the MIT License.