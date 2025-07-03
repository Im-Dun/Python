import json
danh_sach_benh_nhan = {}
def benh_nhan_moi():
    try:
        MaBN = input("Nhập mã bệnh nhân: ")
        if MaBN in danh_sach_benh_nhan:
            print("Mã bệnh nhân đã tồn tại. Vui lòng nhập mã khác.")
            return

        TenBN = input("Nhập tên bệnh nhân: ")
        NgaySinh = input("Nhập ngày sinh (YYYY-MM-DD): ")
        GioiTinh = input("Nhập giới tính (Nam/Nữ): ")
        DiaChi = input("Nhập địa chỉ: ")
        Tuoi = int(input("Nhập tuổi: "))
        SDT = input("Nhập số điện thoại: ")

        benh_nhan = {
            "TenBN": TenBN,
            "NgaySinh": NgaySinh,
            "GioiTinh": GioiTinh,
            "DiaChi": DiaChi,
            "Tuoi": Tuoi,
            "SDT": SDT
        }
        danh_sach_benh_nhan[MaBN] = benh_nhan
        print("Bệnh nhân đã được thêm thành công.")
    except ValueError:
        print("Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng kiểm tra lại thông tin.")

def sua_thong_tin_benh_nhan():
    try:
        MaBN = input("Nhập mã bệnh nhân cần sửa: ")
        if MaBN not in danh_sach_benh_nhan:
            print("Không tìm thấy bệnh nhân với mã đã nhập.")
            return
        TenBN = input("Nhập tên mới: ")
        NgaySinh = input("Nhập ngày sinh mới (YYYY-MM-DD): ")
        GioiTinh = input("Nhập giới tính mới (Nam/Nữ): ")
        DiaChi = input("Nhập địa chỉ mới: ")
        Tuoi = int(input("Nhập tuổi mới: "))
        SDT = input("Nhập số điện thoại mới: ")
        danh_sach_benh_nhan[MaBN] = {
            "TenBN": TenBN,
            "NgaySinh": NgaySinh,
            "GioiTinh": GioiTinh,
            "DiaChi": DiaChi,
            "Tuoi": Tuoi,
            "SDT": SDT
        }
        print("Thông tin bệnh nhân đã được cập nhật.")
    except ValueError:
        print("Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng kiểm tra lại thông tin.")

def xoa_benh_nhan():
    try:
        MaBN = input("Nhập mã bệnh nhân cần xóa: ")
        if MaBN in danh_sach_benh_nhan:
            del danh_sach_benh_nhan[MaBN]
            print("Bệnh nhân đã được xóa thành công.")
        else:
            print("Không tìm thấy bệnh nhân với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_benh_nhan_theo_ma():
    try:
        MaBN = input("Nhập mã bệnh nhân cần tìm: ")
        if MaBN in danh_sach_benh_nhan:
            print(f"Tìm thấy bệnh nhân: {danh_sach_benh_nhan[MaBN]}")
        else:
            print("Không tìm thấy bệnh nhân với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_benh_nhan_theo_ten():
    try:
        TenBN = input("Nhập tên bệnh nhân cần tìm: ")
        for benh_nhan in danh_sach_benh_nhan.values():
            if benh_nhan["TenBN"].lower() == TenBN.lower():
                print(f"Tìm thấy bệnh nhân: {benh_nhan}")
                return
        print("Không tìm thấy bệnh nhân với tên đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def hien_thi_danh_sach_benh_nhan():
    try:
        if danh_sach_benh_nhan:
            print("Danh sách bệnh nhân:")
            for MaBN, benh_nhan in danh_sach_benh_nhan.items():
                print(f"Mã BN: {MaBN}, Thông tin: {benh_nhan}")
        else:
            print("Danh sách bệnh nhân trống.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def loc_benh_nhan_theo_do_tuoi():
    try:
        tuoi = int(input("Nhập độ tuổi cần lọc: "))
        danh_sach_loc = [benh_nhan for benh_nhan in danh_sach_benh_nhan.values() if benh_nhan["Tuoi"] == tuoi]
        if danh_sach_loc:
            print("Danh sách bệnh nhân theo độ tuổi:")
            for benh_nhan in danh_sach_loc:
                print(benh_nhan)
        else:
            print("Không tìm thấy bệnh nhân với độ tuổi đã nhập.")
    except ValueError:
        print("Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng kiểm tra lại thông tin.")

def loc_benh_nhan_theo_gioi_tinh():
    try:
        gioi_tinh = input("Nhập giới tính cần lọc (Nam/Nữ): ")
        danh_sach_loc = [benh_nhan for benh_nhan in danh_sach_benh_nhan.values() if benh_nhan["GioiTinh"].lower() == gioi_tinh.lower()]
        if danh_sach_loc:
            print("Danh sách bệnh nhân theo giới tính:")
            for benh_nhan in danh_sach_loc:
                print(benh_nhan)
        else:
            print("Không tìm thấy bệnh nhân với giới tính đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def dem_tong_so_benh_nhan():
    try:
        print(f"Tổng số bệnh nhân: {len(danh_sach_benh_nhan)}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def xuat_danh_sach_benh_nhan_ra_json():
    try:
        with open("./btl/benhnhan.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_benh_nhan, f, ensure_ascii=False, indent=4)
        print("Danh sách bệnh nhân đã được xuất ra file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def nhap_danh_sach_benh_nhan_tu_json():
    try:
        with open("./btl/benhnhan.json", "r", encoding="utf-8") as f:
            global danh_sach_benh_nhan
            danh_sach_benh_nhan = json.load(f)
        print("Danh sách bệnh nhân đã được nhập từ file JSON.")
    except FileNotFoundError:
        print("File JSON không tồn tại.")
    except json.JSONDecodeError:
        print("Đã xảy ra lỗi khi đọc file JSON. Vui lòng kiểm tra định dạng file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def ghi_danh_sach_benh_nhan():
    try:
        with open("./btl/benhnhan.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_benh_nhan, f, ensure_ascii=False, indent=4)
        print("Danh sách bệnh nhân đã được ghi vào file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

danh_sach_bac_si = {}
def them_bac_si_moi():
    try:
        MaBS = input("Nhập mã bác sĩ: ")
        if MaBS in danh_sach_bac_si:
            print("Mã bác sĩ đã tồn tại. Vui lòng nhập mã khác.")
            return
        TenBS = input("Nhập tên bác sĩ: ")
        ChuyenKhoa = input("Nhập chuyên khoa: ")
        GioiTinh = input("Nhập giới tính (Nam/Nữ): ")
        SDT = input("Nhập số điện thoại: ")
        bac_si = {
            "TenBS": TenBS,
            "ChuyenKhoa": ChuyenKhoa,
            "GioiTinh": GioiTinh,
            "SDT": SDT
        }
        danh_sach_bac_si[MaBS] = bac_si
        print("Bác sĩ đã được thêm thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def sua_thong_tin_bac_si():
    try:
        MaBS = input("Nhập mã bác sĩ cần sửa: ")
        if MaBS not in danh_sach_bac_si:
            print("Không tìm thấy bác sĩ với mã đã nhập.")
            return
        TenBS = input("Nhập tên mới: ")
        ChuyenKhoa = input("Nhập chuyên khoa mới: ")
        GioiTinh = input("Nhập giới tính mới (Nam/Nữ): ")
        SDT = input("Nhập số điện thoại mới: ")
        danh_sach_bac_si[MaBS] = {
            "TenBS": TenBS,
            "ChuyenKhoa": ChuyenKhoa,
            "GioiTinh": GioiTinh,
            "SDT": SDT
        }
        print("Thông tin bác sĩ đã được cập nhật.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def xoa_bac_si():
    try:
        MaBS = input("Nhập mã bác sĩ cần xóa: ")
        if MaBS in danh_sach_bac_si:
            del danh_sach_bac_si[MaBS]
            print("Bác sĩ đã được xóa thành công.")
        else:
            print("Không tìm thấy bác sĩ với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_bac_si_theo_ma():
    try:
        MaBS = input("Nhập mã bác sĩ cần tìm: ")
        if MaBS in danh_sach_bac_si:
            print(f"Tìm thấy bác sĩ: {danh_sach_bac_si[MaBS]}")
        else:
            print("Không tìm thấy bác sĩ với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_bac_si_theo_chuyen_khoa():
    try:
        ChuyenKhoa = input("Nhập chuyên khoa cần tìm: ")
        found = False
        for bs in danh_sach_bac_si.values():
            if bs["ChuyenKhoa"].lower() == ChuyenKhoa.lower():
                print(f"Tìm thấy bác sĩ: {bs}")
                found = True
        if not found:
            print("Không tìm thấy bác sĩ với chuyên khoa đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def hien_thi_danh_sach_bac_si():
    try:
        if danh_sach_bac_si:
            print("Danh sách bác sĩ:")
            for MaBS, bs in danh_sach_bac_si.items():
                print(f"Mã BS: {MaBS}, Thông tin: {bs}")
        else:
            print("Danh sách bác sĩ trống.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def loc_bac_si_theo_gioi_tinh():
    try:
        gioi_tinh = input("Nhập giới tính cần lọc (Nam/Nữ): ")
        ds = [bs for bs in danh_sach_bac_si.values() if bs["GioiTinh"].lower() == gioi_tinh.lower()]
        if ds:
            print("Danh sách bác sĩ theo giới tính:")
            for bs in ds:
                print(bs)
        else:
            print("Không tìm thấy bác sĩ với giới tính đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def dem_so_bac_si_theo_chuyen_khoa():
    try:
        chuyen_khoa = input("Nhập chuyên khoa cần đếm: ")
        dem = sum(1 for bs in danh_sach_bac_si.values() if bs["ChuyenKhoa"].lower() == chuyen_khoa.lower())
        print(f"Số bác sĩ theo chuyên khoa {chuyen_khoa}: {dem}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def xuat_danh_sach_bac_si_ra_json():
    try:
        with open("btl/bacsi.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_bac_si, f, ensure_ascii=False, indent=4)
        print("Danh sách bác sĩ đã được xuất ra file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def nhap_danh_sach_bac_si_tu_json():
    try:
        with open("btl/bacsi.json", "r", encoding="utf-8") as f:
            global danh_sach_bac_si
            danh_sach_bac_si = json.load(f)
        print("Danh sách bác sĩ đã được nhập từ file JSON.")
    except FileNotFoundError:
        print("File JSON không tồn tại.")
    except json.JSONDecodeError:
        print("Đã xảy ra lỗi khi đọc file JSON. Vui lòng kiểm tra định dạng file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def ghi_danh_sach_bac_si():
    try:
        with open("btl/bacsi.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_bac_si, f, ensure_ascii=False, indent=4)
        print("Danh sách bác sĩ đã được ghi vào file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

danh_sach_lich_kham = {}
def tao_lich_kham_moi():
    try:
        MaLK = input("Nhập mã lịch khám: ")
        if MaLK in danh_sach_lich_kham:
            print("Mã lịch khám đã tồn tại. Vui lòng nhập mã khác.")
            return

        MaBN = input("Nhập mã bệnh nhân: ")
        if MaBN not in danh_sach_benh_nhan:
            print("Mã bệnh nhân không tồn tại. Vui lòng nhập mã khác.")
            return

        MaBS = input("Nhập mã bác sĩ: ")
        NgayKham = input("Nhập ngày khám (YYYY-MM-DD): ")
        GioKham = input("Nhập giờ khám (HH:MM): ")

        lich_kham = {
            "MaBN": MaBN,
            "MaBS": MaBS,
            "NgayKham": NgayKham,
            "GioKham": GioKham
        }
        danh_sach_lich_kham[MaLK] = lich_kham
        print("Lịch khám đã được tạo thành công.")
    except ValueError:
        print("Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng kiểm tra lại thông tin.")

def sua_lich_kham():
    try:
        MaLK = input("Nhập mã lịch khám cần sửa: ")
        if MaLK not in danh_sach_lich_kham:
            print("Không tìm thấy lịch khám với mã đã nhập.")
            return

        MaBN = input("Nhập mã bệnh nhân mới: ")
        if MaBN not in danh_sach_benh_nhan:
            print("Mã bệnh nhân không tồn tại. Vui lòng nhập mã khác.")
            return
        MaBS = input("Nhập mã bác sĩ mới: ")
        if MaBS not in danh_sach_benh_nhan:
            print("Mã bác sĩ không tồn tại. Vui lòng nhập mã khác.")
            return

        NgayKham = input("Nhập ngày khám (YYYY-MM-DD): ")
        GioKham = input("Nhập giờ khám (HH:MM): ")
        Phong = input("Nhập phòng khám: ")

        lich_kham = {
            "MaBN": MaBN,
            "MaBS": MaBS,
            "NgayKham": NgayKham,
            "GioKham": GioKham,
            "Phong": Phong
        }
        danh_sach_lich_kham[MaLK] = lich_kham
        print("Lịch khám đã được cập nhật thành công.")
    except ValueError:
        print("Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng kiểm tra lại thông tin.")

def huy_lich_kham():
    try:
        MaLK = input("Nhập mã lịch khám cần hủy: ")
        if MaLK in danh_sach_lich_kham:
            del danh_sach_lich_kham[MaLK]
            print("Lịch khám đã được hủy thành công.")
        else:
            print("Không tìm thấy lịch khám với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_lich_kham_theo_ma_benh_nhan():
    try:
        MaBN = input("Nhập mã bệnh nhân cần tìm lịch khám: ")
        lich_kham = [lk for lk in danh_sach_lich_kham.values() if lk["MaBN"] == MaBN]
        if lich_kham:
            print("Danh sách lịch khám của bệnh nhân:")
            for lk in lich_kham:
                print(lk)
        else:
            print("Không tìm thấy lịch khám cho bệnh nhân với mã đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_lich_kham_theo_ngay():
    try:
        NgayKham = input("Nhập ngày khám cần tìm (YYYY-MM-DD): ")
        lich_kham = [lk for lk in danh_sach_lich_kham.values() if lk["NgayKham"] == NgayKham]
        if lich_kham:
            print("Danh sách lịch khám theo ngày:")
            for lk in lich_kham:
                print(lk)
        else:
            print("Không tìm thấy lịch khám cho ngày đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def hien_thi_lich_kham_trong_tuan():
    try:
        from datetime import datetime, timedelta
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        lich_kham_tuan = [lk for lk in danh_sach_lich_kham.values() if start_of_week <= datetime.strptime(lk["NgayKham"], "%Y-%m-%d") <= end_of_week]
        
        if lich_kham_tuan:
            print("Danh sách lịch khám trong tuần:")
            for lk in lich_kham_tuan:
                print(lk)
        else:
            print("Không có lịch khám trong tuần này.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def thong_ke_lich_kham_theo_ngay():
    try:
        NgayKham = input("Nhập ngày cần thống kê (YYYY-MM-DD): ")
        lich_kham = [lk for lk in danh_sach_lich_kham.values() if lk["NgayKham"] == NgayKham]
        if lich_kham:
            print(f"Tổng số lịch khám trong ngày {NgayKham}: {len(lich_kham)}")
            for lk in lich_kham:
                print(lk)
        else:
            print("Không có lịch khám trong ngày đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def luu_lich_kham_ra_json():
    try:
        with open("btl/lichkham.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_lich_kham, f, ensure_ascii=False, indent=4)
        print("Danh sách lịch khám đã được lưu ra file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def nhap_danh_sach_lich_kham_tu_json():
    try:
        with open("btl/lichkham.json", "r", encoding="utf-8") as f:
            global danh_sach_lich_kham
            danh_sach_lich_kham = json.load(f)
        print("Danh sách lịch khám đã được nhập từ file JSON.")
    except FileNotFoundError:
        print("File JSON không tồn tại.")
    except json.JSONDecodeError:
        print("Đã xảy ra lỗi khi đọc file JSON. Vui lòng kiểm tra định dạng file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def doc_lich_kham_tu_json():
    try:
        with open("btl/lichkham.json", "r", encoding="utf-8") as f:
            lich_kham = json.load(f)
            print("Danh sách lịch khám đã được đọc từ file JSON:")
            for lk in lich_kham.values():
                print(lk)
    except FileNotFoundError:
        print("File JSON không tồn tại.")
    except json.JSONDecodeError:
        print("Đã xảy ra lỗi khi đọc file JSON. Vui lòng kiểm tra định dạng file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def kiem_tra_trung_lich_bac_si():
    try:
        lich_kham = {}
        for lk in danh_sach_lich_kham.values():
            if lk["MaBS"] in lich_kham:
                lich_kham[lk["MaBS"]].append(lk)
            else:
                lich_kham[lk["MaBS"]] = [lk]

        for ma_bs, lich in lich_kham.items():
            if len(lich) > 1:
                print(f"Bác sĩ {ma_bs} có lịch khám trùng lặp:")
                for lk in lich:
                    print(lk)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def ghi_danh_sach_lich_kham():
    try:
        with open("btl/lichkham.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_lich_kham, f, ensure_ascii=False, indent=4)
        print("Danh sách lịch khám đã được ghi vào file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

danh_sach_don_thuoc = {}
def tao_don_thuoc_moi():
    try:
        MaDT = input("Nhập mã đơn thuốc: ")
        if MaDT in danh_sach_don_thuoc:
            print("Mã đơn thuốc đã tồn tại. Vui lòng nhập mã khác.")
            return
        MaBN = input("Nhập mã bệnh nhân: ")
        if MaBN not in danh_sach_benh_nhan:
            print("Mã bệnh nhân không tồn tại.")
            return
        NgayKe = input("Nhập ngày kê đơn (YYYY-MM-DD): ")
        danh_sach_don_thuoc[MaDT] = {
            "MaBN": MaBN,
            "NgayKe": NgayKe,
            "Thuoc": []
        }
        print("Đơn thuốc đã được tạo thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def them_thuoc_vao_don():
    try:
        MaDT = input("Nhập mã đơn thuốc cần thêm thuốc: ")
        if MaDT not in danh_sach_don_thuoc:
            print("Không tìm thấy đơn thuốc với mã đã nhập.")
            return
        TenThuoc = input("Nhập tên thuốc: ")
        SoLuong = int(input("Nhập số lượng: "))
        DonGia = float(input("Nhập đơn giá: "))
        thuoc = {
            "TenThuoc": TenThuoc,
            "SoLuong": SoLuong,
            "DonGia": DonGia
        }
        danh_sach_don_thuoc[MaDT]["Thuoc"].append(thuoc)
        print("Thuốc đã được thêm vào đơn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def xoa_thuoc_khoi_don():
    try:
        MaDT = input("Nhập mã đơn thuốc cần xóa thuốc: ")
        if MaDT not in danh_sach_don_thuoc:
            print("Không tìm thấy đơn thuốc với mã đã nhập.")
            return
        TenThuoc = input("Nhập tên thuốc cần xóa: ")
        thuoc_list = danh_sach_don_thuoc[MaDT]["Thuoc"]
        for thuoc in thuoc_list:
            if thuoc["TenThuoc"].lower() == TenThuoc.lower():
                thuoc_list.remove(thuoc)
                print("Thuốc đã được xóa khỏi đơn.")
                return
        print("Không tìm thấy thuốc với tên đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def hien_thi_don_thuoc_theo_benh_nhan():
    try:
        MaBN = input("Nhập mã bệnh nhân cần xem đơn thuốc: ")
        found = False
        for MaDT, don in danh_sach_don_thuoc.items():
            if don["MaBN"] == MaBN:
                print(f"Đơn thuốc {MaDT}: {don}")
                found = True
        if not found:
            print("Không tìm thấy đơn thuốc với mã bệnh nhân đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def luu_don_thuoc_ra_json():
    try:
        with open("btl/donthuoc.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_don_thuoc, f, ensure_ascii=False, indent=4)
        print("Đơn thuốc đã được lưu ra file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def nhap_danh_sach_don_thuoc_tu_json():
    try:
        with open("btl/donthuoc.json", "r", encoding="utf-8") as f:
            global danh_sach_don_thuoc
            danh_sach_don_thuoc = json.load(f)
        print("Danh sách đơn thuốc đã được nhập từ file JSON.")
    except FileNotFoundError:
        print("File JSON không tồn tại.")
    except json.JSONDecodeError:
        print("Đã xảy ra lỗi khi đọc file JSON. Vui lòng kiểm tra định dạng file.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tinh_tong_tien_thuoc_trong_don():
    try:
        MaDT = input("Nhập mã đơn thuốc cần tính tổng tiền: ")
        if MaDT not in danh_sach_don_thuoc:
            print("Không tìm thấy đơn thuốc với mã đã nhập.")
            return
        tong = sum(thuoc["SoLuong"] * thuoc["DonGia"] for thuoc in danh_sach_don_thuoc[MaDT]["Thuoc"])
        print(f"Tổng tiền thuốc trong đơn {MaDT}: {tong} VND")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_benh_nhan_co_don_thuoc_nhieu_nhat():
    try:
        if not danh_sach_don_thuoc:
            print("Danh sách đơn thuốc trống.")
            return
        max_ma = max(danh_sach_don_thuoc, key=lambda k: len(danh_sach_don_thuoc[k]["Thuoc"]))
        max_don = danh_sach_don_thuoc[max_ma]
        print(f"Bệnh nhân có đơn thuốc nhiều nhất: {max_don['MaBN']} với {len(max_don['Thuoc'])} loại thuốc.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def kiem_tra_thuoc_trung_lap_trong_don():
    try:
        MaDT = input("Nhập mã đơn thuốc cần kiểm tra: ")
        if MaDT not in danh_sach_don_thuoc:
            print("Không tìm thấy đơn thuốc với mã đã nhập.")
            return
        seen = set()
        for thuoc in danh_sach_don_thuoc[MaDT]["Thuoc"]:
            ten = thuoc["TenThuoc"].lower()
            if ten in seen:
                print(f"Thuốc {thuoc['TenThuoc']} bị trùng lặp trong đơn.")
                return
            seen.add(ten)
        print("Không có thuốc trùng lặp trong đơn thuốc.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def thong_ke_thuoc_duoc_ke_nhieu_nhat():
    try:
        thuoc_count = {}
        for don in danh_sach_don_thuoc.values():
            for thuoc in don["Thuoc"]:
                ten = thuoc["TenThuoc"]
                thuoc_count[ten] = thuoc_count.get(ten, 0) + thuoc["SoLuong"]
        if not thuoc_count:
            print("Không có thuốc nào được kê.")
            return
        max_thuoc = max(thuoc_count, key=thuoc_count.get)
        print(f"Thuốc được kê nhiều nhất: {max_thuoc} với số lượng {thuoc_count[max_thuoc]}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def tim_don_thuoc_theo_ngay_ke():
    try:
        NgayKe = input("Nhập ngày kê đơn cần tìm (YYYY-MM-DD): ")
        found = False
        for MaDT, don in danh_sach_don_thuoc.items():
            if don["NgayKe"] == NgayKe:
                print(f"Đơn thuốc {MaDT}: {don}")
                found = True
        if not found:
            print("Không tìm thấy đơn thuốc với ngày đã nhập.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def ghi_danh_sach_don_thuoc():
    try:
        with open("btl/donthuoc.json", "w", encoding="utf-8") as f:
            json.dump(danh_sach_don_thuoc, f, ensure_ascii=False, indent=4)
        print("Danh sách đơn thuốc đã được ghi vào file JSON.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def menu():
    print("\n====== MENU QUẢN LÝ KHÁM CHỮA BỆNH ======")
    print("\n Bệnh nhân:")
    print("1.  Thêm bệnh nhân mới")
    print("2.  Sửa thông tin bệnh nhân")
    print("3.  Xóa bệnh nhân")
    print("4.  Tìm bệnh nhân theo mã")
    print("5.  Tìm bệnh nhân theo tên")
    print("6.  Hiển thị danh sách bệnh nhân")
    print("7.  Lọc bệnh nhân theo độ tuổi")
    print("8.  Lọc bệnh nhân theo giới tính")
    print("9.  Đếm tổng số bệnh nhân")
    print("10. Xuất danh sách bệnh nhân ra file JSON")
    print("11. Nhập danh sách bệnh nhân từ file JSON")
    print("12. Ghi danh sách bệnh nhân vào file JSON")
    
    print("\n Bác sĩ:")
    print("13. Thêm bác sĩ mới")
    print("14. Sửa thông tin bác sĩ")
    print("15. Xóa bác sĩ")
    print("16. Tìm bác sĩ theo mã")
    print("17. Tìm bác sĩ theo chuyên khoa")
    print("18. Hiển thị danh sách bác sĩ")
    print("19. Lọc bác sĩ theo giới tính")
    print("20. Đếm số bác sĩ theo chuyên khoa")
    print("21. Xuất danh sách bác sĩ ra file JSON")
    print("22. Nhập danh sách bác sĩ từ file JSON")
    print("23. Ghi danh sách bác sĩ vào file JSON")

    print("\n Lịch khám:")
    print("24. Tạo lịch khám mới")
    print("25. Sửa lịch khám")
    print("26. Hủy lịch khám")
    print("27. Tìm lịch khám theo mã bệnh nhân")
    print("28. Tìm lịch khám theo ngày")
    print("29. Hiển thị lịch khám trong tuần")
    print("30. Thống kê lịch khám theo ngày")
    print("31. Lưu lịch khám ra file JSON")
    print("32. Nhập danh sách lịch khám từ file JSON")
    print("33. Ghi danh sách lịch khám vào file JSON")
    print("34. Đọc lịch khám từ file JSON")
    print("35. Kiểm tra trùng lịch giữa các bác sĩ")

    print("\n Đơn thuốc:")
    print("36. Tạo đơn thuốc mới")
    print("37. Thêm thuốc vào đơn")
    print("38. Xóa thuốc khỏi đơn")
    print("39. Hiển thị đơn thuốc theo bệnh nhân")
    print("40. Lưu đơn thuốc ra file JSON")
    print("41. Nhập danh sách đơn thuốc từ file JSON")
    print("42. Ghi danh sách đơn thuốc vào file JSON")
    print("43. Tính tổng tiền thuốc trong đơn")
    print("44. Tìm bệnh nhân có đơn thuốc nhiều nhất")
    print("45. Kiểm tra thuốc trùng lặp trong đơn")
    print("46. Thống kê thuốc được kê nhiều nhất")
    print("47. Tìm đơn thuốc theo ngày kê")

    print("0.  Thoát chương trình")

if __name__ == "__main__":
    while True:
        menu()
        nhap = input("Nhập lựa chọn của bạn: ")

        if nhap.isdigit():
            lua_chon = int(nhap)

            if lua_chon == 1:
                benh_nhan_moi()
            elif lua_chon == 2:
                sua_thong_tin_benh_nhan()
            elif lua_chon == 3:
                xoa_benh_nhan()
            elif lua_chon == 4:
                tim_benh_nhan_theo_ma()
            elif lua_chon == 5:
                tim_benh_nhan_theo_ten()
            elif lua_chon == 6:
                hien_thi_danh_sach_benh_nhan()
            elif lua_chon == 7:
                loc_benh_nhan_theo_do_tuoi()
            elif lua_chon == 8:
                loc_benh_nhan_theo_gioi_tinh()
            elif lua_chon == 9:
                dem_tong_so_benh_nhan()
            elif lua_chon == 10:
                xuat_danh_sach_benh_nhan_ra_json()
            elif lua_chon == 11:
                nhap_danh_sach_benh_nhan_tu_json()
            elif lua_chon == 12:
                ghi_danh_sach_benh_nhan()
            elif lua_chon == 13:
                them_bac_si_moi()
            elif lua_chon == 14:
                sua_thong_tin_bac_si()
            elif lua_chon == 15:
                xoa_bac_si()
            elif lua_chon == 16:
                tim_bac_si_theo_ma()
            elif lua_chon == 17:
                tim_bac_si_theo_chuyen_khoa()
            elif lua_chon == 18:
                hien_thi_danh_sach_bac_si()
            elif lua_chon == 19:
                loc_bac_si_theo_gioi_tinh()
            elif lua_chon == 20:
                dem_so_bac_si_theo_chuyen_khoa()
            elif lua_chon == 21:
                xuat_danh_sach_bac_si_ra_json()
            elif lua_chon == 22:
                nhap_danh_sach_bac_si_tu_json()
            elif lua_chon == 23:
                ghi_danh_sach_bac_si()
            elif lua_chon == 24:
                tao_lich_kham_moi()
            elif lua_chon == 25:
                sua_lich_kham()
            elif lua_chon == 26:
                huy_lich_kham()
            elif lua_chon == 27:
                tim_lich_kham_theo_ma_benh_nhan()
            elif lua_chon == 28:
                tim_lich_kham_theo_ngay()
            elif lua_chon == 29:
                hien_thi_lich_kham_trong_tuan()
            elif lua_chon == 30:
                thong_ke_lich_kham_theo_ngay()
            elif lua_chon == 31:
                luu_lich_kham_ra_json()
            elif lua_chon == 32:
                nhap_danh_sach_lich_kham_tu_json()
            elif lua_chon == 33:
                ghi_danh_sach_lich_kham()
            elif lua_chon == 34:
                doc_lich_kham_tu_json()
            elif lua_chon == 35:
                kiem_tra_trung_lich_bac_si()
            elif lua_chon == 36:
                tao_don_thuoc_moi()
            elif lua_chon == 37:
                them_thuoc_vao_don()
            elif lua_chon == 38:
                xoa_thuoc_khoi_don()
            elif lua_chon == 39:
                hien_thi_don_thuoc_theo_benh_nhan()
            elif lua_chon == 40:
                luu_don_thuoc_ra_json()
            elif lua_chon == 41:
                nhap_danh_sach_don_thuoc_tu_json()
            elif lua_chon == 42:
                ghi_danh_sach_don_thuoc()
            elif lua_chon == 43:
                tinh_tong_tien_thuoc_trong_don()
            elif lua_chon == 44:
                tim_benh_nhan_co_don_thuoc_nhieu_nhat()
            elif lua_chon == 45:
                kiem_tra_thuoc_trung_lap_trong_don()
            elif lua_chon == 46:
                thong_ke_thuoc_duoc_ke_nhieu_nhat()
            elif lua_chon == 47:
                tim_don_thuoc_theo_ngay_ke()
            elif lua_chon == 0:
                print("Thoát chương trình")
                break
            else:
                print("Lựa chọn không phù hợp, vui lòng chọn từ 0 đến 47.")