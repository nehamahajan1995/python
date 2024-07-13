import datetime

def main():
    print(f"Script run at: {datetime.datetime.now()}")

    # Create a dummy file
    file_content = "This is a dummy file created by the script."
    with open('dummy_file.txt', 'w') as f:
        f.write(file_content)
    
    print("Dummy file 'dummy_file.txt' created.")

if __name__ == "__main__":
    main()
