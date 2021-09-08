import streamlit as st
import time


def main():
    st.title("Pomotime. 👋")

    st.sidebar.header("Halo Selamat Datang! 🙌")
    st.sidebar.write("")
    st.sidebar.write("")
    
    halaman = ("Beranda", "Tentang")
    choice = st.sidebar.selectbox("", halaman)


    if choice == "Beranda":
        st.subheader("Aplikasi manajemen waktu untuk meningkatkan produktivitas. ⏲️")
        st.write("")
        st.write("")
        st.write("**Siapakah nama anda ❓**")
        name_input1 = st.text_input(label = "Nama : ")
        if name_input1:
            st.write("")
            st.write("")
            st.write(f"Hallo **_{name_input1}_!** 👋. Selamat datang di Pomotime. Mari belajar melakukan manajemen waktu metode Pomodoro menggunakan Pomotime.")
        
        st.write("")
        st.write("")
        st.write("**Kapan anda mengerjakan pekerjaan ❓**")
        date = st.date_input("Tanggal : ")
                   
        st.write("")
        st.write("")
        st.write("**Berapa banyak pekerjaan yang diselesaikan hari ini ❓**")
        jumlah = st.radio("Banyak Pekerjaan :", (1,2,3,4,5))
        if jumlah == 1:
            daftar1 = st.text_input("Pekerjaan 1 : ")
            if daftar1:
                check1 = st.checkbox(daftar1)
        elif jumlah == 2:
            daftar2 = st.text_input("Pekerjaan 1 : ")
            daftar3 = st.text_input("Pekerjaan 2 : ")
            if daftar2 :
                check2 = st.checkbox(daftar2)
            if daftar3:
                check3 = st.checkbox(daftar3)
        elif jumlah == 3:
            daftar4 = st.text_input("Pekerjaan 1 : ")
            daftar5 = st.text_input("Pekerjaan 2 : ")
            daftar6 = st.text_input("Pekerjaan 3 : ")
            if daftar4:
                check4 = st.checkbox(daftar4)
            if daftar5:
                check5 = st.checkbox(daftar5)
            if daftar6:
                check6 = st.checkbox(daftar6)
        elif jumlah == 4:
            daftar7 = st.text_input("Pekerjaan 1 : ")
            daftar8 = st.text_input("Pekerjaan 2 : ")
            daftar9 = st.text_input("Pekerjaan 3 : ")
            daftar10 = st.text_input("Pekerjaan 4 : ")
            if daftar7:
                check7 = st.checkbox(daftar7)
            if daftar8:
                check8 = st.checkbox(daftar8)
            if daftar9:
                check9 = st.checkbox(daftar9)
            if daftar10:
                check10 = st.checkbox(daftar10)
        elif jumlah == 5:
            daftar11 = st.text_input("Pekerjaan 1 : ")
            daftar12 = st.text_input("Pekerjaan 2 : ")
            daftar13 = st.text_input("Pekerjaan 3 : ")
            daftar14 = st.text_input("Pekerjaan 4 : ")
            daftar15 = st.text_input("Pekerjaan 5 : ")
            if daftar11:
                check11 = st.checkbox(daftar11)
            if daftar12:
                check12 = st.checkbox(daftar12)
            if daftar13:
                check13 = st.checkbox(daftar13)
            if daftar14:
                check14 = st.checkbox(daftar14)
            if daftar15:
                check15 = st.checkbox(daftar15)
        st.write("")
        st.write("")
        st.write("**Apakah anda sudah siap ❓**")

        start_button = st.button("Mulai")
        t1 = 1500
        t2 = 300
            
        if start_button:
            with st.empty():
                while t1:
                    mins, secs = divmod(t1, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    st.header(f"⏳ {timer}")
                    time.sleep(1)
                    t1 -= 60
                    st.success("🔔 Waktu berakhir! Saatnya Istirahat!")
    
            with st.empty():
                while t2:
                    # Start the break
                    mins2, secs2 = divmod(t2, 60)
                    timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
                    st.header(f"⏳ {timer2}")
                    time.sleep(1)
                    t2 -= 60
                    st.success("🥳 Selamat kamu barhasil menyelesaikan satu putaran Pomodoro!")
        
        st.write("")
        st.write("")
        st.write("**Lihat progress anda ❗️**")
        my_bar = st.progress(0)
        complete = st.radio("Banyak pekerjaan yang telah selesai :", (1,2,3,4,5))
        for percent_complete in range(5):
            if complete == 1:
                my_bar.progress(percent_complete + 10)
            if complete == 2:
                my_bar.progress(percent_complete + 20)
            if complete == 3:
                my_bar.progress(percent_complete + 40)
            if complete == 4:
                my_bar.progress(percent_complete + 80)
            if complete == 5:
                my_bar.progress(percent_complete + 95)

    
    else:
        st.subheader("Apa itu Pomotime ❓ ")
        st.write("""Pomotime pengatur waktu pomodoro yang dapat disesuaikan yang berfungsi 
        di desktop & browser seluler. Tujuan dari aplikasi ini adalah untuk membantu Anda 
        fokus pada tugas apa pun yang sedang Anda kerjakan, seperti belajar, menulis, atau coding. 
        Aplikasi ini terinspirasi oleh **Teknik Pomodoro** yang merupakan 
        metode manajemen waktu yang dikembangkan oleh *Francesco Cirillo* 🧑.""")

        st.subheader("Apa itu Teknik Pomodoro ❓")
        st.write("""Teknik Pomodoro diciptakan oleh Francesco Cirillo untuk cara yang lebih produktif 
        untuk bekerja dan belajar. Teknik ini menggunakan pengatur waktu untuk membagi 
        pekerjaan menjadi beberapa interval, yang biasanya berdurasi 25 menit, 
        dipisahkan dengan istirahat pendek. Setiap interval dikenal sebagai pomodoro, 
        dari kata Italia untuk 'tomat', setelah pengatur waktu dapur berbentuk tomat yang 
        digunakan Cirillo sebagai mahasiswa. - **Wikipedia** 📚.""")

        st.subheader("Bagaimana cara menggunakan Pomotime ❓")
        st.write("1. Masukkan nama anda.")
        st.write("2. Pilih tanggal anda mengerjakan pekejeraan.")
        st.write("3. Pilih banyak pekerjaan yang ingin dilesaikan.")
        st.write("4. Isi pekerjaan yang ingin dilakukan.")
        st.write("5. Tekan tombol mulai.")
        st.write("6. Lihat progress pekerjaan anda.")


if __name__ == '__main__':
    main()