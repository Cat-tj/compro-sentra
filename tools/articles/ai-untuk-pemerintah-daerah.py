SLUG = "ai-untuk-pemerintah-daerah"
DATE = "2026-11-02"
COVER = "/assets/img/art/blog-ai-pemda.webp"
OG_IMAGE = "/assets/og/art-blog-ai-pemda.jpg"

LANGS = {
"": {
"title": "AI untuk Pemerintah Daerah: Asisten Dokumen yang Datanya Tidak Keluar",
"description": "Contoh pemakaian AI untuk pemda yang realistis: tanya jawab peraturan, ringkasan rapat, dan pencarian arsip, dengan syarat kontrol data, rujukan sumber, dan peninjauan manusia.",
"category": "AI & data",
"lead": "AI berguna bagi pemda bila dibatasi pada pekerjaan yang jelas, memakai dokumen sendiri, dan jawabannya selalu bisa ditelusuri ke sumber.",
"wa_text": "Halo Sentra, saya baru membaca artikel \"AI untuk Pemerintah Daerah\" dan ingin diskusi pilot untuk instansi kami.",
"aside": [("/services/private-llm", "Private LLM"), ("/industri/pemerintahan", "Solusi pemerintahan"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT untuk perusahaan: risiko data dan alternatif")],
"body": """<p>Pemda menyimpan banyak dokumen: peraturan, surat edaran, notulen rapat, laporan, dan arsip. Pegawai sering menghabiskan waktu mencari dan merangkum. Asisten AI berbasis dokumen sendiri bisa membantu di sini, tanpa mengirim isi dokumen ke layanan luar bila dijalankan di infrastruktur instansi.</p>
<h2 id="contoh-pemakaian">Pemakaian apa yang realistis?</h2>
<ul><li><strong>Tanya jawab peraturan.</strong> Pegawai bertanya "apa ketentuan perjalanan dinas untuk kegiatan X?", sistem mencari di dokumen yang diunggah dan menjawab dengan rujukan pasal atau halaman.</li><li><strong>Ringkasan rapat.</strong> Rekaman atau transkrip rapat diringkas menjadi poin keputusan dan tindak lanjut untuk ditinjau notulis.</li><li><strong>Pencarian arsip.</strong> Mencari surat atau dokumen berdasarkan isi, bukan hanya nomor atau judul.</li><li><strong>Draf awal surat dan laporan</strong> dari templat dan data yang sudah ada, untuk disunting pegawai.</li><li><strong>Layanan informasi warga</strong> yang menjawab pertanyaan umum dari daftar layanan resmi.</li></ul>
<h2 id="data-tidak-keluar">Mengapa data tidak boleh sembarangan keluar?</h2>
<p>Dokumen pemda bisa memuat data pribadi, data keuangan, atau dokumen yang belum dipublikasikan. Menempelkannya ke layanan AI publik berarti data diproses di luar kendali instansi. Opsi yang lebih terkendali adalah menjalankan model di server instansi atau pusat data yang disetujui. Pertimbangan umumnya ada di <a href="/blog/chatgpt-untuk-perusahaan">ChatGPT untuk perusahaan</a>, dan perhitungan perangkat di <a href="/blog/server-ai-on-premise">server AI on-premise</a>.</p>
<h2 id="rujukan-sumber">Mengapa rujukan sumber wajib?</h2>
<p>Model bahasa bisa menjawab dengan yakin padahal salah. Untuk dokumen resmi, setiap jawaban harus menunjukkan dokumen dan bagian yang dipakai, supaya pegawai bisa memeriksanya. Jawaban tanpa rujukan sebaiknya tidak dipakai untuk keputusan. Sistem juga perlu menjawab "tidak ditemukan" bila memang tidak ada di dokumen.</p>
<h2 id="hak-akses">Siapa boleh melihat apa?</h2>
<p>Tidak semua dokumen untuk semua pegawai. Asisten harus mengikuti hak akses yang ada: pengguna hanya mendapat jawaban dari dokumen yang memang boleh dibukanya. Catat siapa bertanya apa untuk audit, dengan memperhatikan privasi pegawai.</p>
<h2 id="pilot">Bagaimana memulai dengan aman?</h2>
<ol><li>Pilih satu kumpulan dokumen yang rapi, misalnya peraturan kepegawaian atau SOP satu dinas.</li><li>Siapkan 30 sampai 50 pertanyaan uji dengan jawaban yang sudah diketahui.</li><li>Jalankan dengan sekelompok kecil pegawai selama beberapa minggu.</li><li>Nilai ketepatan, rujukan, dan manfaat waktu. Perbaiki sebelum diperluas.</li><li>Tetapkan aturan pemakaian: AI membantu, keputusan tetap pada pejabat berwenang.</li></ol>
<h2 id="kaitan-spbe">Kaitannya dengan SPBE dan Satu Data</h2>
<p>AI bekerja lebih baik bila dokumen dan data sudah tertata. Pekerjaan merapikan arsip dan standar data yang dibahas di <a href="/blog/spbe-pemda-persiapan">artikel SPBE</a> dan <a href="/blog/satu-data-daerah-dashboard">Satu Data Daerah</a> sekaligus menjadi fondasi asisten AI.</p>
<p>Sentra membangun asisten AI di infrastruktur Anda. Lihat <a href="/services/private-llm">layanan Private LLM</a> dan <a href="/industri/pemerintahan">solusi pemerintahan</a>.</p>""",
"faq": [("Apakah AI boleh dipakai untuk membuat keputusan pemerintahan?","AI sebaiknya hanya membantu mencari, merangkum, dan menyusun draf. Keputusan dan tanggung jawab tetap pada pejabat berwenang, dengan peninjauan manusia."),
("Bagaimana mencegah AI mengarang jawaban?","Gunakan pencarian di dokumen resmi dengan rujukan wajib, batasi jawaban pada isi dokumen, dan sediakan respons \"tidak ditemukan\". Tidak ada jaminan nol kesalahan, jadi peninjauan manusia tetap perlu."),
("Apakah perlu server khusus?","Tergantung model dan jumlah pengguna. Untuk pilot kecil sering cukup satu server dengan GPU. Hitung setelah pilot, seperti dibahas di artikel server AI on-premise."),
("Dokumen apa yang sebaiknya tidak dimasukkan?","Dokumen berklasifikasi tinggi dan data pribadi sensitif sebaiknya dikecualikan sampai kebijakan akses dan keamanan jelas.")]},
"en": {
"title": "AI for Local Government: A Document Assistant Where Data Stays In-House",
"description": "Realistic AI uses for local government: regulation Q&A, meeting summaries and archive search, with the conditions of data control, source references and human review.",
"category": "AI & data",
"lead": "AI helps local government when limited to clear tasks, using its own documents, with every answer traceable to a source.",
"wa_text": "Hello Sentra, I just read \"AI for Local Government\" and would like to discuss a pilot for our agency.",
"aside": [("/services/private-llm", "Private LLM"), ("/industri/pemerintahan", "Government solutions"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT for business: data risks and alternatives")],
"body": """<p>Local governments hold many documents: regulations, circulars, meeting minutes, reports and archives. Staff often spend time searching and summarising. An AI assistant built on your own documents can help here, without sending document content to an outside service when run on the agency's infrastructure.</p>
<h2 id="contoh-pemakaian">Which uses are realistic?</h2>
<ul><li><strong>Regulation Q&A.</strong> Staff ask "what are the travel rules for activity X?", the system searches the uploaded documents and answers with an article or page reference.</li><li><strong>Meeting summaries.</strong> A recording or transcript is summarised into decision points and follow-ups for the note-taker to review.</li><li><strong>Archive search.</strong> Find letters or documents by content, not just number or title.</li><li><strong>First drafts of letters and reports</strong> from templates and existing data, for staff to edit.</li><li><strong>Citizen information service</strong> answering common questions from the official service list.</li></ul>
<h2 id="data-tidak-keluar">Why must data not leave carelessly?</h2>
<p>Government documents can hold personal data, financial data, or unpublished material. Pasting them into a public AI service means the data is processed outside the agency's control. A more controlled option is running the model on agency servers or an approved data centre. General considerations are in <a href="/en/blog/chatgpt-untuk-perusahaan">ChatGPT for business</a>, and hardware sizing in <a href="/en/blog/server-ai-on-premise">on-premise AI server</a>.</p>
<h2 id="rujukan-sumber">Why are source references mandatory?</h2>
<p>Language models can answer confidently and be wrong. For official documents, every answer must show the document and section used, so staff can check it. An answer without a reference should not be used for decisions. The system must also say "not found" when the answer is not in the documents.</p>
<h2 id="hak-akses">Who may see what?</h2>
<p>Not every document is for every employee. The assistant must follow existing access rights: users only get answers from documents they may open. Log who asked what for audit, mindful of staff privacy.</p>
<h2 id="pilot">How to start safely</h2>
<ol><li>Pick one tidy set of documents, such as staffing regulations or one office's SOPs.</li><li>Prepare 30 to 50 test questions with known answers.</li><li>Run it with a small group of staff for several weeks.</li><li>Assess accuracy, references and time saved. Fix before expanding.</li><li>Set usage rules: AI assists, decisions remain with the authorised official.</li></ol>
<h2 id="kaitan-spbe">The link to SPBE and One Data</h2>
<p>AI works better when documents and data are well organised. The archive tidying and data standards covered in the <a href="/en/blog/spbe-pemda-persiapan">SPBE article</a> and <a href="/en/blog/satu-data-daerah-dashboard">Regional One Data</a> also form the foundation for an AI assistant.</p>
<p>Sentra builds AI assistants on your infrastructure. See the <a href="/en/services/private-llm">Private LLM service</a> and <a href="/en/industri/pemerintahan">government solutions</a>.</p>""",
"faq": [("May AI be used to make government decisions?","AI should only help search, summarise and draft. Decisions and responsibility stay with the authorised official, with human review."),
("How do you stop AI inventing answers?","Use retrieval over official documents with mandatory references, limit answers to document content, and provide a \"not found\" response. There is no guarantee of zero errors, so human review remains necessary."),
("Is a special server needed?","It depends on the model and number of users. For a small pilot one GPU server is often enough. Size it after the pilot, as covered in the on-premise AI server article."),
("Which documents should not be included?","Highly classified documents and sensitive personal data should be excluded until access and security policy are clear.")]},
"ms": {
"title": "AI untuk Kerajaan Tempatan: Pembantu Dokumen yang Datanya Kekal Dalaman",
"description": "Penggunaan AI yang realistik untuk kerajaan tempatan dengan kawalan data dan rujukan sumber.",
"category": "AI & data",
"lead": "AI berguna jika dihadkan kepada tugas yang jelas, menggunakan dokumen sendiri dan jawapan boleh dijejak kepada sumber.",
"wa_text": "Hai Sentra, saya baru membaca artikel \"AI untuk Kerajaan Tempatan\" dan ingin berbincang tentang pilot.",
"aside": [("/services/private-llm", "Private LLM"), ("/industri/pemerintahan", "Penyelesaian kerajaan"), ("/blog/chatgpt-untuk-perusahaan", "ChatGPT untuk syarikat")],
"body": """<p>Pembantu AI berasaskan dokumen sendiri boleh membantu mencari dan merumus dokumen tanpa menghantar kandungan ke perkhidmatan luar jika dijalankan pada infrastruktur agensi.</p>
<h2 id="contoh-pemakaian">Penggunaan yang realistik</h2>
<p>Soal jawab peraturan dengan rujukan, ringkasan mesyuarat untuk disemak pencatat, carian arkib mengikut kandungan dan draf awal surat untuk disunting.</p>
<h2 id="rujukan-sumber">Rujukan sumber wajib</h2>
<p>Model boleh menjawab dengan yakin tetapi salah, maka setiap jawapan mesti menunjukkan dokumen dan bahagian yang digunakan. Keputusan kekal pada pegawai yang berkuasa. Lihat <a href="/ms/services/private-llm">perkhidmatan Private LLM</a> dan <a href="/ms/blog/chatgpt-untuk-perusahaan">ChatGPT untuk syarikat</a>.</p>""",
"faq": [("Bolehkah AI digunakan untuk membuat keputusan?","AI hanya membantu mencari, merumus dan menyusun draf; keputusan kekal pada pegawai berkuasa."),
("Bagaimana mengelak AI mereka jawapan?","Gunakan carian pada dokumen rasmi dengan rujukan wajib dan semakan manusia.")]},
"zh": {
"title": "地方政府的 AI：数据不出门的文档助手",
"description": "地方政府切合实际的 AI 用法：法规问答、会议纪要摘要和档案检索，前提是数据可控、有来源引用并经人工审核。",
"category": "AI 与数据",
"lead": "当 AI 限定在明确任务、使用自己的文档并且每个答案都能追溯到来源时，对地方政府才有帮助。",
"wa_text": "您好 Sentra，我刚读了《地方政府的 AI》，想讨论我们机构的试点。",
"aside": [("/services/private-llm", "私有 LLM"), ("/industri/pemerintahan", "政府解决方案"), ("/blog/chatgpt-untuk-perusahaan", "企业使用 ChatGPT")],
"body": """<p>基于自有文档的 AI 助手可帮助检索和摘要，并且在机构自己的基础设施上运行时，文档内容不会发送到外部服务。</p>
<h2 id="contoh-pemakaian">切合实际的用法</h2>
<p>带条款或页码引用的法规问答、供记录员审核的会议摘要、按内容检索档案，以及供员工修改的信函初稿。</p>
<h2 id="rujukan-sumber">必须有来源引用</h2>
<p>语言模型可能很自信却答错，因此每个答案都必须指出所用文档和章节。决策仍由有权限的官员负责。参见<a href="/zh/services/private-llm">私有 LLM 服务</a>和<a href="/zh/blog/chatgpt-untuk-perusahaan">企业使用 ChatGPT</a>。</p>""",
"faq": [("AI 可以用来做政府决策吗？","AI 只应协助检索、摘要和起草，决策仍由有权限的官员负责。"),
("如何避免 AI 编造答案？","对官方文档检索并强制引用来源，同时保留人工审核。")]},
"ko": {
"title": "지방정부를 위한 AI: 데이터가 밖으로 나가지 않는 문서 도우미",
"description": "지방정부에 현실적인 AI 활용: 규정 질의응답, 회의 요약, 문서 검색, 그리고 데이터 통제·출처 표시·사람의 검토 조건.",
"category": "AI·데이터",
"lead": "AI는 명확한 업무에 한정하고, 자체 문서를 쓰며, 모든 답이 출처로 추적될 때 지방정부에 도움이 됩니다.",
"wa_text": "안녕하세요 Sentra, \"지방정부를 위한 AI\" 글을 읽고 우리 기관의 파일럿을 논의하고 싶습니다.",
"aside": [("/services/private-llm", "프라이빗 LLM"), ("/industri/pemerintahan", "정부 솔루션"), ("/blog/chatgpt-untuk-perusahaan", "기업의 ChatGPT 사용")],
"body": """<p>자체 문서를 기반으로 한 AI 도우미는 검색과 요약을 도울 수 있으며, 기관 인프라에서 실행하면 문서 내용이 외부 서비스로 나가지 않습니다.</p>
<h2 id="contoh-pemakaian">현실적인 활용</h2>
<p>조항·쪽수를 표시하는 규정 질의응답, 기록 담당자가 검토할 회의 요약, 내용 기반 문서 검색, 직원이 고칠 서한 초안입니다.</p>
<h2 id="rujukan-sumber">출처 표시는 필수</h2>
<p>언어 모델은 자신 있게 틀릴 수 있으므로 모든 답은 사용한 문서와 부분을 보여줘야 합니다. 결정은 권한 있는 공무원에게 남습니다. <a href="/ko/services/private-llm">프라이빗 LLM 서비스</a>와 <a href="/ko/blog/chatgpt-untuk-perusahaan">기업의 ChatGPT 사용</a>을 확인하세요.</p>""",
"faq": [("AI로 행정 결정을 내려도 되나요?","AI는 검색, 요약, 초안 작성만 돕고 결정과 책임은 권한 있는 공무원에게 있습니다."),
("AI가 답을 지어내지 않게 하려면?","공식 문서 검색과 출처 표시를 강제하고 사람이 검토하세요.")]},
}
