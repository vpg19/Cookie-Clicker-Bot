# 🍪 Cookie Clicker Bot 🤖

An automated bot built with **Selenium** and **Python** to play the popular game [Cookie Clicker](http://orteil.dashnet.org/experiments/cookie/) optimally. The bot clicks the cookie and strategically purchases upgrades to maximize cookies per second (CPS).

## Features ✨
- **Auto-clicking** the cookie at maximum speed.
- **Smart upgrades** – Buys the most cost-effective upgrades first.
- **5-minute runtime** – Runs for 5 minutes and prints the final CPS.
- **Robust error handling** – Avoids crashes due to dynamic page changes.

## Prerequisites 📋
- Python 3.8+
- Chrome browser installed
- Selenium (`pip install selenium`)
- ChromeDriver (see [Setup](#setup))

## Setup ⚙️
1. **Install dependencies:**
   ```sh
   pip install selenium
Download ChromeDriver (matching your Chrome version):

Get it from ChromeDriver Downloads.

Place it in the project folder or add it to your PATH.

Usage 🚀
Clone the repository:

sh
git clone https://github.com/vpg19/cookie-clicker-bot.git
cd cookie-clicker-bot
Run the bot:

sh
python cookie_bot.py
Watch the bot dominate Cookie Clicker! 🍪🔥

##How It Works 🤖
Clicks the cookie as fast as possible.

Checks for affordable upgrades every 5 seconds.

Purchases the best upgrade (highest ROI first).

Runs for 5 minutes, then prints the final CPS.

##Customization ⚡
Change runtime: Modify five_min in the code (e.g., 60*10 for 10 minutes).

Adjust strategy: Edit the upgrade priority logic in the buy_upgrades() section.

##Troubleshooting 🛠️
Issue	Solution
ChromeDriver not found	Ensure it’s in your PATH or update the webdriver.Chrome() path.
ElementNotInteractable	The bot may try to click too fast. Increase delays if needed.
Game updates break the bot	Check for HTML/CSS changes in the game and update selectors.

##Contributing 🤝
Feel free to fork and improve! Some ideas:

Add GUI controls (start/stop).

Optimize upgrade logic further.

Add multiplayer bot support.

##License 📄
MIT License - Free to use and modify.
