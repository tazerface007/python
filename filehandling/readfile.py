"""Python Program to demonstrate file reading in python"""
import os

if __name__ == '__main__':
    try:
        if os.path.exists('hello.txt'):
            print('File Exists!')
            with open('hello.txt','r') as file:
                print(f'{file.read()}')
        else:
            raise FileNotFoundError('File not found');
    except Exception as e:
        print(f'{e}')

