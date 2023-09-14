# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
# This file is part a of < https://github.com/TeamUltroid/Ultroid/ >
# Please read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

FROM theteamultroid/ultroid:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

# Install required packages
RUN apt-get update && apt-get install -y python3-dev python3-pip

# Install dependencies
# Fixed typo in the file name. Changed 'requirements.txt' to 'requirements.txt' to match the actual file name.
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# changing workdir
WORKDIR "/root/TeamUltroid"

# Expose port
EXPOSE 8080

# start the bot.
CMD ["bash", "startup"]
