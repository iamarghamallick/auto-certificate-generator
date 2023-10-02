import cv2
import time

list_of_name = []

def cleanup_data():
    with open("name_data.txt") as file:
        for line in file:
            # print(line.strip())
            list_of_name.append(line.strip())

def generate_certificates():
    for index, name in enumerate(list_of_name):
        print(f"Processing {index+1} / {len(list_of_name)}")
        templete = cv2.imread("certificate-template.png")
        cv2.putText(templete, name, (2000, 2000), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 120, 255), 20, cv2.LINE_AA)
        cv2.imwrite(f"generated-certificate-data/{name + '_' + str(time.time())}.png", templete)
    print("SUCCESS!")


if __name__ == "__main__":
    cleanup_data()
    generate_certificates()

