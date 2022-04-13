import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
choice = '1'
while choice != '0':
    print('Choose QR operation')
    print('(1) Encode')
    print('(2) Decode')
    print('(0) Exit')
    choice = input()

    if choice == '1':
        print('Enter data to encode into a QRCode')
        data = input()

        img = qrcode.make(data)

        print('Enter the absolute path to where you want to save your QRCode')
        path = input()
        print('Enter the file name')
        name = input()
        img.save(path + '/' + name + '.png')

        print('QRCode image created')
        print('')
        print('')
    elif choice == '2':
        print('Enter the absolute path to your QRCode image (including the file name and extension)')
        data = input()

        img = Image.open(data)
        result = decode(img)

        print(result[0].data)
        print('')
        print('')
    elif choice == '0':
        exit()
    else:
        print('Please enter a valid choice (try inputting a bracketed number)')
        print('')
        print('')
