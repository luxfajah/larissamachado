import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- ==================== SEÇÃO 13: SLIDE 1 - PERFIL & DESTAQUES FUNCIONAIS ==================== -->'
end_marker = '<!-- ==================== MODAL OVERLAY DE STORIES EM TELA CHEIA (INSTAGRAM) ==================== -->'

new_content = '''<!-- ==================== SEÇÃO 13: SLIDE 1 - PERFIL & DESTAQUES FUNCIONAIS ==================== -->
        <section class="slide future" id="slide-social-profile" data-theme="sand-paper">
          <div class="slide-content social-two-col-layout hero-profile-layout">
            
            <!-- Coluna Esquerda: Mockup iPhone Instagram Perfil Real em Destaque (~65%) -->
            <div class="social-col-left hero-iphone-col">
              <div class="iphone-mockup-frame hero-iphone-frame">
                <!-- Top Island & Status Bar -->
                <div class="iphone-notch-bar">
                  <span class="iphone-time">9:41</span>
                  <div class="iphone-dynamic-island"></div>
                  <div class="iphone-status-icons">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 21l3.54-.62C9.4 20.73 10.66 21 12 21c4.97 0 9-4.03 9-9s-4.03-9-9-9z"/></svg>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                  </div>
                </div>

                <!-- Instagram Mobile Header -->
                <div class="ig-app-header">
                  <div class="ig-username-badge">
                    <span class="ig-handle">dra.larissamachado</span>
                    <svg class="ig-verified-icon" width="14" height="14" viewBox="0 0 24 24" fill="none">
                      <path d="M12 2L15.09 3.26L18.4 2.84L19.92 5.82L23 6.94L22.84 10.29L24.78 13L23.12 15.91L23.63 19.23L20.42 20.21L18.73 23.09L15.48 22.38L12.78 24.36L10.08 22.38L6.83 23.09L5.14 20.21L1.93 19.23L2.44 15.91L0.78 13L2.72 10.29L2.56 6.94L5.64 5.82L7.16 2.84L10.47 3.26L12 2Z" fill="#3897F0"/>
                      <path d="M10 15.5L6.5 12L7.91 10.59L10 12.67L16.09 6.58L17.5 8L10 15.5Z" fill="white"/>
                    </svg>
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                  </div>
                  <div class="ig-header-actions">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
                  </div>
                </div>

                <!-- Instagram Mobile Profile Body -->
                <div class="ig-profile-body">
                  <div class="ig-top-info">
                    <div class="ig-avatar-wrapper">
                      <div class="ig-avatar-ring">
                        <img src="./redes-sociais/Foto Perfil.jpg" alt="Dra. Larissa Machado" class="ig-avatar-img">
                      </div>
                    </div>
                    <div class="ig-stats-container">
                      <div class="ig-stat-box">
                        <span class="ig-stat-num">1.248</span>
                        <span class="ig-stat-label">publicações</span>
                      </div>
                      <div class="ig-stat-box">
                        <span class="ig-stat-num">18,4 mil</span>
                        <span class="ig-stat-label">seguidores</span>
                      </div>
                      <div class="ig-stat-box">
                        <span class="ig-stat-num">412</span>
                        <span class="ig-stat-label">seguindo</span>
                      </div>
                    </div>
                  </div>

                  <!-- Bio Info -->
                  <div class="ig-bio-text">
                    <h4 class="ig-display-name">Dra. Larissa Machado</h4>
                    <p class="ig-bio-tagline">Oftalmologista • Especialista em Plástica Ocular</p>
                    <p class="ig-bio-quote">Rejuvenescer o olhar sem deixar de ser você ✨</p>
                    <p class="ig-bio-location">📍 Atibaia · CRM 197872 / RQE 128236</p>
                    <p class="ig-bio-cta">Comece por aqui ↓</p>
                  </div>

                  <a href="https://share.google/9v6BVUdKtrHndWnxr" target="_blank" rel="noopener noreferrer" class="ig-link-bar">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                    <span>share.google/9v6BVUdKtrHndWnxr</span>
                  </a>

                  <!-- Action Buttons -->
                  <div class="ig-action-btns-row">
                    <button class="ig-btn-primary">Seguir</button>
                    <button class="ig-btn-secondary">Enviar mensagem</button>
                    <button class="ig-btn-secondary icon-btn">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg>
                    </button>
                  </div>

                  <!-- Destaques Funcionais (Highlights Row) com Imagens Reais -->
                  <div class="ig-highlights-section">
                    <div class="ig-highlight-item" data-story="1">
                      <div class="ig-highlight-circle pulsing-ring">
                        <img src="./redes-sociais/Capa Destaque 1.jpg" alt="Destaque Comece Aqui">
                        <div class="ig-play-badge">
                          <svg width="10" height="10" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                        </div>
                      </div>
                      <span class="ig-highlight-title">Comece aqui</span>
                    </div>

                    <div class="ig-highlight-item" data-story="2">
                      <div class="ig-highlight-circle pulsing-ring">
                        <img src="./redes-sociais/Capa Destaque 2.jpg" alt="Destaque Onde Atendo">
                        <div class="ig-play-badge">
                          <svg width="10" height="10" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>
                        </div>
                      </div>
                      <span class="ig-highlight-title">Onde atendo</span>
                    </div>
                  </div>

                  <!-- Mini Feed Tabs Bar -->
                  <div class="ig-feed-tabs-mini">
                    <div class="tab-icon active"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg></div>
                    <div class="tab-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
                    <div class="tab-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
                  </div>

                  <!-- Feed Grid Preview Real -->
                  <div class="ig-mini-grid">
                    <div class="mini-post"><img src="./redes-sociais/1.1.jpg" alt="Post 1"></div>
                    <div class="mini-post"><img src="./redes-sociais/2.1.jpg" alt="Post 2"></div>
                    <div class="mini-post"><img src="./redes-sociais/3.1.jpg" alt="Post 3"></div>
                  </div>

                </div>
              </div>
            </div>

            <!-- Coluna Direita: Explicação Estratégica Compacta -->
            <div class="social-col-right">
              <div class="section-tag">13 · Redes Sociais · Perfil & Destaques</div>
              <h2 class="editorial-eyebrow-large" style="margin-top: 4px;">Arquitetura do Perfil</h2>
              <h3 class="editorial-heading-huge" style="margin-bottom: 16px; font-size: 26px;">Conexão Humana & Autoridade Médica</h3>
              
              <p class="social-rationale-intro" style="font-size: 14px; margin-bottom: 20px;">
                O perfil da Dra. Larissa no Instagram funciona como a <strong>primeira impressão digital</strong> do consultório. A estrutura combina rigidez técnica com sensibilidade acolhedora, orientando o potencial paciente desde a bio até os destaques.
              </p>

              <div class="social-strategy-cards compact-strategy-list">
                <div class="strategy-card-item">
                  <div class="strategy-card-num">01</div>
                  <div class="strategy-card-info">
                    <h4>Foto de Perfil & Postura</h4>
                    <p>Expressão serena, olhar atento e postura acolhedora. Transmite empatia médica sem pose engessada nem estética mercantilizada.</p>
                  </div>
                </div>

                <div class="strategy-card-item">
                  <div class="strategy-card-num">02</div>
                  <div class="strategy-card-info">
                    <h4>Bio Estratégica em 4 Blocos</h4>
                    <p>Especialidade refinada, promessa de marca (<em>"Rejuvenescer o olhar sem deixar de ser você"</em>), CRM/RQE em Atibaia/SP e CTA orientada à conversão.</p>
                  </div>
                </div>

                <div class="strategy-card-item">
                  <div class="strategy-card-num">03</div>
                  <div class="strategy-card-info">
                    <h4>Destaques Fixos Interativos (Stories)</h4>
                    <p>Organização dos pontos de dúvida em 2 pilares primários: <strong>"Comece aqui"</strong> (apresentação & técnica) e <strong>"Onde atendo"</strong> (localização & consultório em Atibaia).</p>
                  </div>
                </div>
              </div>

              <!-- Trigger Buttons -->
              <div class="interactive-trigger-pill-bar" style="margin-top: 20px;">
                <button class="trigger-story-btn" data-story="1">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>
                  <span>Ver Destaque "Comece aqui" (Stories)</span>
                </button>
                <button class="trigger-story-btn secondary" data-story="2">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  <span>Ver Destaque "Onde atendo"</span>
                </button>
              </div>

            </div>

          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 2 - POST 1 (PREPARAÇÃO) ==================== -->
        <section class="slide future" id="slide-social-post-1" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 1 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/1.1.jpg" id="post-img-1" alt="Post 1 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>248 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> A gente aprende a culpar o cansaço por tudo...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 1 [PREPARAÇÃO DA AUDIÊNCIA]</span>
                  <div class="post-viewer-counter">Carrossel · 6 Cards</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="1">
                  <button class="card-nav-btn prev-card-btn">‹</button>
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/1.1.jpg" class="carousel-img active" alt="Card 1">
                    <img src="./redes-sociais/1.2+.jpg" class="carousel-img" alt="Card 2">
                    <img src="./redes-sociais/1.3.jpg" class="carousel-img" alt="Card 3">
                    <img src="./redes-sociais/1.4.jpg" class="carousel-img" alt="Card 4">
                    <img src="./redes-sociais/1.5.jpg" class="carousel-img" alt="Card 5">
                    <img src="./redes-sociais/1.6.jpg" class="carousel-img" alt="Card 6">
                  </div>
                  <button class="card-nav-btn next-card-btn">›</button>
                  <div class="card-dots-row">
                    <div class="card-dot active"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div>
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 1</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>A gente aprende a culpar o cansaço por tudo o que aparece no rosto, mas nem sempre ele é o culpado. Com o tempo, a pálpebra superior perde firmeza e passa a projetar uma sombra discreta sobre o olho e é essa sombra que muda a mensagem que o seu rosto transmite. O olhar comunica cansaço, seriedade, abatimento, mesmo quando por dentro é o oposto...</p>
                    <p>Por isso, aqui no consultório, a ordem é sempre essa: entender primeiro o que te trouxe até aqui e decidir depois a melhor intervenção.</p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 3 - POST 2 (EDUCACIONAL) ==================== -->
        <section class="slide future" id="slide-social-post-2" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 2 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/2.1.jpg" id="post-img-2" alt="Post 2 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>312 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> Toda semana, as mesmas perguntas aparecem...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 2 [EDUCACIONAL]</span>
                  <div class="post-viewer-counter">Carrossel · 6 Cards</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="2">
                  <button class="card-nav-btn prev-card-btn">‹</button>
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/2.1.jpg" class="carousel-img active" alt="Card 1">
                    <img src="./redes-sociais/2.2.jpg" class="carousel-img" alt="Card 2">
                    <img src="./redes-sociais/2.3.jpg" class="carousel-img" alt="Card 3">
                    <img src="./redes-sociais/2.4.jpg" class="carousel-img" alt="Card 4">
                    <img src="./redes-sociais/2.5.jpg" class="carousel-img" alt="Card 5">
                    <img src="./redes-sociais/2.6.jpg" class="carousel-img" alt="Card 6">
                  </div>
                  <button class="card-nav-btn next-card-btn">›</button>
                  <div class="card-dots-row">
                    <div class="card-dot active"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div>
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 2</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>Toda semana, as mesmas perguntas aparecem no consultório. E faz todo sentido: ninguém decide nada sobre os próprios olhos sem antes tirar o medo do caminho.</p>
                    <p>Então, reuni aqui as dúvidas que mais escuto. Respondi cada uma como respondo pessoalmente: com a informação que você precisa para pensar com clareza.</p>
                    <p>Você vai reparar que não tem "resultado garantido" nem "transformação". Tem explicação. Porque a decisão é sua... O meu papel é fazer você entender antes de decidir.</p>
                    <p>Ficou alguma pergunta de fora? Pode me mandar que eu respondo.</p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 4 - POST 3 (EDUCACIONAL) ==================== -->
        <section class="slide future" id="slide-social-post-3" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 3 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/3.1.jpg" id="post-img-3" alt="Post 3 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>189 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> “E a cicatriz?” é quase sempre a primeira...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 3 [EDUCACIONAL]</span>
                  <div class="post-viewer-counter">Carrossel · 3 Cards</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="3">
                  <button class="card-nav-btn prev-card-btn">‹</button>
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/3.1.jpg" class="carousel-img active" alt="Card 1">
                    <img src="./redes-sociais/3.2.jpg" class="carousel-img" alt="Card 2">
                    <img src="./redes-sociais/3.4.jpg" class="carousel-img" alt="Card 3">
                  </div>
                  <button class="card-nav-btn next-card-btn">›</button>
                  <div class="card-dots-row">
                    <div class="card-dot active"></div><div class="card-dot"></div><div class="card-dot"></div>
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 3</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>Essa é uma pergunta clássica que merece um espaço só dela. Passa para o lado e confira os cards acima!</p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 5 - POST 4 (LOCAL DE ATENDIMENTO) ==================== -->
        <section class="slide future" id="slide-social-post-4" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 4 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/4.jpg" id="post-img-4" alt="Post 4 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>142 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> Este é o meu local de atendimento atualmente...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 4 [LOCAL DE ATENDIMENTO]</span>
                  <div class="post-viewer-counter">Single Card</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="4">
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/4.jpg" class="carousel-img active" alt="Card 1">
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 4</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>Este é o meu local de atendimento atualmente.</p>
                    <p>Para agendamento de consultas, clique diretamente no link da bio: <br><strong><a href="https://share.google/9v6BVUdKtrHndWnxr" target="_blank" style="color:#00376B;">share.google/9v6BVUdKtrHndWnxr</a></strong></p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 6 - POST 5 (APRESENTAÇÃO PROFISSIONAL) ==================== -->
        <section class="slide future" id="slide-social-post-5" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 5 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/5.1.jpg" id="post-img-5" alt="Post 5 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>405 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> Seja oficialmente bem-vindo por aqui...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 5 [APRESENTAÇÃO PROFISSIONAL]</span>
                  <div class="post-viewer-counter">Carrossel · 5 Cards</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="5">
                  <button class="card-nav-btn prev-card-btn">‹</button>
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/5.1.jpg" class="carousel-img active" alt="Card 1">
                    <img src="./redes-sociais/5.2.jpg" class="carousel-img" alt="Card 2">
                    <img src="./redes-sociais/5.3.jpg" class="carousel-img" alt="Card 3">
                    <img src="./redes-sociais/5.4.jpg" class="carousel-img" alt="Card 4">
                    <img src="./redes-sociais/5.5.jpg" class="carousel-img" alt="Card 5">
                  </div>
                  <button class="card-nav-btn next-card-btn">›</button>
                  <div class="card-dots-row">
                    <div class="card-dot active"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div><div class="card-dot"></div>
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 5</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>Seja oficialmente bem-vindo por aqui. Meu objetivo nesta página é trazer informação embasada para você que tem interesse na temática.</p>
                    <p>Qualquer dúvida, por favor, meu direct está aberto para conversarmos.</p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ==================== SEÇÃO 13: SLIDE 7 - POST 6 (EDUCACIONAL SOBRE PLÁSTICA OCULAR) ==================== -->
        <section class="slide future" id="slide-social-post-6" data-theme="off-white">
          <div class="slide-content post-slide-layout">
            <!-- Coluna Esquerda: Mockup Post 6 -->
            <div class="post-col-left">
              <div class="iphone-mockup-frame post-mockup-frame">
                <div class="iphone-notch-bar"><span class="iphone-time">9:41</span><div class="iphone-dynamic-island"></div></div>
                <div class="ig-post-view">
                  <div class="ig-post-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" class="ig-post-avatar" alt="Avatar">
                    <span class="ig-post-username">dra.larissamachado</span>
                    <span class="ig-post-more">•••</span>
                  </div>
                  <div class="ig-post-image-container">
                    <img src="./redes-sociais/6.jpg" id="post-img-6" alt="Post 6 Card">
                  </div>
                  <div class="ig-post-actions">
                    <div class="ig-actions-left">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                    </div>
                    <div class="ig-actions-right">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
                    </div>
                  </div>
                  <div class="ig-post-likes"><strong>267 curtidas</strong></div>
                  <div class="ig-post-caption-preview"><strong>dra.larissamachado</strong> Muita gente associa cirurgia de pálpebra a rejuvenescimento...</div>
                </div>
              </div>
            </div>

            <!-- Coluna Direita: Cards Carousel & Legenda -->
            <div class="post-col-right">
              <div class="post-viewer-container">
                <div class="post-viewer-header">
                  <span class="post-viewer-cat-badge">CONTEÚDO 6 [EDUCACIONAL SOBRE PLÁSTICA OCULAR]</span>
                  <div class="post-viewer-counter">Single Card</div>
                </div>

                <div class="post-cards-carousel-box" data-post-carousel="6">
                  <div class="card-display-viewport">
                    <img src="./redes-sociais/6.jpg" class="carousel-img active" alt="Card 1">
                  </div>
                </div>

                <div class="post-copy-box">
                  <div class="copy-box-header">
                    <img src="./redes-sociais/Foto Perfil.jpg" alt="Avatar" class="copy-avatar">
                    <div class="copy-user-meta">
                      <span class="copy-handle">dra.larissamachado</span>
                      <span class="copy-sub">Legenda Oficial do Post 6</span>
                    </div>
                  </div>
                  <div class="copy-scroll-body">
                    <p>Muita gente associa cirurgia de pálpebra a rejuvenescimento, mas a plástica ocular também trata condições que afetam a saúde e o funcionamento dos seus olhos.</p>
                    <p><strong>Ptose:</strong> é a queda da pálpebra superior. Com o tempo, ou por questões congênitas e neurológicas, o músculo que sustenta a pálpebra enfraquece, e ela passa a cobrir parte do olho. O incômodo raramente é só estético: a ptose reduz o campo de visão, obriga você a levantar a sobrancelha o dia inteiro para enxergar e cansa. A cirurgia reposiciona a pálpebra na altura certa, devolvendo abertura ao olhar e conforto à visão.</p>
                    <p><strong>Tumores palpebrais:</strong> nem toda "verruguinha" ou nódulo na pálpebra é inofensivo. Existem lesões benignas, mas também tumores que precisam de atenção, inclusive alguns tipos de câncer de pele, que são comuns nessa região por causa da exposição solar. A plástica ocular cuida da remoção da lesão e da reconstrução da pálpebra, preservando tanto a função (proteção do olho) quanto a estética. Avaliar cedo faz toda a diferença.</p>
                    <p><strong>Obstrução das vias lacrimais:</strong> quando o canal que drena a lágrima entope, ela não tem para onde ir. O resultado é o olho lacrimejando o tempo todo, secreção e infecções que voltam sempre. Não é frescura nem "olho sensível": é um problema de drenagem com solução cirúrgica, que reconstrói o caminho da lágrima e resolve o incômodo de vez.</p>
                    <p>Se você se reconheceu em algum desses sinais, o primeiro passo é entender o que está acontecendo.</p>
                    <p><strong>Dra. Larissa · Oftalmologia · Plástica Ocular · CRM 197872-SP</strong></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        '''

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

if idx_start != -1 and idx_end != -1:
    html = html[:idx_start] + new_content + html[idx_end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated slides successfully!')
else:
    print('Markers not found!')
