SLUG = "chatgpt-untuk-perusahaan"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-chatgpt-perusahaan.webp"
OG_IMAGE = "/assets/og/art-blog-chatgpt-perusahaan.jpg"

LANGS = {
"": {
"title": "ChatGPT untuk Perusahaan: Risiko Data dan Alternatif On-Premise",
"description": "Apa yang perlu dicek sebelum karyawan memakai ChatGPT atau AI publik lain untuk dokumen kantor, dan kapan model on-premise atau private LLM lebih masuk akal.",
"category": "AI & data",
"lead": "Karyawan sudah memakai AI publik, dengan atau tanpa izin. Lebih baik perusahaan menetapkan aturan dan pilihan yang jelas daripada berpura-pura itu tidak terjadi.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"ChatGPT untuk Perusahaan\" dan ingin diskusi soal AI yang datanya tetap di perusahaan.",
"aside": [("/services/private-llm", "Private LLM untuk perusahaan"), ("/produk/sentrai", "SentrAI"), ("/industri/korporasi", "Solusi korporasi")],
"body": """<p>Pertanyaan yang tepat bukan "boleh pakai ChatGPT atau tidak", tetapi "data apa yang boleh dimasukkan ke layanan mana". Layanan AI publik berguna untuk tugas umum. Masalah muncul saat dokumen internal, data pelanggan, atau kontrak ikut dimasukkan tanpa aturan.</p>
<h2 id="risiko-data">Apa risiko data yang perlu dipahami?</h2>
<ul><li><strong>Data keluar dari perusahaan.</strong> Teks yang diketik diproses di server penyedia. Perlakuan datanya (disimpan berapa lama, dipakai melatih model atau tidak) berbeda antar paket dan penyedia, dan bisa berubah. Baca syarat paket yang benar-benar dipakai, jangan mengandalkan ingatan.</li><li><strong>Akun pribadi.</strong> Karyawan yang memakai akun gratis pribadi membuat perusahaan tidak punya kendali atau jejak audit.</li><li><strong>Data pribadi.</strong> Memasukkan data pelanggan atau karyawan bisa bertentangan dengan kewajiban perlindungan data pribadi.</li><li><strong>Kerahasiaan.</strong> Dokumen tender, harga, atau strategi yang bocor sulit ditarik kembali.</li></ul>
<h2 id="aturan-sederhana">Aturan sederhana yang bisa dimulai minggu ini</h2>
<ol><li>Tetapkan tiga kelas data: boleh dimasukkan, boleh dengan anonimisasi, dan dilarang (kontrak, data pelanggan, kredensial, kode sumber rahasia).</li><li>Sediakan akun perusahaan dengan pengaturan privasi yang sudah dicek, bukan akun pribadi.</li><li>Latih karyawan dengan contoh nyata apa yang boleh dan tidak.</li><li>Catat siapa memakai apa untuk keperluan audit.</li></ol>
<h2 id="kapan-on-premise">Kapan on-premise atau private LLM lebih masuk akal?</h2>
<ul><li>Dokumen yang ingin dibantu AI termasuk kategori rahasia atau diatur regulasi.</li><li>Instansi atau industri mewajibkan data tetap di lingkungan sendiri.</li><li>Ada kebutuhan menjawab dari dokumen internal (SOP, kontrak, laporan) dengan rujukan sumber.</li><li>Pemakaian cukup besar sehingga biaya per pemakaian layanan publik jadi perhitungan.</li></ul>
<h2 id="imbalan-on-premise">Apa yang harus diterima kalau memilih on-premise?</h2>
<p>Model terbuka yang dijalankan sendiri umumnya lebih kecil daripada model publik terbesar, sehingga kualitas pada tugas sulit bisa berbeda. Anda juga menanggung perangkat keras (GPU, RAM, penyimpanan), pembaruan, dan pengamanan. Karena itu mulailah dari satu kasus penggunaan yang jelas, misalnya tanya jawab SOP, lalu ukur hasilnya sebelum meluas.</p>
<h2 id="cara-menyusun-pilot">Bagaimana menyusun pilot yang masuk akal?</h2>
<p>Pilih satu kumpulan dokumen yang rapi, tetapkan 30 sampai 50 pertanyaan uji dengan jawaban yang sudah diketahui, jalankan dengan beberapa pengguna selama beberapa minggu, lalu nilai ketepatan jawaban dan kepercayaan pengguna. Keputusan membeli perangkat keras sebaiknya sesudah pilot, bukan sebelumnya.</p>
<p>Sentra membangun asisten AI di lingkungan perusahaan Anda. Lihat <a href="/services/private-llm">layanan Private LLM</a>, <a href="/produk/sentrai">SentrAI</a>, dan <a href="/industri/korporasi">solusi korporasi</a>.</p>""",
"faq": [("Apakah ChatGPT aman untuk data perusahaan?","Tergantung paket dan pengaturan. Paket bisnis biasanya punya kebijakan data berbeda dari akun gratis. Baca syarat terbaru penyedia dan tetapkan kelas data yang boleh dimasukkan."),
("Apakah private LLM selalu lebih baik?","Tidak. Ia lebih baik untuk kontrol data dan rujukan dokumen internal, tetapi kualitas pada tugas umum yang sulit bisa lebih rendah daripada model publik terbesar."),
("Berapa perangkat keras yang dibutuhkan?","Bergantung ukuran model dan jumlah pengguna. Tentukan setelah pilot, bukan sebelum."),
("Apakah karyawan perlu dilarang memakai AI publik?","Larangan total sering diabaikan. Lebih efektif memberi aturan kelas data dan alternatif resmi.")]},
"en": {
"title": "ChatGPT for Business: Data Risks and On-Premise Alternatives",
"description": "What to check before staff use ChatGPT or other public AI for office documents, and when an on-premise model or private LLM makes more sense.",
"category": "AI & data",
"lead": "Staff are already using public AI, with or without permission. It is better for a company to set clear rules and options than to pretend it is not happening.",
"wa_text": "Hello Sentra, I just read \"ChatGPT for Business\" and would like to discuss AI where data stays in the company.",
"aside": [("/services/private-llm", "Private LLM for companies"), ("/produk/sentrai", "SentrAI"), ("/industri/korporasi", "Corporate solutions")],
"body": """<p>The right question is not "may we use ChatGPT or not" but "which data may go into which service". Public AI services are useful for general tasks. Trouble starts when internal documents, customer data or contracts go in without rules.</p>
<h2 id="risiko-data">Which data risks should you understand?</h2>
<ul><li><strong>Data leaves the company.</strong> Typed text is processed on the provider's servers. How data is treated (retention, use for model training) differs between plans and providers and can change. Read the terms of the plan actually in use, do not rely on memory.</li><li><strong>Personal accounts.</strong> Staff using free personal accounts leave the company with no control or audit trail.</li><li><strong>Personal data.</strong> Entering customer or employee data may conflict with personal data protection duties.</li><li><strong>Confidentiality.</strong> Leaked tender documents, prices or strategy are hard to recall.</li></ul>
<h2 id="aturan-sederhana">Simple rules you can start this week</h2>
<ol><li>Set three data classes: allowed, allowed with anonymisation, and forbidden (contracts, customer data, credentials, secret source code).</li><li>Provide company accounts with privacy settings that have been checked, not personal ones.</li><li>Train staff with real examples of what is and is not allowed.</li><li>Record who uses what for audit purposes.</li></ol>
<h2 id="kapan-on-premise">When does on-premise or a private LLM make more sense?</h2>
<ul><li>The documents you want AI to help with are confidential or regulated.</li><li>Your agency or industry requires data to stay in your own environment.</li><li>You need answers from internal documents (SOPs, contracts, reports) with source references.</li><li>Usage is large enough that per-use cost of public services becomes a factor.</li></ul>
<h2 id="imbalan-on-premise">What must you accept with on-premise?</h2>
<p>Open models you run yourself are generally smaller than the largest public models, so quality on hard tasks can differ. You also carry the hardware (GPU, RAM, storage), updates and security. So start with one clear use case, such as SOP question answering, and measure results before expanding.</p>
<h2 id="cara-menyusun-pilot">How to set up a sensible pilot</h2>
<p>Pick one tidy set of documents, define 30 to 50 test questions with known answers, run it with a few users for several weeks, then assess answer accuracy and user trust. Decide on hardware after the pilot, not before.</p>
<p>Sentra builds AI assistants inside your company environment. See the <a href="/en/services/private-llm">Private LLM service</a>, <a href="/en/produk/sentrai">SentrAI</a> and <a href="/en/industri/korporasi">corporate solutions</a>.</p>""",
"faq": [("Is ChatGPT safe for company data?","It depends on the plan and settings. Business plans usually have different data policies from free accounts. Read the provider's current terms and define which data classes may be entered."),
("Is a private LLM always better?","No. It is better for data control and internal-document references, but quality on hard general tasks can be lower than the largest public models."),
("How much hardware is needed?","It depends on model size and number of users. Decide after a pilot, not before."),
("Should staff be banned from public AI?","Total bans are often ignored. Data-class rules and an official alternative work better.")]},
"ms": {
"title": "ChatGPT untuk Syarikat: Risiko Data dan Alternatif On-Premise",
"description": "Apa yang perlu disemak sebelum pekerja menggunakan ChatGPT untuk dokumen pejabat, dan bila model on-premise lebih sesuai.",
"category": "AI & data",
"lead": "Pekerja sudah menggunakan AI awam, dengan atau tanpa kebenaran. Lebih baik syarikat menetapkan peraturan yang jelas.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"ChatGPT untuk Syarikat\" dan ingin berbincang tentang AI yang datanya kekal dalam syarikat.",
"aside": [("/services/private-llm", "Private LLM untuk syarikat"), ("/produk/sentrai", "SentrAI"), ("/industri/korporasi", "Penyelesaian korporat")],
"body": """<p>Soalan yang tepat bukan "boleh guna ChatGPT atau tidak", tetapi "data apa boleh dimasukkan ke perkhidmatan mana". Masalah timbul apabila dokumen dalaman, data pelanggan atau kontrak dimasukkan tanpa peraturan.</p>
<h2 id="risiko-data">Apakah risiko data?</h2>
<ul><li>Data keluar dari syarikat dan diproses di pelayan penyedia; layanan data berbeza antara pelan dan boleh berubah.</li><li>Akaun peribadi menyebabkan syarikat tiada kawalan atau jejak audit.</li><li>Data peribadi dan dokumen sulit sukar ditarik balik.</li></ul>
<h2 id="aturan-sederhana">Peraturan mudah untuk bermula</h2>
<p>Tetapkan tiga kelas data (dibenarkan, dibenarkan dengan penyamaran, dilarang), sediakan akaun syarikat dan latih pekerja dengan contoh sebenar. Model on-premise sesuai apabila dokumen sulit atau terkawal, dan bermula dengan satu kes penggunaan yang jelas.</p>
<p>Lihat <a href="/ms/services/private-llm">perkhidmatan Private LLM</a> dan <a href="/ms/produk/sentrai">SentrAI</a> daripada Sentra.</p>""",
"faq": [("Adakah ChatGPT selamat untuk data syarikat?","Bergantung pada pelan dan tetapan. Baca syarat terkini penyedia dan tetapkan kelas data."),
("Adakah private LLM sentiasa lebih baik?","Tidak. Ia lebih baik untuk kawalan data, tetapi kualiti tugas umum yang sukar boleh lebih rendah."),
("Perlukah pekerja dilarang menggunakan AI awam?","Larangan menyeluruh sering diabaikan. Peraturan kelas data dan alternatif rasmi lebih berkesan.")]},
"zh": {
"title": "企业使用 ChatGPT：数据风险与本地部署替代方案",
"description": "员工用 ChatGPT 等公共 AI 处理办公文件前应检查什么，以及何时本地部署或私有 LLM 更合适。",
"category": "AI 与数据",
"lead": "员工已经在用公共 AI，无论是否获批。公司最好制定明确规则和选项。",
"wa_text": "您好 Sentra，我刚读了《企业使用 ChatGPT》，想讨论数据留在公司内的 AI。",
"aside": [("/services/private-llm", "企业私有 LLM"), ("/produk/sentrai", "SentrAI"), ("/industri/korporasi", "企业解决方案")],
"body": """<p>正确的问题不是“能不能用 ChatGPT”，而是“哪些数据可以放进哪个服务”。当内部文件、客户数据或合同在没有规则的情况下被输入时，就会出问题。</p>
<h2 id="risiko-data">有哪些数据风险？</h2>
<ul><li>数据离开公司，在服务商服务器上处理；不同套餐的数据处理方式不同且可能变化，请阅读实际使用套餐的条款。</li><li>个人账号让公司失去控制和审计记录。</li><li>个人数据和机密文件一旦泄露难以收回。</li></ul>
<h2 id="aturan-sederhana">可以立即开始的简单规则</h2>
<p>设定三类数据（允许、匿名后允许、禁止），提供公司账号，并用真实案例培训员工。文件机密或受监管时，本地部署更合适，并从一个明确的用例开始。</p>
<p>参见 Sentra 的<a href="/zh/services/private-llm">私有 LLM 服务</a>和 <a href="/zh/produk/sentrai">SentrAI</a>。</p>""",
"faq": [("ChatGPT 对公司数据安全吗？","取决于套餐和设置。请阅读服务商最新条款并设定可输入的数据类别。"),
("私有 LLM 一定更好吗？","不一定。数据可控性更强，但在困难的通用任务上质量可能低于最大的公共模型。"),
("应该禁止员工使用公共 AI 吗？","全面禁止常被无视，数据分类规则加官方替代方案更有效。")]},
"ko": {
"title": "기업의 ChatGPT 사용: 데이터 위험과 온프레미스 대안",
"description": "직원이 ChatGPT 등 공개 AI로 업무 문서를 다루기 전에 확인할 점과, 온프레미스·프라이빗 LLM이 적합한 경우.",
"category": "AI·데이터",
"lead": "직원들은 허락 여부와 관계없이 이미 공개 AI를 쓰고 있습니다. 명확한 규칙과 선택지를 두는 편이 낫습니다.",
"wa_text": "안녕하세요 Sentra, \"기업의 ChatGPT 사용\" 글을 읽고 데이터가 회사 안에 남는 AI에 대해 상담하고 싶습니다.",
"aside": [("/services/private-llm", "기업용 프라이빗 LLM"), ("/produk/sentrai", "SentrAI"), ("/industri/korporasi", "기업 솔루션")],
"body": """<p>올바른 질문은 \"ChatGPT를 써도 되는가\"가 아니라 \"어떤 데이터를 어떤 서비스에 넣어도 되는가\"입니다. 내부 문서, 고객 데이터, 계약서가 규칙 없이 입력될 때 문제가 생깁니다.</p>
<h2 id="risiko-data">어떤 데이터 위험이 있나요?</h2>
<ul><li>입력한 텍스트는 제공업체 서버에서 처리되며 요금제마다 데이터 취급이 다르고 바뀔 수 있습니다. 실제 사용하는 요금제의 약관을 읽으세요.</li><li>개인 계정을 쓰면 회사가 통제와 감사 기록을 잃습니다.</li><li>개인정보와 기밀 문서는 유출되면 회수하기 어렵습니다.</li></ul>
<h2 id="aturan-sederhana">이번 주부터 할 수 있는 간단한 규칙</h2>
<p>데이터를 허용, 익명화 후 허용, 금지의 세 등급으로 나누고, 회사 계정을 제공하며, 실제 사례로 교육하세요. 문서가 기밀이거나 규제 대상이면 온프레미스가 적합하며, 명확한 하나의 사례로 시작하세요.</p>
<p>Sentra의 <a href="/ko/services/private-llm">프라이빗 LLM 서비스</a>와 <a href="/ko/produk/sentrai">SentrAI</a>를 확인하세요.</p>""",
"faq": [("ChatGPT는 회사 데이터에 안전한가요?","요금제와 설정에 따라 다릅니다. 제공업체의 최신 약관을 읽고 입력 가능한 데이터 등급을 정하세요."),
("프라이빗 LLM이 항상 더 좋은가요?","아닙니다. 데이터 통제에는 유리하지만 어려운 일반 작업에서는 최대 규모의 공개 모델보다 품질이 낮을 수 있습니다."),
("직원의 공개 AI 사용을 금지해야 하나요?","전면 금지는 무시되기 쉽습니다. 데이터 등급 규칙과 공식 대안이 더 효과적입니다.")]},
}
