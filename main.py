import datetime

def main():
    now = datetime.datetime.now()
    print("=" * 40)
    print(" CHÀO MƯỜNG BẠN ĐẾN VỚI GITHUB ACTIONS!")
    print(f" Thời gian hệ thống ghi nhận: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(" Bài tập Python đầu tiên đã chạy thành công!")
    print("=" * 40)

if __name__ == "__main__":
    main()
