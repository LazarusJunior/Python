# File Creation
try:
   # Open the file in write mode
   file = open("my_file.txt", "w")

   # Write some lines to the file
   file.write("This is the first line.\n")
   file.write("Second line: 42\n")
   file.write("Third line: Hello, World!\n")

except Exception as e:
   # Handle any exceptions that may occur
   print(f"An error occurred: {e}")

finally:
   # Make sure the file is closed after writing
   file.close()
   print("File creation process completed.")

# File Reading and Display
try:
   # Open the file in read mode
   file = open("my_file.txt", "r")

   # Read the contents of the file
   contents = file.read()

   # Print the contents of the file
   print("\nContents of my_file.txt:")
   print(contents)

except Exception as e:
   # Handle any exceptions that may occur
   print(f"An error occurred: {e}")

finally:
   # Make sure the file is closed after reading
   file.close()

# File Appending
try:
   # Open the file in append mode
   file = open("my_file.txt", "a")

   # Append some lines to the file
   file.write("\nFourth line: Appending text.\n")
   file.write("Fifth line: 3.14\n")
   file.write("Sixth line: Goodbye!\n")

except Exception as e:
   # Handle any exceptions that may occur
   print(f"An error occurred: {e}")

finally:
   # Make sure the file is closed after appending
   file.close()
   print("File appending process completed.")

# File Reading and Display (after appending)
try:
   # Open the file in read mode
   file = open("my_file.txt", "r")

   # Read the updated contents of the file
   contents = file.read()

   # Print the updated contents of the file
   print("\nUpdated contents of my_file.txt:")
   print(contents)

except Exception as e:
   # Handle any exceptions that may occur
   print(f"An error occurred: {e}")

finally:
   # Make sure the file is closed after reading
   file.close()
