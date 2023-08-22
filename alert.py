import smtplib
import csv
import time
from email.message import EmailMessage
from datetime import datetime

def alert(body, to):
    # set message contents
    msg = EmailMessage()
    msg.set_content(body)
    msg['to'] = to

    # set up user that the alert comes from
    user = "tyler.baxter.weatherbot@gmail.com"
    msg['from'] = user
    password = "moiklyiwdwsbqbei"

    # set up server to send message, send the message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def getData(file_name):
    # open data file
    file = open(file_name)
    csvReader = csv.reader(file)

    # get header information
    header = []
    header = next(csvReader)
    """ Header format:
        0  name
        1  datetime
        2  tempmax
        3  tempmin
        4  temp
        5  feelslikemax
        6  feelslikemin
        7  feelslike
        8  dew
        9  humidity
        10 precip
        11 precipprob
        12 precipcover
        13 preciptype
        14 snow
        15 snowdepth
        16 windgust
        17 windspeed
        18 winddir
        19 sealevelpressure
        20 cloudcover
        21 visibility
        22 solarradiation
        23 solarenergy
        24 uvindex
        25 severerisk
        26 sunrise
        27 sunset
        28 moonphase
        29 conditions
        30 description
        31 icon
        32 stations
    """

    # get weather information
    rows = []
    for row in csvReader:
        rows.append(row)

    # close file and return the found data
    file.close()
    return rows

if __name__ == '__main__':
    data = getData('weatherBot/pleasantonWeatherData.csv')
    # get todays date and make it the same string as in the csv file
    today = datetime.today().strftime("%Y-%m-%d")

    # initialize vars
    header = "Welcome to Weather Bot!\n"
    location = ""
    date = ""
    temp_range = ""
    hum = ""
    rain = ""
    wind_speed = ""
    cloud_cover = ""
    uvindex = ""
    sunrise = ""
    sunset = ""
    description = ""
    closer = "\n\nThanks for using Weather Bot! See you tomorrow."

    # set vars
    for day in data:
        if day[1] == today:
            location = "This forecast is for " + day[0] + " on " + day[1] + '\n\n'
            description = "You can expect " + day[30] + "\n"
            sunrise = "Today's sun will rise at approximately " + day[26][11:16:]
            sunset = " and set around " + day[27][11:16:] + "\n\n"
            temp_range = "The temperature will range today from " + day[3] + "*F to " + day[2] + "*F."
            if ((float)(day[2]) + (float)(day[3])) / 2 < 60:
                temp_range += " Don't forget your jacket!"
            elif ((float)(day[2]) + (float)(day[3])) / 2 > 80:
                temp_range += " Don't forget those sun glasses!"
            temp_range += "\n"
            hum = "There will be " + day[9] + "% humidity "
            cloud_cover = "with a cloud cover of " + day[20] + "%.\n\n"
            if (int)(day[11]) > 5:
                rain = "There is a " + day[11] + "% chance of rain today. "
                if (int)(day[11]) > 20:
                    rain += "You should bring an umbrella!"
                rain += "\n"
            if (float)(day[17]) > 10:
                wind_speed = "Today is going to be windy with a windspeed of " + day[17] + "mph\n"
            uvindex = "The UV Index for today is " + day[24] + ". "
            if (int)(day[24]) > 3:
                uvindex += "Don't forget to wear sunscreen"
                if (int)(day[24]) > 6:
                    uvindex += " and reapply in the afternoon"
                uvindex += "!"
            if (int)(day[24]) <= 1:
                uvindex += "No need for suncreen today!"
                     
    weather1 = header + location
    weather2 = description + sunrise + sunset
    weather3 = temp_range + hum + cloud_cover
    weather4 = rain + wind_speed
    weather5 = uvindex
    alert(weather1, "9253377983@vtext.com")
    time.sleep(1)
    alert(weather2, "9253377983@vtext.com")
    time.sleep(1)
    alert(weather3, "9253377983@vtext.com")
    time.sleep(1)
    alert(weather4, "9253377983@vtext.com")
    time.sleep(1)
    alert(weather5, "9253377983@vtext.com")
    time.sleep(1)
    alert(closer, "9253377983@vtext.com")
