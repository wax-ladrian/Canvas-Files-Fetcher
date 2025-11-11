The Python script fetches files for you from Canvas using Canvas API. It only downloads files that are not already downloaded to the output folders. It qualifies that by name alone (upgrade to be done: if file exists in Canvas with date of modification more recent than the one in the output folder, it downloads and replaces)

Go to the python script and put in your Token and your canvas domain. You must create a file where each line has the course_id, path/to/output/folder for each course, like the exemple 'courses.txt' in this repository. The course ID is the one in the link to the canvas course.

Running the python script should then fetch all your files for each course.

Things to be improved:
- it doesn't preserve the Folder structure that the Canvas Course has, it will dump all the files from 'files' of the course in the output path for the given course;
- if file exists in Canvas with date of modification more recent than the one in the output folder, it won't replace the old file with the new one since it only uses file name as criteria to know if it should fetch the file again or not;
- If a file exists in the context of an assignment but is not in the files part of canvas, the script doesn't know it exists.