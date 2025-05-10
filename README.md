# Website Blocker

A Python script that blocks specified websites during certain times of the day by modifying the system's hosts file.

## Features

* Blocks specified websites during scheduled times
* Works on Windows, macOS, and Linux
* Automatically flushes DNS cache after modifying hosts file

## Requirements

* Python 3.x
* `schedule` library (install with `pip install schedule`)

## Usage

1. Clone the repository: `git clone https://github.com/your-username/website-blocker.git`
2. Install the required libraries: `pip install schedule`
3. Run the script with administrator privileges:
	* On Windows: Right-click on the Python executable or script and select "Run as administrator."
	* On macOS/Linux: Run `sudo python block_websites.py` in the terminal.
4. Configure the `blocked_websites` list in `block_websites.py` to include the websites you want to block.
5. Schedule the blocking and unblocking times by modifying the `schedule.every().day.at()` calls in `block_websites.py`.

## Configuration

* `blocked_websites`: A list of websites to block. Add or remove websites as needed.
* `hosts_path`: The path to the system's hosts file. Automatically determined based on the operating system.
* `redirect_ip`: The IP address to redirect blocked websites to. Defaults to `127.0.0.1`.

## Notes

* This script requires administrator privileges to modify the hosts file.
* The script assumes that the system's hosts file is in the standard location for each operating system.
* If you're using a custom hosts file location, you'll need to modify the `hosts_path` variable accordingly.

## Contributing

Pull requests and issues are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
