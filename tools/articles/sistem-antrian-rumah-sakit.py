SLUG = "sistem-antrian-rumah-sakit"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-antrian-rs.webp"
OG_IMAGE = "/assets/og/art-blog-antrian-rs.jpg"

LANGS = {
"": {
"title": "Sistem Antrian Rumah Sakit dan Klinik: Kiosk, Layar, dan Integrasi SIMRS",
"description": "Apa yang perlu disiapkan untuk sistem antrian rumah sakit, klinik, atau poliklinik: alur pasien, kiosk, layar panggilan, integrasi SIMRS, dan data waktu tunggu.",
"category": "Kesehatan",
"lead": "Antrian yang kacau bukan hanya soal kenyamanan. Di fasilitas kesehatan, ia memengaruhi waktu tunggu pasien dan beban kerja petugas pendaftaran.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"Sistem Antrian Rumah Sakit\" dan ingin konsultasi untuk fasilitas kesehatan kami.",
"aside": [("/produk/kiosk", "Kiosk"), ("/services/integrasi-sistem", "Integrasi sistem"), ("/portfolio/sistem-antrian-poliklinik", "Studi kasus: sistem antrian poliklinik")],
"body": """<p>Sistem antrian di rumah sakit dan klinik biasanya mencakup pengambilan nomor, pemanggilan ke loket atau ruang periksa, dan layar informasi di ruang tunggu. Yang membedakannya dari antrian di kantor layanan lain adalah alurnya bertingkat: pendaftaran, pemeriksaan, laboratorium atau radiologi, farmasi, dan kasir.</p>
<h2 id="alur-pasien">Seperti apa alur pasien yang perlu dipetakan?</h2>
<ol><li>Pasien tiba, mengambil nomor di kiosk atau mendaftar lewat aplikasi atau website.</li><li>Pendaftaran: verifikasi identitas dan data kunjungan.</li><li>Poliklinik: antrian per dokter atau per poli.</li><li>Penunjang: laboratorium atau radiologi bila ada.</li><li>Farmasi: antrian obat.</li><li>Kasir atau penyelesaian administrasi.</li></ol>
<p>Setiap tahap bisa menjadi titik penumpukan. Memetakan alur dan mengukur waktu di tiap tahap lebih penting daripada memilih perangkat.</p>
<h2 id="komponen">Komponen sistem</h2>
<ul><li><strong>Kiosk atau pendaftaran daring</strong> untuk mengambil nomor sesuai jenis layanan atau dokter.</li><li><strong>Layar panggilan dan suara</strong> di setiap area tunggu.</li><li><strong>Aplikasi petugas</strong> untuk memanggil, menunda, atau mengalihkan pasien.</li><li><strong>Dasbor</strong> waktu tunggu dan beban tiap poli.</li><li><strong>Tampilan untuk pasien prioritas</strong> seperti lansia, ibu hamil, atau kasus gawat, sesuai kebijakan fasilitas.</li></ul>
<h2 id="integrasi-simrs">Mengapa integrasi dengan SIMRS penting?</h2>
<p>Bila antrian berdiri sendiri, petugas mengetik ulang data yang sudah ada di Sistem Informasi Manajemen Rumah Sakit (SIMRS). Integrasi memungkinkan nomor antrian terhubung ke data kunjungan, jadwal dokter, dan status pelayanan. Tanyakan lebih dulu apakah SIMRS Anda menyediakan antarmuka (API) atau berkas pertukaran data, karena itu menentukan tingkat kesulitan. Bila fasilitas melayani pasien dengan antrean daring dari penjamin, cek persyaratan integrasi terbarunya dari penyedia layanan tersebut.</p>
<h2 id="data-pasien">Bagaimana dengan data pasien?</h2>
<p>Informasi kesehatan termasuk data pribadi yang sensitif. Layar di ruang tunggu sebaiknya menampilkan nomor antrian, bukan nama lengkap atau diagnosis. Batasi data yang disimpan oleh sistem antrian pada yang dibutuhkan, dan tetapkan hak akses petugas serta retensinya. Konsultasikan kebijakan ini dengan bagian hukum dan penanggung jawab data fasilitas.</p>
<h2 id="mengukur">Apa yang diukur untuk perbaikan?</h2>
<ul><li>Rata-rata dan sebaran waktu tunggu per poli dan per jam.</li><li>Waktu layanan per dokter atau loket.</li><li>Jam puncak, untuk mengatur jadwal petugas.</li><li>Persentase pasien yang pergi sebelum dipanggil.</li></ul>
<p>Studi kasus penerapan di poliklinik ada di <a href="/portfolio/sistem-antrian-poliklinik">sistem antrian poliklinik</a>. Perencanaan kiosk untuk layanan publik lain ada di <a href="/blog/kiosk-pelayanan-publik-mpp">kiosk pelayanan publik</a>.</p>
<p>Sentra menyediakan kiosk, sistem antrian, dan integrasi. Lihat <a href="/produk/kiosk">produk kiosk</a> dan <a href="/services/integrasi-sistem">integrasi sistem</a>.</p>""",
"faq": [("Apakah sistem antrian harus terhubung ke SIMRS?","Tidak wajib untuk mulai, tetapi integrasi mengurangi input ganda dan memungkinkan data waktu tunggu yang lebih berguna. Cek dulu antarmuka yang tersedia di SIMRS Anda."),
("Apakah pasien bisa mendaftar dari rumah?","Bisa bila sistem mendukung pendaftaran lewat website atau aplikasi. Sediakan tetap kiosk dan loket bagi pasien yang tidak memakai ponsel."),
("Apakah nama pasien boleh ditampilkan di layar?","Sebaiknya tidak. Gunakan nomor antrian, dan jaga privasi pasien sesuai kebijakan fasilitas dan aturan perlindungan data."),
("Berapa lama pemasangan?","Bergantung ukuran fasilitas, jumlah poli, dan ada tidaknya integrasi. Konfirmasi lewat survei lokasi dan alur layanan.")]},
"en": {
"title": "Hospital and Clinic Queue Systems: Kiosks, Displays and HIS Integration",
"description": "What to prepare for a queue system in a hospital, clinic or outpatient department: patient flow, kiosks, call displays, hospital information system integration and waiting-time data.",
"category": "Healthcare",
"lead": "A chaotic queue is not just about comfort. In healthcare facilities it affects patient waiting time and the workload of registration staff.",
"wa_text": "Hello Sentra, I just read \"Hospital Queue Systems\" and would like advice for our healthcare facility.",
"aside": [("/produk/kiosk", "Kiosk"), ("/services/integrasi-sistem", "System integration"), ("/portfolio/sistem-antrian-poliklinik", "Case study: outpatient queue system")],
"body": """<p>A hospital or clinic queue system usually covers number issuing, calling to counters or consulting rooms, and information screens in the waiting area. What sets it apart from other service offices is its tiered flow: registration, consultation, laboratory or radiology, pharmacy and cashier.</p>
<h2 id="alur-pasien">What patient flow needs mapping?</h2>
<ol><li>The patient arrives, takes a number at the kiosk or registers through an app or website.</li><li>Registration: identity verification and visit data.</li><li>Outpatient clinic: queue per doctor or clinic.</li><li>Support services: laboratory or radiology where applicable.</li><li>Pharmacy: medicine queue.</li><li>Cashier or administrative completion.</li></ol>
<p>Every stage can become a bottleneck. Mapping the flow and measuring time at each stage matters more than choosing hardware.</p>
<h2 id="komponen">System components</h2>
<ul><li><strong>Kiosk or online registration</strong> to take a number by service type or doctor.</li><li><strong>Call displays and audio</strong> in each waiting area.</li><li><strong>Staff application</strong> to call, defer or redirect patients.</li><li><strong>Dashboard</strong> of waiting time and load per clinic.</li><li><strong>Display for priority patients</strong> such as the elderly, pregnant women or urgent cases, per facility policy.</li></ul>
<h2 id="integrasi-simrs">Why does hospital information system (HIS) integration matter?</h2>
<p>If the queue stands alone, staff retype data already in the Hospital Information Management System (SIMRS). Integration links queue numbers to visit data, doctor schedules and service status. First ask whether your SIMRS offers an interface (API) or data exchange files, because that sets the difficulty. If the facility serves patients through online queues from a payer, check the latest integration requirements from that provider.</p>
<h2 id="data-pasien">What about patient data?</h2>
<p>Health information is sensitive personal data. Waiting-room screens should show queue numbers, not full names or diagnoses. Limit what the queue system stores to what is needed, and set staff access rights and retention. Consult your legal team and the facility's data officer on this policy.</p>
<h2 id="mengukur">What to measure for improvement</h2>
<ul><li>Average and spread of waiting time per clinic and per hour.</li><li>Service time per doctor or counter.</li><li>Peak hours, to plan staff schedules.</li><li>Percentage of patients who leave before being called.</li></ul>
<p>A clinic deployment case study is at <a href="/en/portfolio/sistem-antrian-poliklinik">outpatient queue system</a>. Kiosk planning for other public services is in <a href="/en/blog/kiosk-pelayanan-publik-mpp">public service kiosks</a>.</p>
<p>Sentra supplies kiosks, queue systems and integration. See the <a href="/en/produk/kiosk">kiosk product</a> and <a href="/en/services/integrasi-sistem">system integration</a>.</p>""",
"faq": [("Must the queue system connect to SIMRS?","Not to get started, but integration reduces double entry and gives more useful waiting-time data. First check the interface your SIMRS offers."),
("Can patients register from home?","Yes if the system supports registration by website or app. Keep kiosks and counters for patients without phones."),
("May patient names appear on the screen?","Preferably not. Use queue numbers and protect patient privacy per facility policy and data protection rules."),
("How long does installation take?","It depends on facility size, number of clinics and whether integration is needed. Confirm after a site and service-flow survey.")]},
"ms": {
"title": "Sistem Giliran Hospital dan Klinik: Kiosk, Paparan dan Integrasi",
"description": "Apa yang perlu disediakan untuk sistem giliran hospital atau klinik.",
"category": "Kesihatan",
"lead": "Giliran yang kucar-kacir bukan sekadar soal keselesaan; ia menjejaskan masa menunggu pesakit.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"Sistem Giliran Hospital\" dan ingin berunding.",
"aside": [("/produk/kiosk", "Kiosk"), ("/services/integrasi-sistem", "Integrasi sistem"), ("/portfolio/sistem-antrian-poliklinik", "Kajian kes: sistem giliran poliklinik")],
"body": """<p>Sistem giliran biasanya merangkumi pengambilan nombor, panggilan ke kaunter atau bilik pemeriksaan dan skrin maklumat. Aliran pesakit berperingkat: pendaftaran, pemeriksaan, makmal atau radiologi, farmasi dan juruwang.</p>
<h2 id="data-pasien">Data pesakit</h2>
<p>Maklumat kesihatan ialah data peribadi sensitif. Skrin di ruang menunggu patut memaparkan nombor giliran, bukan nama penuh atau diagnosis. Integrasi dengan sistem maklumat hospital mengurangkan input berganda; semak dahulu antara muka yang tersedia.</p>
<p>Lihat <a href="/ms/produk/kiosk">produk kiosk</a> dan <a href="/ms/services/integrasi-sistem">integrasi sistem</a> daripada Sentra.</p>""",
"faq": [("Adakah sistem giliran mesti bersambung dengan SIMRS?","Tidak wajib untuk bermula, tetapi integrasi mengurangkan input berganda."),
("Bolehkah nama pesakit dipaparkan?","Sebaiknya tidak; gunakan nombor giliran.")]},
"zh": {
"title": "医院与诊所排队系统：自助终端、显示屏与 HIS 集成",
"description": "医院、诊所或门诊部排队系统需要准备什么：患者流程、自助终端、叫号屏、医院信息系统集成和等待时间数据。",
"category": "医疗",
"lead": "混乱的排队不只是舒适度问题，在医疗机构还影响患者等待时间和挂号人员的工作量。",
"wa_text": "您好 Sentra，我刚读了《医院排队系统》，想咨询我们的医疗机构。",
"aside": [("/produk/kiosk", "自助终端"), ("/services/integrasi-sistem", "系统集成"), ("/portfolio/sistem-antrian-poliklinik", "案例：门诊排队系统")],
"body": """<p>排队系统通常包括取号、呼叫到窗口或诊室，以及候诊区信息屏。患者流程是分层的：挂号、诊疗、检验或放射、药房和收费。</p>
<h2 id="data-pasien">患者数据</h2>
<p>健康信息属于敏感个人数据。候诊区屏幕应显示排队号码，而不是全名或诊断。与医院信息系统集成可减少重复录入，请先确认可用的接口。</p>
<p>参见 Sentra 的<a href="/zh/produk/kiosk">自助终端产品</a>和<a href="/zh/services/integrasi-sistem">系统集成</a>。</p>""",
"faq": [("排队系统必须连接 SIMRS 吗？","开始时不必，但集成可减少重复录入。"),
("屏幕上可以显示患者姓名吗？","最好不要，使用排队号码。")]},
"ko": {
"title": "병원·의원 대기 시스템: 키오스크, 화면, 병원정보시스템 연동",
"description": "병원, 의원, 외래에 필요한 대기 시스템 준비: 환자 동선, 키오스크, 호출 화면, 병원정보시스템 연동, 대기시간 데이터.",
"category": "의료",
"lead": "어수선한 대기는 편의의 문제만이 아닙니다. 의료기관에서는 환자 대기시간과 접수 직원의 업무량에 영향을 줍니다.",
"wa_text": "안녕하세요 Sentra, \"병원 대기 시스템\" 글을 읽고 우리 의료기관을 상담하고 싶습니다.",
"aside": [("/produk/kiosk", "키오스크"), ("/services/integrasi-sistem", "시스템 통합"), ("/portfolio/sistem-antrian-poliklinik", "사례: 외래 대기 시스템")],
"body": """<p>대기 시스템은 보통 번호 발급, 창구·진료실 호출, 대기실 안내 화면을 포함합니다. 환자 동선은 접수, 진료, 검사·영상, 약국, 수납으로 단계적입니다.</p>
<h2 id="data-pasien">환자 데이터</h2>
<p>건강 정보는 민감한 개인정보입니다. 대기실 화면에는 이름이나 진단이 아니라 대기번호를 표시하세요. 병원정보시스템과 연동하면 중복 입력이 줄어드니 먼저 제공되는 인터페이스를 확인하세요.</p>
<p>Sentra의 <a href="/ko/produk/kiosk">키오스크 제품</a>과 <a href="/ko/services/integrasi-sistem">시스템 통합</a>을 확인하세요.</p>""",
"faq": [("대기 시스템을 반드시 SIMRS와 연동해야 하나요?","시작할 때는 필수가 아니지만 연동하면 중복 입력이 줄어듭니다."),
("화면에 환자 이름을 표시해도 되나요?","가급적 피하고 대기번호를 사용하세요.")]},
}
