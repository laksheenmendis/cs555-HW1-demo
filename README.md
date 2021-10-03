# cs555-HW1-demo

Lab.jpeg, Sample-text.txt and photography_guidebook.pdf are three files that we will be using for the demo. In addition, make sure the previously provided test_file.csv (~500MB) in Canvas is also available. It is the responsibility of each team to have these files available in their testing environment at the start of the demo.

edit_file.py contains an elementary program that changes a single byte within a file (from middle or end). This program may be used to simulate disk failures and test the failover and slice correction functionality in the assignment. If there is another approach you have used to simulate chunk corruption, you are free to alternatively use that during the demo.

To run the edit_file.py and change a byte in the middle of the file use the below command;

python3 edit_file.py <file_chunk_name> middle


To run the edit_file.py and change a byte in the end of the file use the below command;

python3 edit_file.py <file_chunk_name> end
