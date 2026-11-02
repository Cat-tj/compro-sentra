SLUG = "keamanan-website-checklist"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-keamanan-website.webp"
OG_IMAGE = "/assets/og/art-blog-keamanan-website.jpg"

LANGS = {
"": {
"title": "Checklist Keamanan Website: 12 Hal yang Dicek Sebelum Diretas",
"description": "Daftar 12 pemeriksaan keamanan website untuk kantor, sekolah, dan instansi: pembaruan, kata sandi, cadangan, akun, tanda peretasan judi online, dan langkah saat sudah terkena.",
"category": "Keamanan digital",
"lead": "Sebagian besar website yang diretas bukan karena serangan canggih, tetapi karena pembaruan tertunda, kata sandi lemah, atau akun lama yang lupa dimatikan.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"Checklist Keamanan Website\" dan ingin website kami diperiksa.",
"aside": [("/services/konsultasi-teknologi", "Konsultasi teknologi"), ("/services/custom-software", "Custom software"), ("/produk/website", "Website")],
"body": """<p>Gunakan daftar ini sebagai pemeriksaan berkala, misalnya tiap tiga bulan. Hampir semuanya bisa dikerjakan tanpa alat mahal. Bila ada yang tidak Anda pahami, minta pengelola website atau vendor menjelaskan jawabannya secara tertulis.</p>
<h2 id="checklist">Apa saja 12 pemeriksaannya?</h2>
<ol><li><strong>HTTPS aktif</strong> di semua halaman, dengan sertifikat yang tidak kedaluwarsa dan pengalihan dari http.</li><li><strong>Pembaruan terpasang</strong> untuk CMS (misalnya WordPress), tema, dan plugin. Pembaruan keamanan yang tertunda adalah pintu masuk paling umum.</li><li><strong>Hapus plugin dan tema yang tidak dipakai.</strong> Yang dinonaktifkan pun bisa memuat celah.</li><li><strong>Kata sandi admin kuat dan unik</strong>, tidak dipakai di layanan lain, disimpan di pengelola kata sandi.</li><li><strong>Verifikasi dua langkah</strong> untuk login admin, hosting, dan email domain.</li><li><strong>Daftar akun dibersihkan.</strong> Matikan akun mantan karyawan dan vendor lama; beri hak akses seperlunya saja.</li><li><strong>Cadangan otomatis</strong> yang disimpan di luar server website, dan pernah diuji dipulihkan.</li><li><strong>Hak akses berkas</strong> yang wajar: berkas tidak perlu dapat ditulis oleh semua pihak, dan folder unggahan tidak boleh mengeksekusi skrip.</li><li><strong>Batasi percobaan login</strong> dan sembunyikan atau amankan halaman login admin.</li><li><strong>Pemantauan perubahan berkas</strong> atau pemberitahuan bila ada berkas baru yang tidak dikenal.</li><li><strong>Akun registrar dan DNS</strong> dilindungi kata sandi kuat dan verifikasi dua langkah; domain dikunci dan email kontak aktif.</li><li><strong>Log tersimpan</strong> cukup lama untuk menelusuri kejadian bila terjadi insiden.</li></ol>
<h2 id="tanda-judi-online">Apa tanda website terkena injeksi judi online?</h2>
<ul><li>Hasil pencarian Google untuk nama website Anda menampilkan judul atau deskripsi berisi kata judi atau slot.</li><li>Halaman terlihat normal bagi Anda, tetapi berbeda bagi pengunjung dari Google (disebut cloaking).</li><li>Ada berkas atau halaman baru yang tidak pernah Anda buat, atau tautan tersembunyi di footer.</li><li>Pencarian <code>site:domainanda.go.id</code> di Google menampilkan halaman yang tidak dikenal.</li></ul>
<h2 id="jika-terkena">Apa yang dilakukan jika sudah terkena?</h2>
<ol><li>Jangan hanya menghapus halaman yang terlihat. Penyusup biasanya meninggalkan pintu belakang untuk masuk lagi.</li><li>Ganti semua kata sandi (admin, hosting, basis data, FTP) dan matikan akun yang tidak dikenal.</li><li>Pulihkan dari cadangan bersih bila ada, lalu pasang semua pembaruan.</li><li>Cari dan hapus berkas yang tidak dikenal, lalu periksa ulang sesudahnya.</li><li>Ajukan peninjauan ulang di Google Search Console setelah bersih.</li><li>Catat kronologi untuk pelaporan internal, dan laporkan sesuai prosedur instansi bila perlu.</li></ol>
<h2 id="siapa-bertanggung-jawab">Siapa yang seharusnya bertanggung jawab?</h2>
<p>Tetapkan satu nama penanggung jawab, bukan "tim IT" secara umum, dan masukkan perawatan keamanan dalam kontrak vendor, termasuk siapa yang memperbarui dan seberapa cepat. Website yang dibuat sekali lalu dibiarkan adalah penyebab utama masalah ini.</p>
<p>Sentra membantu pemeriksaan, perbaikan, dan perawatan website. Lihat <a href="/services/konsultasi-teknologi">konsultasi teknologi</a>, <a href="/services/custom-software">custom software</a>, dan <a href="/produk/website">layanan website</a>.</p>""",
"faq": [("Seberapa sering website perlu diperiksa?","Pemeriksaan keamanan ringan tiap tiga bulan, dan pembaruan keamanan segera setelah dirilis. Website instansi atau yang menyimpan data pengguna perlu lebih sering."),
("Apakah cadangan saja cukup?","Tidak. Cadangan membantu pulih, tetapi tidak mencegah. Pastikan juga pembaruan, kata sandi, dan verifikasi dua langkah beres, dan uji pemulihannya."),
("Bagaimana tahu website saya sudah bersih setelah dibersihkan?","Periksa ulang beberapa hari kemudian: cari berkas baru yang tidak dikenal, cek hasil pencarian Google, dan pantau log login. Peretas sering kembali lewat pintu belakang."),
("Apakah website statis lebih aman?","Umumnya permukaan seranganya jauh lebih kecil karena tidak ada basis data atau panel admin yang terbuka, tetapi akun hosting dan domain tetap perlu diamankan.")]},
"en": {
"title": "Website Security Checklist: 12 Checks Before You Get Hacked",
"description": "A 12-point website security checklist for offices, schools and agencies: updates, passwords, backups, accounts, signs of online-gambling injection, and what to do once hit.",
"category": "Digital security",
"lead": "Most hacked websites fall not to sophisticated attacks but to delayed updates, weak passwords or old accounts nobody switched off.",
"wa_text": "Hello Sentra, I just read \"Website Security Checklist\" and would like our website checked.",
"aside": [("/services/konsultasi-teknologi", "Technology consulting"), ("/services/custom-software", "Custom software"), ("/produk/website", "Website")],
"body": """<p>Use this list as a periodic check, for example every three months. Almost all of it needs no expensive tools. If something is unclear, ask your website manager or vendor to explain the answer in writing.</p>
<h2 id="checklist">What are the 12 checks?</h2>
<ol><li><strong>HTTPS on</strong> for all pages, with an unexpired certificate and redirect from http.</li><li><strong>Updates installed</strong> for the CMS (such as WordPress), themes and plugins. Delayed security updates are the most common way in.</li><li><strong>Remove unused plugins and themes.</strong> Even deactivated ones can contain flaws.</li><li><strong>Strong, unique admin passwords</strong>, not reused elsewhere, stored in a password manager.</li><li><strong>Two-step verification</strong> for admin login, hosting and domain email.</li><li><strong>Clean up the account list.</strong> Disable former staff and old vendors; grant only the access needed.</li><li><strong>Automatic backups</strong> stored off the website server, and restore-tested at least once.</li><li><strong>Sensible file permissions</strong>: files need not be writable by everyone, and upload folders must not execute scripts.</li><li><strong>Limit login attempts</strong> and hide or protect the admin login page.</li><li><strong>File change monitoring</strong> or alerts for new unknown files.</li><li><strong>Registrar and DNS accounts</strong> protected with strong passwords and two-step verification; domain locked and contact email active.</li><li><strong>Logs kept</strong> long enough to trace an incident.</li></ol>
<h2 id="tanda-judi-online">What are the signs of online-gambling injection?</h2>
<ul><li>Google results for your site name show titles or descriptions with gambling or slot words.</li><li>Pages look normal to you but different to visitors from Google (cloaking).</li><li>New files or pages you never created, or hidden links in the footer.</li><li>Searching <code>site:yourdomain.go.id</code> on Google shows unknown pages.</li></ul>
<h2 id="jika-terkena">What to do if you are already hit</h2>
<ol><li>Do not just delete the visible pages. Intruders usually leave a backdoor to return.</li><li>Change all passwords (admin, hosting, database, FTP) and disable unknown accounts.</li><li>Restore from a clean backup if you have one, then install all updates.</li><li>Find and remove unknown files, then recheck afterwards.</li><li>Request a review in Google Search Console once clean.</li><li>Record the timeline for internal reporting, and report per your agency's procedure if needed.</li></ol>
<h2 id="siapa-bertanggung-jawab">Who should be responsible?</h2>
<p>Name one responsible person, not just "the IT team", and write security maintenance into the vendor contract, including who applies updates and how fast. A website built once and then left alone is the main cause of this problem.</p>
<p>Sentra helps with website checks, repair and maintenance. See <a href="/en/services/konsultasi-teknologi">technology consulting</a>, <a href="/en/services/custom-software">custom software</a> and <a href="/en/produk/website">website services</a>.</p>""",
"faq": [("How often should a website be checked?","A light security check every three months, and security updates as soon as they are released. Agency sites or those holding user data need it more often."),
("Are backups alone enough?","No. Backups help recovery but do not prevent attacks. Also fix updates, passwords and two-step verification, and test restoring."),
("How do I know the site is clean after cleanup?","Recheck a few days later: look for new unknown files, check Google results and watch login logs. Attackers often return through a backdoor."),
("Is a static website safer?","Generally its attack surface is much smaller because there is no exposed database or admin panel, but hosting and domain accounts still need securing.")]},
"ms": {
"title": "Senarai Semak Keselamatan Laman Web: 12 Perkara Sebelum Digodam",
"description": "12 semakan keselamatan laman web untuk pejabat, sekolah dan agensi: kemas kini, kata laluan, sandaran, akaun dan tanda suntikan judi dalam talian.",
"category": "Keselamatan digital",
"lead": "Kebanyakan laman web yang digodam bukan kerana serangan canggih, tetapi kerana kemas kini tertangguh, kata laluan lemah atau akaun lama.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"Senarai Semak Keselamatan Laman Web\" dan ingin laman web kami disemak.",
"aside": [("/services/konsultasi-teknologi", "Perundingan teknologi"), ("/services/custom-software", "Perisian tersuai"), ("/produk/website", "Laman web")],
"body": """<p>Gunakan senarai ini sebagai semakan berkala, contohnya setiap tiga bulan.</p>
<h2 id="checklist">Apakah 12 semakan itu?</h2>
<ol><li>HTTPS aktif di semua halaman.</li><li>Kemas kini CMS, tema dan plugin dipasang.</li><li>Buang plugin dan tema yang tidak digunakan.</li><li>Kata laluan admin kuat dan unik.</li><li>Pengesahan dua langkah untuk admin, hosting dan e-mel domain.</li><li>Bersihkan senarai akaun dan hadkan akses.</li><li>Sandaran automatik di luar pelayan dan pernah diuji pemulihan.</li><li>Kebenaran fail yang munasabah.</li><li>Hadkan percubaan log masuk.</li><li>Pemantauan perubahan fail.</li><li>Lindungi akaun pendaftar dan DNS.</li><li>Simpan log cukup lama.</li></ol>
<h2 id="tanda-judi-online">Apakah tanda suntikan judi dalam talian?</h2>
<p>Keputusan carian Google memaparkan tajuk judi atau slot, halaman berbeza untuk pengunjung dari Google (cloaking), fail baharu yang tidak dikenali, atau pautan tersembunyi. Jangan hanya memadam halaman yang kelihatan; tukar semua kata laluan, pulihkan dari sandaran bersih dan cari pintu belakang.</p>
<p>Lihat <a href="/ms/services/konsultasi-teknologi">perundingan teknologi</a> dan <a href="/ms/produk/website">perkhidmatan laman web</a> daripada Sentra.</p>""",
"faq": [("Berapa kerap laman web perlu disemak?","Semakan ringan setiap tiga bulan dan kemas kini keselamatan sebaik sahaja dikeluarkan."),
("Adakah sandaran sahaja mencukupi?","Tidak. Sandaran membantu pemulihan tetapi tidak mencegah serangan."),
("Adakah laman web statik lebih selamat?","Biasanya permukaan serangan lebih kecil, tetapi akaun hosting dan domain tetap perlu dilindungi.")]},
"zh": {
"title": "网站安全检查清单：被黑前要检查的 12 件事",
"description": "适用于机构、学校和政府部门的 12 项网站安全检查：更新、密码、备份、账号、网络赌博注入迹象以及被入侵后的处理。",
"category": "数字安全",
"lead": "大多数被黑的网站并非遭遇高级攻击，而是更新被拖延、密码太弱或旧账号未关闭。",
"wa_text": "您好 Sentra，我刚读了《网站安全检查清单》，想请你们检查我们的网站。",
"aside": [("/services/konsultasi-teknologi", "技术咨询"), ("/services/custom-software", "定制软件"), ("/produk/website", "网站")],
"body": """<p>可将此清单作为定期检查，例如每三个月一次，几乎都不需要昂贵工具。</p>
<h2 id="checklist">12 项检查是什么？</h2>
<ol><li>所有页面启用 HTTPS。</li><li>安装 CMS、主题和插件更新。</li><li>删除不用的插件和主题。</li><li>管理员密码强且唯一。</li><li>管理员登录、主机和域名邮箱启用两步验证。</li><li>清理账号列表，最小权限。</li><li>自动备份存放在网站服务器之外，并测试过恢复。</li><li>合理的文件权限。</li><li>限制登录尝试次数。</li><li>监控文件变更。</li><li>保护注册商和 DNS 账号。</li><li>日志保留足够久。</li></ol>
<h2 id="tanda-judi-online">网络赌博注入的迹象</h2>
<p>谷歌搜索结果显示赌博或老虎机标题、对谷歌来访者显示不同页面（伪装）、出现不明新文件或隐藏链接。不要只删除可见页面；应更换所有密码、从干净备份恢复并查找后门。</p>
<p>参见 Sentra 的<a href="/zh/services/konsultasi-teknologi">技术咨询</a>和<a href="/zh/produk/website">网站服务</a>。</p>""",
"faq": [("网站多久检查一次？","每三个月做一次轻量检查，安全更新发布后立即安装。"),
("只有备份够吗？","不够。备份帮助恢复，但不能预防攻击。"),
("静态网站更安全吗？","通常攻击面小得多，但主机和域名账号仍需保护。")]},
"ko": {
"title": "웹사이트 보안 체크리스트: 해킹당하기 전에 확인할 12가지",
"description": "기관·학교·사무실을 위한 12가지 웹사이트 보안 점검: 업데이트, 비밀번호, 백업, 계정, 온라인 도박 삽입 징후, 피해 시 대응.",
"category": "디지털 보안",
"lead": "해킹당한 웹사이트 대부분은 정교한 공격이 아니라 미뤄진 업데이트, 약한 비밀번호, 방치된 옛 계정 때문입니다.",
"wa_text": "안녕하세요 Sentra, \"웹사이트 보안 체크리스트\" 글을 읽고 우리 웹사이트 점검을 요청하고 싶습니다.",
"aside": [("/services/konsultasi-teknologi", "기술 컨설팅"), ("/services/custom-software", "맞춤 소프트웨어"), ("/produk/website", "웹사이트")],
"body": """<p>이 목록을 3개월마다 같은 주기적 점검으로 활용하세요. 대부분 비싼 도구가 필요 없습니다.</p>
<h2 id="checklist">12가지 점검 항목</h2>
<ol><li>모든 페이지 HTTPS 적용.</li><li>CMS, 테마, 플러그인 업데이트 설치.</li><li>사용하지 않는 플러그인·테마 삭제.</li><li>강력하고 고유한 관리자 비밀번호.</li><li>관리자 로그인, 호스팅, 도메인 이메일에 2단계 인증.</li><li>계정 목록 정리와 최소 권한.</li><li>웹 서버 밖에 저장되고 복원 테스트를 거친 자동 백업.</li><li>적절한 파일 권한.</li><li>로그인 시도 제한.</li><li>파일 변경 모니터링.</li><li>도메인 등록기관·DNS 계정 보호.</li><li>충분한 기간의 로그 보관.</li></ol>
<h2 id="tanda-judi-online">온라인 도박 삽입 징후</h2>
<p>구글 검색 결과에 도박·슬롯 제목이 보이거나, 구글 방문자에게만 다른 페이지가 보이거나(클로킹), 모르는 새 파일과 숨은 링크가 있는 경우입니다. 보이는 페이지만 지우지 말고 모든 비밀번호를 바꾸고 깨끗한 백업으로 복원하며 백도어를 찾으세요.</p>
<p>Sentra의 <a href="/ko/services/konsultasi-teknologi">기술 컨설팅</a>과 <a href="/ko/produk/website">웹사이트 서비스</a>를 확인하세요.</p>""",
"faq": [("웹사이트는 얼마나 자주 점검해야 하나요?","3개월마다 가벼운 점검을 하고 보안 업데이트는 나오는 즉시 설치하세요."),
("백업만으로 충분한가요?","아닙니다. 백업은 복구에 도움이 되지만 공격을 막지는 못합니다."),
("정적 웹사이트가 더 안전한가요?","공격 표면이 훨씬 작지만 호스팅과 도메인 계정은 여전히 보호해야 합니다.")]},
}
