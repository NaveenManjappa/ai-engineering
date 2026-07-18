import requests
import json
import os


class OpenMeteoClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv(
            "OPEN_METEO_BASE_URL", "https://api.open-meteo.com/v1/forecast"
        )

    def get_current(self, lat, lon):
        try:
            params = {"latitude": lat, "longitude": lon, "current_weather": True}
            response = requests.get(url=self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("current_weather", {})
            # print(response.json())
            # with open("weather.json","w") as f:
            #   json.dump(response.json(),fp=f,indent=4,)
        except requests.exceptions.HTTPError as httperror:
            print(f"Error happened with api {httperror}")
            return {}

    def get_forecast(self, lat, lon, days):
        try:
            params = {
                "latitude": lat,
                "longitude": lon,
                "daily": "temperature_2m_max",
                "forecast_days": days,
            }

            response = requests.get(url=self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            result = []
            daily = data.get("daily", {})
            times = daily.get("time", [])
            temps = daily.get("temperature_2m_max", [])
            for date, temp in zip(times, temps):
                result.append(
                    {
                        "date": date,
                        "max_temp": temp,
                    }
                )
            return result
            # return response.json()
            # print(response.json())
            # with open("weather_forecast.json", "w") as f:
            #     json.dump(
            #         response.json(),
            #         fp=f,
            #         indent=4,
            #     )
        except requests.exceptions.HTTPError as httperror:
            print(f"Error happened with api {httperror}")
            return []


open_meteo_client = OpenMeteoClient()
data = open_meteo_client.get_current("51.5074", "-0.1278")
# print(data)
data = open_meteo_client.get_forecast("51.5074", "-0.1278", 3)
# print(data)
#data = open_meteo_client.get_forecast("dfd", "fsds", 3)
if not data:
    print("Could not retreive the forecast. Please check corodinates and check later")
else:
    for day in data:
        print(f"Date:{day['date']}, Max temp:{day['max_temp']}")
