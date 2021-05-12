import file_reading_writing as fread

if __name__ == '__main__':
    print(fread.read_file('test_file'))

    print(fread.write_file('save.txt', 'save'))
    