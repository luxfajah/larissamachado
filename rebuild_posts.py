html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Helper to build a post section
def make_post_section(post_num, section_id, theme, badge, cards_html, dots_html, likes, caption_preview, full_caption):
    return f'''<!-- ==================== SEÇÃO 13: SLIDE {post_num + 1} - POST {post_num} ==================== -->
        <section class="slide future" id="{section_id}" data-theme="{theme}">
          <div class="slide-content post-slide-layout">

            <!-- Coluna Esquerda: iPhone Mockup Grande com Carousel Interno -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame iphone-post-hero-frame">
                <div class="iphone-notch-bar">
                  <span class="iphone-time">9:41</span>
                  <div class="iphone-dynamic-island"></div>
                  <div class="iphone-status-icons">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M1 6l11 11L23 6"/></svg>
                  </div>
                </div>
                <div class="ig-post-view">
                  <!-- Instagram Post Header -->
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8E8E8E" stroke-width="2"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
                  </div>
                  <!-- Carousel Viewport with Overlay Controls -->
                  <div class="ig-post-carousel-viewport" data-post-carousel="{post_num}">
                    {cards_html}
                    <button class="ig-carousel-prev prev-card-btn">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M15 18l-6-6 6-6"/></svg>
                    </button>
                    <button class="ig-carousel-next next-card-btn">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M9 18l6-6-6-6"/></svg>
                    </button>
                    <div class="ig-carousel-dots card-dots-row">{dots_html}</div>
                  </div>
                  <!-- Post Actions -->
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>{likes}</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> {caption_preview}</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Apenas Copy / Legenda -->
            <div class="post-col-right post-copy-only">
              <span class="post-viewer-cat-badge">{badge}</span>
              <div class="post-copy-box post-copy-full">
                <div class="copy-box-header">
                  <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                  <div class="copy-user-meta">
                    <span class="copy-handle">dra.larissamachado</span>
                    <span class="copy-sub">Legenda Oficial</span>
                  </div>
                </div>
                <div class="copy-scroll-body">
                  {full_caption}
                </div>
                <div class="copy-actions-bar">
                  <div class="action-icons-left">
                    <span class="action-icon red-like">❤️ {likes}</span>
                    <span class="action-icon">💬</span>
                  </div>
                  <span class="action-icon">🔖</span>
                </div>
              </div>
            </div>

          </div>
        </section>
'''

# Define each post's data
posts = [
    {
        "num": 1,
        "section_id": "slide-social-post-1",
        "theme": "off-white",
        "badge": "CONTEÚDO 1 [PREPARAÇÃO DA AUDIÊNCIA] · Carrossel 6 Cards",
        "cards": [
            "./redes-sociais/1.1.jpg",
            "./redes-sociais/1.2+.jpg",
            "./redes-sociais/1.3.jpg",
            "./redes-sociais/1.4.jpg",
            "./redes-sociais/1.5.jpg",
            "./redes-sociais/1.6.jpg",
        ],
        "likes": "248 curtidas",
        "caption_preview": "A gente aprende a culpar o cansaço por tudo...",
        "full_caption": '''<p>A gente aprende a culpar o cansaço por tudo o que aparece no rosto, mas nem sempre ele é o culpado. Com o tempo, a pálpebra superior perde firmeza e passa a projetar uma sombra discreta sobre o olho e é essa sombra que muda a mensagem que o seu rosto transmite. O olhar comunica cansaço, seriedade, abatimento, mesmo quando por dentro é o oposto...</p>
                  <p>Por isso, aqui no consultório, a ordem é sempre essa: entender primeiro o que te trouxe até aqui e decidir depois a melhor intervenção.</p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
    {
        "num": 2,
        "section_id": "slide-social-post-2",
        "theme": "off-white",
        "badge": "CONTEÚDO 2 [EDUCACIONAL] · Carrossel 6 Cards",
        "cards": [
            "./redes-sociais/2.1.jpg",
            "./redes-sociais/2.2.jpg",
            "./redes-sociais/2.3.jpg",
            "./redes-sociais/2.4.jpg",
            "./redes-sociais/2.5.jpg",
            "./redes-sociais/2.6.jpg",
        ],
        "likes": "312 curtidas",
        "caption_preview": "Toda semana, as mesmas perguntas aparecem...",
        "full_caption": '''<p>Toda semana, as mesmas perguntas aparecem no consultório. E faz todo sentido: ninguém decide nada sobre os próprios olhos sem antes tirar o medo do caminho.</p>
                  <p>Então, reuni aqui as dúvidas que mais escuto. Respondi cada uma como respondo pessoalmente: com a informação que você precisa para pensar com clareza.</p>
                  <p>Você vai reparar que não tem "resultado garantido" nem "transformação". Tem explicação. Porque a decisão é sua... O meu papel é fazer você entender antes de decidir.</p>
                  <p>Ficou alguma pergunta de fora? Pode me mandar que eu respondo.</p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
    {
        "num": 3,
        "section_id": "slide-social-post-3",
        "theme": "off-white",
        "badge": "CONTEÚDO 3 [EDUCACIONAL] · Carrossel 3 Cards",
        "cards": [
            "./redes-sociais/3.1.jpg",
            "./redes-sociais/3.2.jpg",
            "./redes-sociais/3.4.jpg",
        ],
        "likes": "189 curtidas",
        "caption_preview": '"E a cicatriz?" é quase sempre a primeira...',
        "full_caption": '''<p>Essa é uma pergunta clássica que merece um espaço só dela. Passa para o lado e confira os cards acima!</p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
    {
        "num": 4,
        "section_id": "slide-social-post-4",
        "theme": "off-white",
        "badge": "CONTEÚDO 4 [LOCAL DE ATENDIMENTO] · Single Card",
        "cards": [
            "./redes-sociais/4.jpg",
        ],
        "likes": "142 curtidas",
        "caption_preview": "Este é o meu local de atendimento atualmente...",
        "full_caption": '''<p>Este é o meu local de atendimento atualmente.</p>
                  <p>Para agendamento de consultas, clique diretamente no link da bio:<br><a href="https://share.google/9v6BVUdKtrHndWnxr" target="_blank" style="color:#00376B;font-weight:600;">share.google/9v6BVUdKtrHndWnxr</a></p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
    {
        "num": 5,
        "section_id": "slide-social-post-5",
        "theme": "off-white",
        "badge": "CONTEÚDO 5 [APRESENTAÇÃO PROFISSIONAL] · Carrossel 5 Cards",
        "cards": [
            "./redes-sociais/5.1.jpg",
            "./redes-sociais/5.2.jpg",
            "./redes-sociais/5.3.jpg",
            "./redes-sociais/5.4.jpg",
            "./redes-sociais/5.5.jpg",
        ],
        "likes": "405 curtidas",
        "caption_preview": "Seja oficialmente bem-vindo por aqui...",
        "full_caption": '''<p>Seja oficialmente bem-vindo por aqui. Meu objetivo nesta página é trazer informação embasada para você que tem interesse na temática.</p>
                  <p>Qualquer dúvida, por favor, meu direct está aberto para conversarmos.</p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
    {
        "num": 6,
        "section_id": "slide-social-post-6",
        "theme": "off-white",
        "badge": "CONTEÚDO 6 [EDUCACIONAL] · Single Card",
        "cards": [
            "./redes-sociais/6.jpg",
        ],
        "likes": "267 curtidas",
        "caption_preview": "Muita gente associa cirurgia de pálpebra a rejuvenescimento...",
        "full_caption": '''<p>Muita gente associa cirurgia de pálpebra a rejuvenescimento, mas a plástica ocular também trata condições que afetam a saúde e o funcionamento dos seus olhos.</p>
                  <p><strong>Ptose:</strong> é a queda da pálpebra superior. Com o tempo, o músculo enfraquece, cobrindo parte do olho. A cirurgia reposiciona a pálpebra na altura certa, devolvendo abertura ao olhar e conforto à visão.</p>
                  <p><strong>Tumores palpebrais:</strong> nem toda "verruguinha" é inofensiva. A plástica ocular cuida da remoção da lesão e da reconstrução da pálpebra, preservando função e estética.</p>
                  <p><strong>Obstrução das vias lacrimais:</strong> quando o canal de drenagem entope, a lágrima não tem para onde ir. A cirurgia reconstrói o caminho e resolve o incômodo de vez.</p>
                  <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>'''
    },
]

def build_cards_html(cards):
    out = ''
    for i, src in enumerate(cards):
        active = ' active' if i == 0 else ''
        out += f'    <img src="{src}" class="carousel-img{active}" alt="Card {i+1}">\n                    '
    return out.strip()

def build_dots_html(cards):
    out = ''
    for i in range(len(cards)):
        active = ' active' if i == 0 else ''
        out += f'<div class="card-dot{active}"></div>'
    return out

# Build all 6 sections
new_posts_html = ''
for p in posts:
    cards_html = build_cards_html(p['cards'])
    dots_html = build_dots_html(p['cards'])
    new_posts_html += make_post_section(
        post_num=p['num'],
        section_id=p['section_id'],
        theme=p['theme'],
        badge=p['badge'],
        cards_html=cards_html,
        dots_html=dots_html,
        likes=p['likes'],
        caption_preview=p['caption_preview'],
        full_caption=p['full_caption']
    )

start_marker = '<!-- ==================== SEÇÃO 13: SLIDE 2 - POST 1 (PREPARAÇÃO) ==================== -->'
end_marker = '<!-- ==================== MODAL OVERLAY DE STORIES EM TELA CHEIA (INSTAGRAM) ==================== -->'

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

if idx_start != -1 and idx_end != -1:
    html = html[:idx_start] + '\n        ' + new_posts_html + '\n        ' + html[idx_end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Successfully rebuilt all 6 post slides! ({len(html)} bytes total)')
else:
    print(f'Markers not found! start={idx_start}, end={idx_end}')
