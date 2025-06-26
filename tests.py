# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python_file



def test():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))  # should error
    print(run_python_file("calculator", "nonexistent.py"))  # should error
  # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
  # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
  # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # result = get_file_content("calculator", "main.py")
    # print(result)

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")

    # Uncomment to test lorem truncation manually
    # print("=> get_file_content('calculator', 'lorem.txt')  (should truncate):")
    # print(get_file_content("calculator", "lorem.txt"))
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)


if __name__ == "__main__":
    test()