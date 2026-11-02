SLUG = "backup-data-kantor-321"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-backup-321.webp"
OG_IMAGE = "/assets/og/art-blog-backup-321.jpg"

LANGS = {
"": {
"title": "Backup Data Kantor: Aturan 3-2-1 dalam Praktik",
"description": "Cara menerapkan aturan backup 3-2-1 di kantor kecil sampai menengah: apa yang dicadangkan, di mana disimpan, seberapa sering, dan cara menguji pemulihan.",
"category": "Keamanan digital",
"lead": "Backup yang belum pernah diuji pulih sama dengan tidak punya backup. Aturan 3-2-1 memberi kerangka sederhana yang bisa dijalankan kantor kecil.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"Backup Data Kantor 3-2-1\" dan ingin konsultasi rencana backup kantor kami.",
"aside": [("/services/konsultasi-teknologi", "Konsultasi teknologi"), ("/services/pengadaan-it", "Pengadaan perangkat IT"), ("/blog/keamanan-website-checklist", "Checklist keamanan website")],
"body": """<p>Aturan 3-2-1 berarti: simpan <strong>3 salinan</strong> data (satu asli dan dua cadangan), pada <strong>2 jenis media</strong> yang berbeda, dengan <strong>1 salinan di lokasi lain</strong>. Tujuannya agar satu kejadian, entah disk rusak, ransomware, kebakaran, atau pencurian, tidak menghapus semua salinan sekaligus.</p>
<h2 id="apa-dicadangkan">Apa saja yang perlu dicadangkan?</h2>
<ul><li>Berkas kerja bersama di server atau NAS.</li><li>Basis data aplikasi dan konfigurasi sistemnya.</li><li>Email dan dokumen penting di laptop karyawan.</li><li>Website, termasuk berkas unggahan dan basis datanya.</li><li>Pengaturan perangkat jaringan dan kunci lisensi.</li></ul>
<p>Mulailah dengan daftar sederhana: data apa yang bila hilang membuat kantor berhenti bekerja? Itu yang pertama dicadangkan.</p>
<h2 id="contoh-321">Seperti apa 3-2-1 untuk kantor kecil?</h2>
<ol><li><strong>Salinan 1:</strong> data kerja di server atau NAS kantor.</li><li><strong>Salinan 2:</strong> cadangan terjadwal ke disk eksternal atau NAS kedua di ruangan berbeda (media kedua).</li><li><strong>Salinan 3:</strong> cadangan terenkripsi ke penyimpanan cloud atau lokasi lain (salinan di luar kantor).</li></ol>
<h2 id="frekuensi">Seberapa sering dan berapa lama disimpan?</h2>
<p>Tentukan dua angka: berapa jam data boleh hilang (RPO) dan berapa lama sistem boleh mati sampai pulih (RTO). Data yang berubah tiap hari biasanya dicadangkan setiap malam atau lebih sering. Simpan beberapa versi (harian, mingguan, bulanan) agar bisa kembali ke kondisi sebelum berkas rusak atau terenkripsi ransomware.</p>
<h2 id="ransomware">Bagaimana melindungi backup dari ransomware?</h2>
<ul><li>Sediakan salinan yang <strong>tidak bisa diubah</strong> (immutable) atau terputus dari jaringan.</li><li>Jangan petakan folder backup sebagai drive yang bisa ditulis dari semua laptop.</li><li>Pakai akun khusus backup dengan kata sandi kuat dan verifikasi dua langkah di layanan cloud.</li><li>Enkripsi cadangan, dan simpan kunci enkripsi terpisah dari data.</li></ul>
<h2 id="uji-pulih">Bagaimana menguji pemulihan?</h2>
<p>Jadwalkan uji pulih tiap tiga bulan: pilih satu berkas dan satu sistem, pulihkan ke lokasi lain, lalu buka dan pastikan isinya benar. Catat berapa lama waktunya. Prosedur tertulis langkah demi langkah penting, karena saat insiden biasanya yang bertugas sedang panik.</p>
<h2 id="kesalahan-umum">Kesalahan yang sering terjadi</h2>
<ul><li>Hanya ada satu disk eksternal yang selalu tercolok di komputer yang sama.</li><li>Cadangan ada, tetapi tidak ada yang tahu cara memulihkannya.</li><li>Salinan di luar kantor tidak pernah diperiksa apakah masih berjalan.</li><li>Data di laptop karyawan tidak dicakup sama sekali.</li></ul>
<p>Sentra membantu merancang rencana backup dan perangkatnya. Lihat <a href="/services/konsultasi-teknologi">konsultasi teknologi</a>, <a href="/services/pengadaan-it">pengadaan perangkat IT</a>, dan <a href="/blog/keamanan-website-checklist">checklist keamanan website</a>.</p>""",
"faq": [("Apakah menyalin ke Google Drive atau layanan sinkronisasi sudah termasuk backup?","Belum tentu. Layanan sinkronisasi ikut menyalin penghapusan atau berkas yang terenkripsi ransomware. Backup sejati menyimpan versi lama yang bisa dikembalikan."),
("Berapa kapasitas yang perlu disiapkan?","Mulai dari ukuran data aktif, lalu tambah ruang untuk beberapa versi dan pertumbuhan. Kapasitas cadangan biasanya beberapa kali lipat data aktif."),
("Siapa yang bertanggung jawab atas backup?","Tetapkan satu nama dan satu pengganti. Backup yang tugas semua orang biasanya tidak dikerjakan siapa pun."),
("Apakah cloud saja cukup?","Cloud memenuhi salinan di luar kantor. Untuk pemulihan cepat, salinan lokal tetap berguna karena mengunduh data besar dari cloud bisa lama.")]},
"en": {
"title": "Office Data Backup: The 3-2-1 Rule in Practice",
"description": "How to apply the 3-2-1 backup rule in a small to mid-size office: what to back up, where to store it, how often, and how to test recovery.",
"category": "Digital security",
"lead": "A backup that has never been test-restored is the same as no backup. The 3-2-1 rule gives a simple framework a small office can follow.",
"wa_text": "Hello Sentra, I just read \"Office Data Backup 3-2-1\" and would like advice on our backup plan.",
"aside": [("/services/konsultasi-teknologi", "Technology consulting"), ("/services/pengadaan-it", "IT procurement"), ("/blog/keamanan-website-checklist", "Website security checklist")],
"body": """<p>The 3-2-1 rule means: keep <strong>3 copies</strong> of data (one original and two backups), on <strong>2 different media types</strong>, with <strong>1 copy off-site</strong>. The aim is that one event, whether a failed disk, ransomware, fire or theft, does not wipe out every copy at once.</p>
<h2 id="apa-dicadangkan">What should be backed up?</h2>
<ul><li>Shared working files on the server or NAS.</li><li>Application databases and system configuration.</li><li>Email and important documents on staff laptops.</li><li>The website, including uploads and its database.</li><li>Network device settings and licence keys.</li></ul>
<p>Start with a simple question: which data, if lost, would stop the office working? Back that up first.</p>
<h2 id="contoh-321">What does 3-2-1 look like for a small office?</h2>
<ol><li><strong>Copy 1:</strong> working data on the office server or NAS.</li><li><strong>Copy 2:</strong> scheduled backup to an external disk or a second NAS in a different room (second medium).</li><li><strong>Copy 3:</strong> encrypted backup to cloud storage or another location (off-site copy).</li></ol>
<h2 id="frekuensi">How often, and how long to keep?</h2>
<p>Decide two numbers: how many hours of data you can afford to lose (RPO) and how long the system may be down before recovery (RTO). Data that changes daily is usually backed up nightly or more often. Keep several versions (daily, weekly, monthly) so you can return to the state before a file was damaged or encrypted by ransomware.</p>
<h2 id="ransomware">How do you protect backups from ransomware?</h2>
<ul><li>Keep a copy that is <strong>immutable</strong> or disconnected from the network.</li><li>Do not map the backup folder as a drive writable from every laptop.</li><li>Use a dedicated backup account with a strong password and two-step verification on cloud services.</li><li>Encrypt backups, and store the key separately from the data.</li></ul>
<h2 id="uji-pulih">How do you test recovery?</h2>
<p>Schedule a recovery test every three months: pick one file and one system, restore to another location, open it and confirm it is correct. Record how long it took. A written step-by-step procedure matters, because whoever is on duty during an incident is usually under stress.</p>
<h2 id="kesalahan-umum">Common mistakes</h2>
<ul><li>A single external disk always plugged into the same computer.</li><li>Backups exist but nobody knows how to restore them.</li><li>The off-site copy is never checked to see whether it is still running.</li><li>Staff laptop data is not covered at all.</li></ul>
<p>Sentra helps design the backup plan and hardware. See <a href="/en/services/konsultasi-teknologi">technology consulting</a>, <a href="/en/services/pengadaan-it">IT procurement</a> and the <a href="/en/blog/keamanan-website-checklist">website security checklist</a>.</p>""",
"faq": [("Is copying to Google Drive or a sync service a backup?","Not necessarily. Sync services also copy deletions and ransomware-encrypted files. A true backup keeps older versions you can restore."),
("How much capacity should I plan?","Start from the size of active data, then add room for several versions and growth. Backup capacity is usually several times the active data."),
("Who is responsible for backups?","Name one person and one deputy. A backup that is everyone's job is usually nobody's."),
("Is cloud alone enough?","Cloud satisfies the off-site copy. For fast recovery a local copy still helps, because downloading large data from the cloud can take long.")]},
"ms": {
"title": "Sandaran Data Pejabat: Peraturan 3-2-1 dalam Amalan",
"description": "Cara menerapkan peraturan sandaran 3-2-1 di pejabat kecil hingga sederhana.",
"category": "Keselamatan digital",
"lead": "Sandaran yang tidak pernah diuji pemulihan sama seperti tiada sandaran.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"Sandaran Data Pejabat 3-2-1\" dan ingin berunding.",
"aside": [("/services/konsultasi-teknologi", "Perundingan teknologi"), ("/services/pengadaan-it", "Perolehan IT"), ("/blog/keamanan-website-checklist", "Senarai semak keselamatan laman web")],
"body": """<p>Peraturan 3-2-1: simpan <strong>3 salinan</strong> data, pada <strong>2 jenis media</strong> berbeza, dengan <strong>1 salinan di lokasi lain</strong>. Tujuannya supaya satu kejadian seperti cakera rosak, ransomware, kebakaran atau kecurian tidak memadam semua salinan.</p>
<h2 id="contoh-321">Contoh untuk pejabat kecil</h2>
<ol><li>Data kerja di pelayan atau NAS pejabat.</li><li>Sandaran berjadual ke cakera luaran atau NAS kedua di bilik berbeza.</li><li>Sandaran disulitkan ke storan awan atau lokasi lain.</li></ol>
<p>Ujilah pemulihan setiap tiga bulan, simpan beberapa versi dan lindungi sandaran daripada ransomware dengan salinan tidak boleh diubah. Lihat <a href="/ms/services/konsultasi-teknologi">perundingan teknologi</a> daripada Sentra.</p>""",
"faq": [("Adakah menyalin ke perkhidmatan penyegerakan dikira sandaran?","Tidak semestinya. Penyegerakan turut menyalin pemadaman dan fail yang disulitkan ransomware."),
("Siapa bertanggungjawab ke atas sandaran?","Tetapkan seorang penanggungjawab dan seorang pengganti.")]},
"zh": {
"title": "办公室数据备份：3-2-1 规则的实践",
"description": "如何在中小型办公室应用 3-2-1 备份规则：备份什么、存在哪、多久一次、如何测试恢复。",
"category": "数字安全",
"lead": "从未测试过恢复的备份等于没有备份。",
"wa_text": "您好 Sentra，我刚读了《办公室数据备份 3-2-1》，想咨询我们的备份方案。",
"aside": [("/services/konsultasi-teknologi", "技术咨询"), ("/services/pengadaan-it", "IT 设备采购"), ("/blog/keamanan-website-checklist", "网站安全检查清单")],
"body": """<p>3-2-1 规则：保存<strong>3 份</strong>数据，使用<strong>2 种不同介质</strong>，其中<strong>1 份存放在异地</strong>。这样单一事件（磁盘损坏、勒索软件、火灾、被盗）不会同时毁掉所有副本。</p>
<h2 id="contoh-321">小型办公室示例</h2>
<ol><li>办公室服务器或 NAS 上的工作数据。</li><li>定时备份到外置硬盘或另一个房间的第二台 NAS。</li><li>加密备份到云存储或其他地点。</li></ol>
<p>每三个月测试一次恢复，保留多个版本，并用不可更改的副本防勒索软件。参见 Sentra 的<a href="/zh/services/konsultasi-teknologi">技术咨询</a>。</p>""",
"faq": [("同步到网盘算备份吗？","不一定。同步服务也会同步删除和被勒索软件加密的文件。"),
("谁负责备份？","指定一名负责人和一名代理。")]},
"ko": {
"title": "사무실 데이터 백업: 3-2-1 규칙 실전",
"description": "소규모~중간 규모 사무실에서 3-2-1 백업 규칙을 적용하는 방법: 무엇을, 어디에, 얼마나 자주 백업하고 복구를 어떻게 테스트하는지.",
"category": "디지털 보안",
"lead": "복구를 한 번도 테스트하지 않은 백업은 백업이 없는 것과 같습니다.",
"wa_text": "안녕하세요 Sentra, \"사무실 데이터 백업 3-2-1\" 글을 읽고 백업 계획을 상담하고 싶습니다.",
"aside": [("/services/konsultasi-teknologi", "기술 컨설팅"), ("/services/pengadaan-it", "IT 장비 조달"), ("/blog/keamanan-website-checklist", "웹사이트 보안 체크리스트")],
"body": """<p>3-2-1 규칙은 데이터를 <strong>3개</strong> 사본으로, <strong>2종류</strong> 매체에, 그중 <strong>1개는 외부</strong>에 보관하는 것입니다. 디스크 고장, 랜섬웨어, 화재, 도난 중 한 사건이 모든 사본을 한꺼번에 없애지 못하게 하기 위함입니다.</p>
<h2 id="contoh-321">소규모 사무실 예시</h2>
<ol><li>사무실 서버 또는 NAS의 작업 데이터.</li><li>외장 디스크나 다른 방의 두 번째 NAS로 예약 백업.</li><li>클라우드 또는 다른 장소로 암호화 백업.</li></ol>
<p>3개월마다 복구를 테스트하고 여러 버전을 보관하며 변경 불가 사본으로 랜섬웨어에 대비하세요. Sentra의 <a href="/ko/services/konsultasi-teknologi">기술 컨설팅</a>을 확인하세요.</p>""",
"faq": [("동기화 서비스에 복사하면 백업인가요?","반드시 그렇지는 않습니다. 동기화는 삭제나 랜섬웨어로 암호화된 파일도 복사합니다."),
("백업 책임자는 누구여야 하나요?","담당자 한 명과 대리인 한 명을 정하세요.")]},
}
