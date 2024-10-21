# Import required libraries from recognizers-text
from os import times_result

from recognizers_text import Culture
from recognizers_number import recognize_number
from recognizers_date_time import recognize_datetime

def extract_data_from_text(input_text):
    try:
        #Culture to recognize
        culture = Culture.English

        #Recognize dates and times
        date_results = recognize_datetime(input_text, culture)
        time_result = recognize_datetime(input_text, culture)

        # Recognize numbers
        number_results = recognize_number(input_text, culture)

        # Initialize data holders
        extracted_data = {
            'Dates':[],
            'Times':[],
            'Numbers':[]
        }

        #Extract recognized dates and times
        for result in date_results:
            if result.resolution:
                if result.type_name == "datetimeV2.date":
                    extracted_data['Dates'].append(result.text)
                elif result.type_name == "datetimeV2.time":
                    extracted_data['Times'].append(result.text)

        #extract recognized numbers
        for result in number_results:
            if result.resolution:
                extracted_data['Numbers'].append(result.text)


        # Handle cases where no data is found
        if not extracted_data['Dates'] and not extracted_data['Times'] and not extracted_data['Numbers']:
            print("No recognizable data found.")
        else:
            # Print structured recognized data
            print("Extracted Data:")
            if extracted_data['Dates']:
                print(f"-Date(s): {', '.join(extracted_data['Dates'])}")
            if extracted_data['Times']:
                print(f"-Time(s): {', '.join(extracted_data['Times'])}")
            if extracted_data['Numbers']:
                print(f"-Number(s): {', '.join(extracted_data['Numbers'])}")
    except Exception as e:
        # Error handling for invalid input or library failures
        print(f"Error occured: {e}")

# Usage Example
input_text = "The meeting is scheduled for July 15, 2024, at 3:00 PM."
extract_data_from_text(input_text)

















