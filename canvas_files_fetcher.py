import requests
import json
import os


domain = 'https://canvas.wisc.edu'  # Your Canvas domain
access_token = '' # Your Canvas API access token
courses = '/Users/oris/Files_Fetcher/courses.txt' # Path to the file containing course IDs and output directories

course_ids = []
output_directories = []

with open(courses, 'r') as file:
    for line in file:
        # Strip whitespace and skip empty lines
        line = line.strip()
        if line:
            # Split by comma and strip whitespace from each part
            parts = line.split(',')
            if len(parts) >= 2:
                course_ids.append(parts[0].strip())
                output_directories.append(parts[1].strip())
    


print(course_ids)
print(output_directories)

# Set the Canvas API endpoint and access token

# Set up headers for API requests
headers = {
    'Authorization': f'Bearer {access_token}'
}


for course_id, output_directory in zip(course_ids, output_directories):
    print(f'------  NOW FETCHING: Course ID: {course_id} ------')
    print(f'Output Directory: {output_directory}')

    endpoint = 'https://canvas.wisc.edu/api/v1/courses/' + str(course_id) + '/files'#+'?per_page=9999'
    # Make a GET request to retrieve the list of files in the folder
    while True:
        print(endpoint)
        response = requests.get(endpoint, headers=headers)

        files = json.loads(response.text) # Get the list of files from the JSON response
        links = response.links  # Get the pagination links from the response


        # Loop through each file and download it to the output directory
        for file in files:
            # location = f'{folder_id}/{file["id"]}'
            filename = f'{file['display_name']}' # Construct the filename with the folder ID and file name
            if not os.path.exists(f'{output_directory}/{filename}'):
                url = file['url'] # Construct the URL for downloading the file
                print(f'Downloading {filename}...')
                print(f'Address: {url}')
                # Download the file to the output directory using requests library
                try:
                    response = requests.get(url, headers=headers)
                    with open(f'{output_directory}/{filename}', 'wb') as f:

                        f.write(response.content)
                except Exception as e:
                    print(f'Failed to download {filename}: {e}. Probably not available publicly.')
        try:
            endpoint = links['next']['url']  # Update the endpoint to the next page if available
        except KeyError:
            break
