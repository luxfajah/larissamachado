import os
import shutil
import subprocess
import fitz

# Define target paths
CLIENT_DIR = "/Users/luxfajah/Documents/Duas mâos/Alice "
JUNHO_DIR = os.path.join(CLIENT_DIR, "Junho")
FONTES_DEST_DIR = os.path.join(CLIENT_DIR, "Fontes")
PDF_OUTPUT_PATH = os.path.join(CLIENT_DIR, "Briefing de Edição - Alice.pdf")
HTML_OUTPUT_PATH = os.path.join(CLIENT_DIR, "Briefing - Alice.html")

# Ensure target directories exist
os.makedirs(FONTES_DEST_DIR, exist_ok=True)

# Copy fonts to client directory for local download accessibility
fonts_to_copy = [
    ("AlbertSans-Regular.ttf", "AlbertSans-Regular.ttf"),
    ("AlbertSans-Bold.ttf", "AlbertSans-Bold.ttf"),
    ("AlbertSans-Italic.ttf", "AlbertSans-Italic.ttf"),
    ("AlbertSans-BoldItalic.ttf", "AlbertSans-BoldItalic.ttf"),
    ("Cosmodrome-Monoline.otf", "Cosmodrome Monoline.otf")
]

for src, dest_name in fonts_to_copy:
    if os.path.exists(src):
        shutil.copy(src, os.path.join(FONTES_DEST_DIR, dest_name))

print("Fontes copiadas para a pasta do cliente.")

def generate_single_html():
    # Helper to generate nav-list HTML with active class
    def get_nav_list_html(active_idx):
        items = [
            ("cover", "00", "book-open", "Capa & Autoria"),
            ("intro", "01", "sparkles", "Conceito & Posicionamento"),
            ("edit", "02", "sliders", "Diretrizes de Edição"),
            ("subs", "03", "file-text", "Legendas & Grafismos"),
            ("visual", "04", "palette", "Cores & Tipografia"),
            ("quality", "05", "award", "Checklist de Qualidade"),
            ("mood", "06", "eye", "Moodboard de Referências"),
            ("downloads", "07", "download", "Arquivos & Downloads")
        ]
        html = '<ul class="nav-list">'
        for idx, (tab_id, num, icon, label) in enumerate(items):
            active_class = "active" if idx == active_idx else ""
            html += f'<li class="nav-item {active_class}" onclick="switchTab(\'{tab_id}\')"><span class="nav-num">{num}</span><i data-lucide="{icon}"></i><span>{label}</span></li>'
        html += '</ul>'
        return html

    # Shared content sections HTML
    cover_section = """
        <div class="cover-layout">
          <div class="cover-header">
            <div class="cover-accent-line"></div>
            <h1 class="cover-title">MANUAL DE<br>DIREÇÃO CRIATIVA</h1>
            <p class="cover-subtitle">Guia de Alinhamento Criativo e Edição Audiovisual</p>
          </div>

          <div class="callout-box" style="margin-top: 20px;">
            <div class="callout-title">DIRETRIZ DE ARTE</div>
            <p class="callout-text">
              Este manual serve como guia conceitual e técnico para garantir que todos os produtos 
              audiovisuais da Alice Stoff reflitam uma linguagem sofisticada, acolhedora e minimalista.
            </p>
          </div>

          <div class="metadata-grid">
            <div class="metadata-card"><span class="metadata-label">CLIENTE</span><span class="metadata-value">Alice Stoff</span></div>
            <div class="metadata-card"><span class="metadata-label">DESIGN</span><span class="metadata-value">Lux Fajah</span></div>
            <div class="metadata-card"><span class="metadata-label">ESTRATÉGIA</span><span class="metadata-value">Thacy Nunes</span></div>
            <div class="metadata-card"><span class="metadata-label">PROJETO</span><span class="metadata-value">Welynadia</span></div>
          </div>
        </div>
    """

    intro_section = """
          <h2 class="page-title">Apresentação & Conceito</h2>
          <p class="page-subtitle">O posicionamento da marca pessoal e os valores estéticos fundamentais do projeto.</p>

          <div class="callout-box">
            <div class="callout-title">PROPÓSITO</div>
            <p class="callout-text">
              A edição deve ser entendida como uma extensão da identidade visual da marca. O propósito 
              é transmitir proximidade, elegância e autoridade natural, sem recorrer a excessos gráficos.
            </p>
          </div>

          <h3 class="section-title">Posicionamento de Comunicação</h3>
          <p style="font-size: 13px; line-height: 1.6; margin-bottom: 16px; color: var(--color-text-primary);">
            Alice Stoff fala para um público sofisticado e conectado. A comunicação audiovisual deve mesclar 
            sensibilidade criativa e credibilidade corporativa. A estética segue a linha editorial (como revistas de design) 
            e scrapbook orgânico contemporâneo.
          </p>

          <h3 class="section-title">Diretrizes de Personalidade</h3>
          <div class="grid-2col">
            <div class="simple-card accent-top-blue">
              <span class="card-header-label blue">DEVE PARECER</span>
              <ul class="list-items">
                <li class="list-item"><span class="list-bullet">•</span><span>Humana e acolhedora</span></li>
                <li class="list-item"><span class="list-bullet">•</span><span>Orgânica e editorial</span></li>
                <li class="list-item"><span class="list-bullet">•</span><span>Minimamente sofisticada</span></li>
                <li class="list-item"><span class="list-bullet">•</span><span>Criativa e autoral</span></li>
              </ul>
            </div>
            <div class="simple-card accent-top-orange">
              <span class="card-header-label orange">NÃO DEVE PARECER</span>
              <ul class="list-items">
                <li class="list-item"><span class="list-cross">×</span><span>Fria ou puramente corporativa</span></li>
                <li class="list-item"><span class="list-cross">×</span><span>Genérica ou baseada em presets prontos</span></li>
                <li class="list-item"><span class="list-cross">×</span><span>Carregada de efeitos visuais chamativos</span></li>
                <li class="list-item"><span class="list-cross">×</span><span>Infantil ou desnecessariamente colorida</span></li>
              </ul>
            </div>
          </div>
    """

    edit_section = """
          <h2 class="page-title">Diretrizes de Edição</h2>
          <p class="page-subtitle">Ritmo, cortes e controle de animação para garantir autoridade e clareza de fala.</p>

          <div class="callout-box">
            <div class="callout-title">CONSELHO DE DIREÇÃO</div>
            <p class="callout-text">
              O ritmo da edição deve ser fluído e natural. Respeite as pausas da fala da Alice para criar 
              momentos de respiro, evitando transições abruptas ou excesso de jump cuts artificiais.
            </p>
          </div>

          <h3 class="section-title">Edição & Ritmo</h3>
          <div class="bullet-list">
            <div class="bullet-item">
              <span class="bullet-marker"></span>
              <span><strong>Cortes Limpos:</strong> Use transições invisíveis. Evite efeitos de zoom contínuo ou transições 3D.</span>
            </div>
            <div class="bullet-item">
              <span class="bullet-marker"></span>
              <span><strong>Atenção Inicial:</strong> Prenda a atenção nos primeiros 3 segundos usando o título principal e a voz natural da Alice, não com trilhas sonoras invasivas.</span>
            </div>
          </div>

          <h3 class="section-title">Tabela de Boas Práticas - Motion Design</h3>
          <div class="simple-card accent-top-blue" style="padding: 15px;">
            <div class="grid-2col" style="gap: 30px; margin-bottom: 0;">
              <div>
                <span class="card-header-label blue">RECOMENDADO (DISCRETO)</span>
                <ul class="list-items" style="font-size: 11px;">
                  <li class="list-item"><span class="list-bullet">•</span><span>Transição em fade ou scale sutil (0.98 para 1.0)</span></li>
                  <li class="list-item"><span class="list-bullet">•</span><span>Pequenos deslocamentos lineares de textos</span></li>
                  <li class="list-item"><span class="list-bullet">•</span><span>Aparecimento suave com controle de opacidade</span></li>
                </ul>
              </div>
              <div>
                <span class="card-header-label orange">EVITAR (EXAGERADO)</span>
                <ul class="list-items" style="font-size: 11px;">
                  <li class="list-item"><span class="list-cross">×</span><span>Presets de animação de canais de entretenimento</span></li>
                  <li class="list-item"><span class="list-cross">×</span><span>Bounce exagerado ou efeitos de tremor/glitch</span></li>
                  <li class="list-item"><span class="list-cross">×</span><span>Efeitos sonoros excessivos (woosh, pop constante)</span></li>
                </ul>
              </div>
            </div>
          </div>
    """

    subs_section = """
          <h2 class="page-title">Legendas & Grafismos</h2>
          <p class="page-subtitle">Aplicação de letterings manuscritos e grifos para direcionamento de foco.</p>

          <div class="callout-box">
            <div class="callout-title">ATENÇÃO NARRATIVA</div>
            <p class="callout-text">
              Nunca utilize intervenções gráficas apenas para preencher tela. Cada rabisco, seta ou palavra 
              manuscrita deve surgir com o único propósito de ressaltar a fala activa da Alice.
            </p>
          </div>

          <div class="grid-2col">
            <div>
              <h3 class="section-title">Diretrizes de Legendas</h3>
              <div class="bullet-list">
                <div class="bullet-item"><span class="bullet-marker"></span><span>Divida as frases em blocos de no máximo 2 a 3 palavras.</span></div>
                <div class="bullet-item"><span class="bullet-marker"></span><span>Destaque palavras-chave específicas em <strong>Laranja</strong> para criar hierarquia visual.</span></div>
                <div class="bullet-item"><span class="bullet-marker"></span><span>Utilize a cor <strong>Off White</strong> no corpo da legenda, evitando o branco puro para reduzir fadiga visual.</span></div>
              </div>
            </div>
            <div>
              <h3 class="section-title">Grafismos Manuais</h3>
              <div class="bullet-list">
                <div class="bullet-item"><span class="bullet-marker"></span><span>Setas e círculos devem ter aparência de desenho feito à mão com pincel fino.</span></div>
                <div class="bullet-item"><span class="bullet-marker"></span><span>Sublinhados e grifos acompanham o surgimento das palavras-chave destacadas.</span></div>
                <div class="bullet-item"><span class="bullet-marker"></span><span>Lettering de impacto deve usar a fonte cursiva <strong>Cosmodrome</strong>.</span></div>
              </div>
            </div>
          </div>
    """

    visual_section = """
          <h2 class="page-title">Cores & Tipografia</h2>
          <p class="page-subtitle">As diretrizes oficiais da paleta de cores e tipografia da Alice Stoff.</p>

          <h3 class="section-title">Tipografia da Identidade</h3>
          <div class="grid-2col">
            <div class="simple-card">
              <span class="card-header-label orange" style="color:var(--color-accent-orange)">FONTE PRINCIPAL (LETTING/DESTAQUE)</span>
              <span class="font-display-name" style="font-family: 'Cosmodrome', sans-serif; color:var(--color-accent-blue)">Cosmodrome Monoline</span>
              <p class="font-desc">Usada em letterings orgânicos de destaque, títulos manuscritos curtos e pequenas intervenções estéticas.</p>
            </div>
            <div class="simple-card">
              <span class="card-header-label blue">FONTE SECUNDÁRIA (LEGENDAS/CORPO)</span>
              <span class="font-display-name" style="font-family: 'Albert Sans', sans-serif; font-weight:700;">Albert Sans</span>
              <p class="font-desc">Usada em legendas, corpo de textos informativos, subtítulos, tabelas e informações de apoio visual.</p>
            </div>
          </div>

          <div class="interactive-test">
            <div class="test-label">SIMULADOR DE TEXTO</div>
            <input type="text" class="test-textarea sim-input-cls" value="O essencial é invisível aos olhos." oninput="updateSimVal(this.value)">
            <div class="grid-2col" style="margin:0;">
              <div>
                <div class="test-label">PREVIEW - COSMODROME</div>
                <div class="preview-box prev-cosmo-cls" style="font-family:'Cosmodrome', sans-serif; font-size:18px; color:var(--color-accent-blue)">O essencial é invisível aos olhos.</div>
              </div>
              <div>
                <div class="test-label">PREVIEW - ALBERT SANS</div>
                <div class="preview-box prev-albert-cls" style="font-family:'Albert Sans', sans-serif; font-weight:700; font-size:15px">O essencial é invisível aos olhos.</div>
              </div>
            </div>
          </div>

          <h3 class="section-title">Paleta de Cores Oficial</h3>
          <div class="swatches-row">
            <div class="swatch-card" onclick="copyColor('#2E2A6E')">
              <div class="swatch-color" style="background-color: #2E2A6E"></div>
              <div class="swatch-info"><span class="swatch-name">Azul</span><span class="swatch-hex">#2E2A6E</span></div>
            </div>
            <div class="swatch-card" onclick="copyColor('#E8763A')">
              <div class="swatch-color" style="background-color: #E8763A"></div>
              <div class="swatch-info"><span class="swatch-name">Laranja</span><span class="swatch-hex">#E8763A</span></div>
            </div>
            <div class="swatch-card" onclick="copyColor('#E8C4B8')">
              <div class="swatch-color" style="background-color: #E8C4B8"></div>
              <div class="swatch-info"><span class="swatch-name">Creme</span><span class="swatch-hex">#E8C4B8</span></div>
            </div>
            <div class="swatch-card" onclick="copyColor('#F4EDE4')">
              <div class="swatch-color" style="background-color: #F4EDE4"></div>
              <div class="swatch-info"><span class="swatch-name">Off White</span><span class="swatch-hex">#F4EDE4</span></div>
            </div>
            <div class="swatch-card" onclick="copyColor('#9B9EA6')">
              <div class="swatch-color" style="background-color: #9B9EA6"></div>
              <div class="swatch-info"><span class="swatch-name">Cinza</span><span class="swatch-hex">#9B9EA6</span></div>
            </div>
          </div>
    """

    quality_section = """
          <h2 class="page-title">Checklist de Qualidade</h2>
          <p class="page-subtitle">Lista interativa de verificação visual antes do envio e postagem oficial.</p>

          <div class="grid-3col">
            <div class="simple-card" style="border-top:3px solid var(--color-accent-blue)">
              <span class="card-header-label" style="color:var(--color-accent-blue)">IDENTIDADE VISUAL</span>
              <div class="list-items" style="gap: 10px;">
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Tipografia correta (Albert Sans e Cosmodrome)</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Paleta de cores oficial aplicada sem ruído</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Lettering manuscrito com boa escala</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Capa integrada e consistente com o feed</span></div>
              </div>
            </div>
            <div class="simple-card" style="border-top:3px solid var(--color-accent-orange)">
              <span class="card-header-label" style="color:var(--color-accent-orange)">RITMO & CORTE</span>
              <div class="list-items" style="gap: 10px;">
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Pausas da fala respeitadas</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Legendas 100% legíveis com Off White</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Grafismos com propósito narrativo claro</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Sem excesso de filtros e efeitos de zoom</span></div>
              </div>
            </div>
            <div class="simple-card" style="border-top:3px solid var(--color-text-muted)">
              <span class="card-header-label" style="color:var(--color-text-muted)">BRANDING GERAL</span>
              <div class="list-items" style="gap: 10px;">
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Vídeo reflete autoridade da Alice Stoff</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Branding discreto e de tom elegante</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Visual editorial consolidado e moderno</span></div>
                <div class="check-item" onclick="toggleCheck(this)"><div class="checkbox-custom"></div><span class="check-text">Consistência estética e de paleta de cores</span></div>
              </div>
            </div>
          </div>

          <div style="display: flex; justify-content: flex-end; margin-top: 10px;">
            <button class="btn-header" onclick="resetChecklist()" style="display: flex; align-items: center; gap: 6px;">
              <i data-lucide="refresh-cw"></i>
              <span>Limpar Progresso</span>
            </button>
          </div>
    """

    mood_section = """
          <h2 class="page-title">Moodboard de Referências</h2>
          <p class="page-subtitle">Painel integrado com todas as imagens em proporção real 4:5 do 1º post. Clique para zoom.</p>

          <div class="moodboard-backing">
            <!-- 8 portrait items of Post 1 exactly (Aspect ratio preserved at 4:5) -->
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 1.jpg')">
              <img src="Junho/Post 1 - 1.jpg" alt="Post 1 - 1" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 2.jpg')">
              <img src="Junho/Post 1 - 2.jpg" alt="Post 1 - 2" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 3.jpg')">
              <img src="Junho/Post 1 - 3.jpg" alt="Post 1 - 3" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 4.jpg')">
              <img src="Junho/Post 1 - 4.jpg" alt="Post 1 - 4" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 5.jpg')">
              <img src="Junho/Post 1 - 5.jpg" alt="Post 1 - 5" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 6.jpg')">
              <img src="Junho/Post 1 - 6.jpg" alt="Post 1 - 6" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 7.jpg')">
              <img src="Junho/Post 1 - 7.jpg" alt="Post 1 - 7" class="moodboard-image">
            </div>
            <div class="moodboard-frame" onclick="zoomImage('Junho/Post 1 - 8.jpg')">
              <img src="Junho/Post 1 - 8.jpg" alt="Post 1 - 8" class="moodboard-image">
            </div>
          </div>
    """

    downloads_section = """
          <h2 class="page-title">Download de Arquivos</h2>
          <p class="page-subtitle">Arquivos tipográficos originais para instalação no Premiere / After Effects. (Clique no ícone de clipe no PDF para abrir)</p>

          <div class="callout-box">
            <div class="callout-title">AVISO DE COMPATIBILIDADE</div>
            <p class="callout-text">
              Baixe e instale as fontes no seu sistema operacional antes de abrir os arquivos de projeto 
              no Adobe Premiere Pro, After Effects ou CapCut Desktop para garantir o layout correto.
            </p>
          </div>

          <div class="downloads-grid">
            <a class="download-btn-card" href="Fontes/Cosmodrome Monoline.otf" download>
              <div class="download-info">
                <span class="download-title">Cosmodrome Monoline</span>
                <span class="download-desc">Fonte primária de destaques (.OTF)</span>
              </div>
              <div class="download-btn-icon"><i data-lucide="paperclip"></i></div>
            </a>
            <a class="download-btn-card" href="Fontes/AlbertSans-Regular.ttf" download>
              <div class="download-info">
                <span class="download-title">Albert Sans Regular</span>
                <span class="download-desc">Fonte secundária de legendas (.TTF)</span>
              </div>
              <div class="download-btn-icon"><i data-lucide="paperclip"></i></div>
            </a>
            <a class="download-btn-card" href="Fontes/AlbertSans-Bold.ttf" download>
              <div class="download-info">
                <span class="download-title">Albert Sans Bold</span>
                <span class="download-desc">Fonte secundária negrito (.TTF)</span>
              </div>
              <div class="download-btn-icon"><i data-lucide="paperclip"></i></div>
            </a>
            <a class="download-btn-card" href="Fontes/AlbertSans-Italic.ttf" download>
              <div class="download-info">
                <span class="download-title">Albert Sans Italic</span>
                <span class="download-desc">Fonte secundária itálico (.TTF)</span>
              </div>
              <div class="download-btn-icon"><i data-lucide="paperclip"></i></div>
            </a>
          </div>
    """

    # Generate print pages containers (clones of the app container for each tab, to print perfectly)
    print_pages_html = ""
    sections_list = [
        ("cover", cover_section),
        ("intro", intro_section),
        ("edit", edit_section),
        ("subs", subs_section),
        ("visual", visual_section),
        ("quality", quality_section),
        ("mood", mood_section),
        ("downloads", downloads_section)
    ]

    for idx, (tab_id, content) in enumerate(sections_list):
        print_pages_html += f"""
      <div class="print-app-container">
        <!-- Sidebar for Slide {idx} -->
        <aside class="sidebar">
          <div class="logo-section">
            <span class="logo-label">DUAS MÃOS</span>
            <span class="logo-sub">DIREÇÃO DE ARTE / CORPORATIVO</span>
          </div>
          {get_nav_list_html(idx)}
          <footer class="sidebar-footer">
            <div>Manual de Direção Criativa</div>
            <div>Versão 1.0 . Julho de 2026</div>
            <div style="margin-top: 8px; opacity: 0.6;">© Duas Mãos</div>
          </footer>
        </aside>

        <!-- Content Area for Slide {idx} -->
        <main class="content-area">
          <div class="header-top">
            <span class="header-meta">PROJETO ALICE STOFF . BRIEFING DE EDIÇÃO AUDIOVISUAL</span>
            <div class="header-actions">
              <button class="btn-header">
                <i data-lucide="download"></i>
                <span>Arquivos de Fontes</span>
              </button>
              <button class="btn-header primary">
                <i data-lucide="check-circle"></i>
                <span>Checklist</span>
              </button>
            </div>
          </div>

          <div style="flex:1;">
            {content}
          </div>

          <footer class="content-footer-note">
            <div>DUAS MÃOS DIREÇÃO DE ARTE</div>
            <div style="font-size:9px; color:var(--color-text-muted); marginTop:4px;">
              Este documento e seus ativos embutidos são propriedades corporativas exclusivas da Alice Stoff.
            </div>
          </footer>
        </main>
      </div>
        """

    # Combine everything (curly brackets in Javascript script must be doubled as {{ and }} to avoid f-string syntax errors)
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Manual de Direção Criativa - Alice Stoff</title>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Albert+Sans:ital,wght@0,300;0,400;0,700;1,400&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet" />
  
  <style>
    @font-face {{
      font-family: 'Cosmodrome';
      src: url('Fontes/Cosmodrome Monoline.otf') format('opentype');
    }}

    :root {{
      --color-bg-sidebar: #f6f4f0;
      --color-bg-content: #ffffff;
      --color-text-primary: #1a1a1a;
      --color-text-secondary: #5e5e5e;
      --color-text-muted: #9b9ea6;
      --color-accent-orange: #e8763a;
      --color-accent-blue: #2e2a6e;
      --color-border: #e5e5e5;
      --color-card-bg: #faf9f6;
      --color-shadow: rgba(0, 0, 0, 0.05);

      --font-corporate: 'Poppins', sans-serif;
      --font-content: 'Albert Sans', sans-serif;
      --font-client: 'Cosmodrome', cursive;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    body {{
      font-family: var(--font-content);
      color: var(--color-text-primary);
      background-color: #ededed;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }}

    /* Widescreen 1920x1080 Aspect Ratio Container */
    .app-container {{
      display: grid;
      grid-template-columns: 280px 1fr;
      width: 100%;
      max-width: 1120px;
      height: 630px; /* Exact 16:9 ratio with 1120px width (1120 * 9 / 16 = 630px) */
      background-color: var(--color-bg-content);
      border-radius: 12px;
      box-shadow: 0 20px 40px var(--color-shadow), 0 0 0 1px rgba(0,0,0,0.05);
      overflow: hidden;
      position: relative;
    }}

    .sidebar {{
      background-color: var(--color-bg-sidebar);
      border-right: 1px solid var(--color-border);
      padding: 30px 25px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }}

    .logo-section {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .logo-label {{
      font-family: var(--font-corporate);
      font-weight: 700;
      font-size: 15px;
      letter-spacing: 1px;
      color: var(--color-text-primary);
    }}

    .logo-sub {{
      font-family: var(--font-corporate);
      font-weight: 400;
      font-size: 9.5px;
      color: var(--color-text-muted);
      letter-spacing: 0.5px;
    }}

    .nav-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 30px;
      list-style: none;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-family: var(--font-corporate);
      font-size: 12.5px;
      font-weight: 500;
      color: var(--color-text-secondary);
      transition: all 0.2s ease;
    }}

    .nav-item:hover {{
      background-color: rgba(0, 0, 0, 0.03);
      color: var(--color-text-primary);
    }}

    .nav-item.active {{
      background-color: #ffffff;
      color: var(--color-accent-orange);
      box-shadow: 0 4px 10px var(--color-shadow);
      border-left: 3px solid var(--color-accent-orange);
    }}

    .nav-num {{
      font-size: 10px;
      font-weight: 700;
      opacity: 0.7;
    }}

    .nav-item svg {{
      width: 13px;
      height: 13px;
    }}

    .sidebar-footer {{
      font-family: var(--font-corporate);
      font-size: 9.5px;
      color: var(--color-text-muted);
      line-height: 1.5;
    }}

    .content-area {{
      padding: 30px 45px;
      overflow-y: auto;
      height: 100%;
      display: flex;
      flex-direction: column;
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}

    .header-meta {{
      font-family: var(--font-corporate);
      font-size: 9.5px;
      font-weight: 600;
      color: var(--color-text-muted);
      letter-spacing: 1px;
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
    }}

    .btn-header {{
      font-family: var(--font-corporate);
      font-size: 9.5px;
      font-weight: 700;
      padding: 6px 12px;
      border: 1px solid var(--color-border);
      border-radius: 4px;
      background-color: white;
      cursor: pointer;
      color: var(--color-text-primary);
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .btn-header svg {{
      width: 11px;
      height: 11px;
    }}

    .btn-header:hover {{
      background-color: #fafafa;
    }}

    .btn-header.primary {{
      background-color: var(--color-accent-orange);
      color: white;
      border-color: var(--color-accent-orange);
    }}

    .btn-header.primary:hover {{
      background-color: #d1622b;
    }}

    .page-title {{
      font-family: var(--font-corporate);
      font-weight: 700;
      font-size: 22px;
      color: var(--color-text-primary);
      margin-bottom: 4px;
    }}

    .page-subtitle {{
      font-size: 12.5px;
      color: var(--color-text-secondary);
      margin-bottom: 16px;
      line-height: 1.6;
    }}

    .callout-box {{
      background-color: var(--color-card-bg);
      border-left: 3px solid var(--color-accent-orange);
      padding: 12px 16px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 16px;
    }}

    .callout-title {{
      font-family: var(--font-corporate);
      font-weight: 700;
      font-size: 10px;
      color: var(--color-accent-orange);
      letter-spacing: 0.5px;
      margin-bottom: 2px;
    }}

    .callout-text {{
      font-size: 11.5px;
      color: var(--color-text-primary);
      line-height: 1.6;
    }}

    .cover-layout {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }}

    .cover-header {{
      margin-top: 15px;
    }}

    .cover-title {{
      font-family: var(--font-corporate);
      font-size: 34px;
      font-weight: 700;
      line-height: 1.1;
      color: var(--color-text-primary);
      margin-bottom: 10px;
    }}

    .cover-accent-line {{
      width: 45px;
      height: 4px;
      background-color: var(--color-accent-orange);
      margin-bottom: 16px;
    }}

    .cover-subtitle {{
      font-size: 14px;
      color: var(--color-text-secondary);
      line-height: 1.5;
    }}

    .metadata-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      margin-top: auto;
      padding-top: 20px;
      border-top: 1px solid var(--color-border);
    }}

    .metadata-card {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .metadata-label {{
      font-family: var(--font-corporate);
      font-size: 8.5px;
      font-weight: 700;
      color: var(--color-text-muted);
      letter-spacing: 0.5px;
    }}

    .metadata-value {{
      font-family: var(--font-corporate);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--color-text-primary);
    }}

    .section-title {{
      font-family: var(--font-corporate);
      font-size: 13.5px;
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: 8px;
      border-bottom: 2px solid var(--color-border);
      padding-bottom: 4px;
    }}

    .grid-2col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }}

    .grid-3col {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 16px;
    }}

    .simple-card {{
      border: 1px solid var(--color-border);
      border-radius: 8px;
      background-color: white;
      padding: 12px 16px;
      display: flex;
      flex-direction: column;
    }}

    .simple-card.accent-top-blue {{
      border-top: 3px solid var(--color-accent-blue);
    }}

    .simple-card.accent-top-orange {{
      border-top: 3px solid var(--color-accent-orange);
    }}

    .card-header-label {{
      font-family: var(--font-corporate);
      font-size: 9.5px;
      font-weight: 700;
      margin-bottom: 6px;
    }}

    .card-header-label.blue {{
      color: var(--color-accent-blue);
    }}

    .card-header-label.orange {{
      color: var(--color-accent-orange);
    }}

    .list-items {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      list-style: none;
    }}

    .list-item {{
      font-size: 11px;
      line-height: 1.5;
      color: var(--color-text-primary);
      display: flex;
      gap: 8px;
      align-items: flex-start;
    }}

    .list-bullet {{
      color: var(--color-accent-orange);
      font-weight: bold;
    }}

    .list-cross {{
      color: var(--color-accent-orange);
    }}

    .bullet-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 12px;
    }}

    .bullet-item {{
      display: flex;
      gap: 8px;
      align-items: flex-start;
      font-size: 11.5px;
      line-height: 1.5;
    }}

    .bullet-marker {{
      width: 4px;
      height: 4px;
      background-color: var(--color-accent-orange);
      border-radius: 1px;
      margin-top: 6px;
      flex-shrink: 0;
    }}

    .swatches-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
    }}

    .swatch-card {{
      flex: 1;
      border: 1px solid var(--color-border);
      border-radius: 6px;
      background-color: white;
      padding: 5px;
      display: flex;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .swatch-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 10px var(--color-shadow);
    }}

    .swatch-color {{
      height: 44px;
      border-radius: 4px;
      width: 100%;
    }}

    .swatch-info {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      padding-bottom: 2px;
    }}

    .swatch-name {{
      font-family: var(--font-corporate);
      font-weight: 700;
      font-size: 9.5px;
      color: var(--color-text-primary);
    }}

    .swatch-hex {{
      font-size: 8px;
      color: var(--color-text-muted);
    }}

    .font-display-name {{
      font-size: 20px;
      margin-bottom: 8px;
      color: var(--color-text-primary);
    }}

    .font-desc {{
      font-size: 11px;
      color: var(--color-text-secondary);
      line-height: 1.5;
    }}

    .interactive-test {{
      border: 1px solid var(--color-border);
      border-radius: 8px;
      padding: 10px;
      margin-bottom: 12px;
      background-color: #fbfbfb;
    }}

    .test-label {{
      font-family: var(--font-corporate);
      font-size: 8.5px;
      font-weight: 700;
      color: var(--color-text-muted);
      margin-bottom: 6px;
    }}

    .test-textarea {{
      width: 100%;
      padding: 6px;
      border: 1px solid var(--color-border);
      border-radius: 6px;
      font-family: var(--font-content);
      font-size: 11.5px;
      margin-bottom: 8px;
      resize: none;
    }}

    .preview-box {{
      background-color: white;
      border: 1px solid var(--color-border);
      border-radius: 6px;
      padding: 12px;
      min-height: 50px;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      box-shadow: inset 0 2px 5px rgba(0,0,0,0.02);
    }}

    .check-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 4px 0;
      cursor: pointer;
      user-select: none;
    }}

    .checkbox-custom {{
      width: 13px;
      height: 13px;
      border: 1px solid #c8c8c8;
      border-radius: 3px;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-shrink: 0;
      transition: all 0.2s ease;
    }}

    .check-item:hover .checkbox-custom {{
      border-color: var(--color-accent-orange);
    }}

    .check-item.checked .checkbox-custom {{
      background-color: var(--color-accent-orange);
      border-color: var(--color-accent-orange);
    }}

    .check-item.checked .checkbox-custom::after {{
      content: "✓";
      color: white;
      font-size: 8px;
      font-weight: bold;
    }}

    .check-text {{
      font-size: 11px;
      color: var(--color-text-primary);
      transition: all 0.2s ease;
    }}

    .check-item.checked .check-text {{
      color: var(--color-text-muted);
      text-decoration: line-through;
    }}

    /* 2x4 Grid layout showing 4:5 portrait cards completely without crop */
    .moodboard-backing {{
      position: relative;
      background-color: #fcfbfa;
      border: 1px solid var(--color-border);
      border-radius: 8px;
      padding: 10px;
      display: grid;
      grid-template-columns: repeat(4, 120px);
      grid-template-rows: repeat(2, 150px);
      gap: 12px;
      justify-content: center;
      align-content: center;
      min-height: 330px;
      overflow: hidden;
    }}

    .moodboard-frame {{
      background-color: white;
      border: 1px solid var(--color-border);
      border-radius: 6px;
      padding: 3px;
      box-shadow: 0 2px 8px var(--color-shadow);
      cursor: pointer;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 120px;
      height: 150px;
      transition: transform 0.2s ease;
    }}

    .moodboard-frame:hover {{
      transform: scale(1.05);
      z-index: 5;
    }}

    .moodboard-image {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 3px;
    }}

    .zoom-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.7);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 100;
      backdrop-filter: blur(5px);
      cursor: pointer;
    }}

    .zoom-content {{
      background-color: white;
      padding: 15px;
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      max-width: 460px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    }}

    .zoom-img {{
      width: 100%;
      max-height: 420px;
      object-fit: contain;
      border-radius: 6px;
    }}

    .downloads-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 16px;
    }}

    .download-btn-card {{
      border: 1px solid var(--color-border);
      border-radius: 8px;
      padding: 12px;
      background-color: white;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .download-btn-card:hover {{
      border-color: var(--color-accent-orange);
      box-shadow: 0 4px 15px var(--color-shadow);
    }}

    .download-info {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      text-align: left;
    }}

    .download-title {{
      font-family: var(--font-corporate);
      font-weight: 700;
      font-size: 12px;
      color: var(--color-text-primary);
    }}

    .download-desc {{
      font-size: 10px;
      color: var(--color-text-muted);
    }}

    .download-btn-icon {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background-color: var(--color-bg-sidebar);
      color: var(--color-accent-orange);
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .download-btn-card:hover .download-btn-icon {{
      background-color: var(--color-accent-orange);
      color: white;
    }}

    .content-footer-note {{
      margin-top: auto;
      border-top: 1px solid var(--color-border);
      padding-top: 12px;
      font-family: var(--font-corporate);
      font-size: 9.5px;
      color: var(--color-text-muted);
      line-height: 1.5;
    }}

    .page-section {{
      display: none;
      height: 100%;
      flex-direction: column;
    }}

    .page-section.active {{
      display: flex;
    }}

    /* Print-specific layout containers (hidden on screen) */
    .print-pages-container {{
      display: none;
    }}

    /* PRINT STYLES - Headless Chrome uses this to render exact sequential horizontal PDF pages */
    @media print {{
      @page {{
        size: 297mm 167mm; /* 16:9 Landscape A4 ratio */
        margin: 0;
      }}

      body {{
        background-color: white !important;
        padding: 0 !important;
        min-height: auto;
      }}

      .app-container {{
        display: none !important; /* Hide screen version */
      }}

      .print-pages-container {{
        display: block !important; /* Show print version */
      }}

      .print-app-container {{
        display: grid !important;
        grid-template-columns: 280px 1fr !important;
        width: 297mm !important;
        height: 167mm !important;
        page-break-after: always !important;
        break-after: page !important;
        background-color: white !important;
        overflow: hidden !important;
        position: relative !important;
      }}

      .print-app-container .sidebar {{
        background-color: var(--color-bg-sidebar) !important;
        border-right: 1px solid var(--color-border) !important;
        padding: 30px 25px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        height: 100% !important;
      }}

      .print-app-container .content-area {{
        padding: 30px 45px !important;
        overflow: hidden !important;
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
      }}

      /* Adjust interactive text-inputs/buttons to be static outlines during printing */
      .interactive-test, .download-btn-card {{
        background-color: white !important;
        border: 1px solid var(--color-border) !important;
      }}

      .preview-box {{
        border: 1px solid var(--color-border) !important;
        background-color: white !important;
      }}

      /* Ensure color swatches print perfectly */
      .swatch-color {{
        border: 1px solid rgba(0,0,0,0.05);
      }}

      .moodboard-backing {{
        grid-template-columns: repeat(4, 120px) !important;
        grid-template-rows: repeat(2, 150px) !important;
        min-height: 330px !important;
        gap: 12px !important;
        justify-content: center !important;
        align-content: center !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Screen shared version (exactly as viewed on screen) -->
  <div class="app-container">
    <!-- Screen Shared Sidebar -->
    <aside class="sidebar">
      <div class="logo-section">
        <span class="logo-label">DUAS MÃOS</span>
        <span class="logo-sub">DIREÇÃO DE ARTE / CORPORATIVO</span>
      </div>

      {get_nav_list_html(0)}

      <footer class="sidebar-footer">
        <div>Manual de Direção Criativa</div>
        <div>Versão 1.0 . Julho de 2026</div>
        <div style="margin-top: 8px; opacity: 0.6;">© Duas Mãos</div>
      </footer>
    </aside>

    <!-- Content Area containing active page tab -->
    <main class="content-area">
      <div class="header-top">
        <span class="header-meta">PROJETO ALICE STOFF . BRIEFING DE EDIÇÃO AUDIOVISUAL</span>
        <div class="header-actions">
          <button class="btn-header" onclick="switchTab('downloads')">
            <i data-lucide="download"></i>
            <span>Arquivos de Fontes</span>
          </button>
          <button class="btn-header primary" onclick="switchTab('quality')">
            <i data-lucide="check-circle"></i>
            <span>Checklist</span>
          </button>
        </div>
      </div>

      <div style="flex:1;">
        <!-- Tab: Cover -->
        <section id="cover" class="page-section active">
          {cover_section}
        </section>

        <!-- Tab: Intro -->
        <section id="intro" class="page-section">
          {intro_section}
        </section>

        <!-- Tab: Edit -->
        <section id="edit" class="page-section">
          {edit_section}
        </section>

        <!-- Tab: Subs -->
        <section id="subs" class="page-section">
          {subs_section}
        </section>

        <!-- Tab: Visual -->
        <section id="visual" class="page-section">
          {visual_section}
        </section>

        <!-- Tab: Quality -->
        <section id="quality" class="page-section">
          {quality_section}
        </section>

        <!-- Tab: Mood -->
        <section id="mood" class="page-section">
          {mood_section}
        </section>

        <!-- Tab: Downloads -->
        <section id="downloads" class="page-section">
          {downloads_section}
        </section>
      </div>

      <!-- Content screen footer -->
      <footer class="content-footer-note">
        <div>DUAS MÃOS DIREÇÃO DE ARTE</div>
        <div style="font-size:9px; color:var(--color-text-muted); margin-top:4px;">
          Este documento e seus ativos embutidos são propriedades corporativas exclusivas da Alice Stoff.
        </div>
      </footer>
    </main>
  </div>

  <!-- Print version wrapper (contains 8 print-app-containers printed sequentially) -->
  <div class="print-pages-container">
    {print_pages_html}
  </div>

  <!-- Zoom Overlay -->
  <div id="zoom-overlay" class="zoom-overlay" style="display:none;" onclick="closeZoom()">
    <div class="zoom-content" onclick="event.stopPropagation()">
      <img id="zoom-img" src="" alt="Zoomed reference" class="zoom-img">
      <div style="display:flex; justify-content:space-between; width:100%; align-items:center;">
        <span class="logo-sub" style="font-size:10px;">PROJETO ALICE STOFF . REFERÊNCIA DIGITAL</span>
        <button class="btn-header" onclick="closeZoom()"><i data-lucide="minimize-2"></i><span>Fechar</span></button>
      </div>
    </div>
  </div>

  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    // Initialize Lucide vector icons
    lucide.createIcons();

    function switchTab(tabId) {{
      // Toggle nav active state in the screen view
      const navItems = document.querySelectorAll('.app-container .nav-item');
      navItems.forEach(item => item.classList.remove('active'));
      
      const tabMapping = {{
        'cover': 0, 'intro': 1, 'edit': 2, 'subs': 3, 'visual': 4, 'quality': 5, 'mood': 6, 'downloads': 7
      }};
      navItems[tabMapping[tabId]].classList.add('active');

      // Toggle page content active state
      const sections = document.querySelectorAll('.app-container .page-section');
      sections.forEach(sec => sec.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
    }}

    function updateSimVal(val) {{
      // Update all typography preview inputs on the page
      const inputs = document.querySelectorAll('.sim-input-cls');
      inputs.forEach(input => input.value = val);

      const cosmos = document.querySelectorAll('.prev-cosmo-cls');
      cosmos.forEach(el => el.innerText = val);

      const alberts = document.querySelectorAll('.prev-albert-cls');
      alberts.forEach(el => el.innerText = val);
    }}

    // Toggle screen checkboxes
    function toggleCheck(el) {{
      el.classList.toggle('checked');
    }}

    function resetChecklist() {{
      const items = document.querySelectorAll('.check-item');
      items.forEach(item => item.classList.remove('checked'));
    }}

    function copyColor(hex) {{
      navigator.clipboard.writeText(hex);
      alert('Cor copiada: ' + hex);
    }}

    function zoomImage(src) {{
      document.getElementById('zoom-img').src = src;
      document.getElementById('zoom-overlay').style.display = 'flex';
    }}

    function closeZoom() {{
      document.getElementById('zoom-overlay').style.display = 'none';
    }}
  </script>
</body>
</html>
"""
    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML único salvo com sucesso em: {HTML_OUTPUT_PATH}")

def convert_html_to_pdf():
    # Use Google Chrome in headless print mode to convert HTML directly to the target PDF path
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={PDF_OUTPUT_PATH}",
        f"file://{HTML_OUTPUT_PATH}"
    ]
    print(f"Executando conversão HTML -> PDF com comando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("PDF gerado com sucesso a partir do HTML via Headless Chrome.")
    else:
        print(f"Erro na geração do PDF: {result.stderr}")

def embed_fonts_and_interactions():
    # Read font bytes
    with open("Cosmodrome-Monoline.otf", "rb") as f:
        cosmo_data = f.read()
    with open("AlbertSans-Regular.ttf", "rb") as f:
        regular_data = f.read()
    with open("AlbertSans-Bold.ttf", "rb") as f:
        bold_data = f.read()
    with open("AlbertSans-Italic.ttf", "rb") as f:
        italic_data = f.read()

    doc = fitz.open(PDF_OUTPUT_PATH)
    
    # 1. Add sidebar links and header button links to ALL pages
    menu_items = [
        "Capa & Autoria",
        "Conceito & Posicionamento",
        "Diretrizes de Edição",
        "Legendas & Grafismos",
        "Cores & Tipografia",
        "Checklist de Qualidade",
        "Moodboard de Referências",
        "Arquivos & Downloads"
    ]

    for p in range(len(doc)):
        page = doc[p]
        
        # Sidebar page jump links
        for target_idx, item_text in enumerate(menu_items):
            rects = page.search_for(item_text)
            sidebar_rects = [r for r in rects if r.x1 < 280]
            if sidebar_rects:
                rect = sidebar_rects[0]
                # Bounding box covering the whole row in sidebar
                clickable_rect = fitz.Rect(15, rect.y0 - 5, rect.x1 + 10, rect.y1 + 5)
                page.insert_link({
                    "kind": fitz.LINK_GOTO,
                    "page": target_idx,
                    "from": clickable_rect
                })
                
        # Header "Arquivos de Fontes" link
        font_btn_rects = [r for r in page.search_for("Arquivos de Fontes") if r.x0 > 280]
        if font_btn_rects:
            rect = font_btn_rects[0]
            btn_rect = fitz.Rect(rect.x0 - 25, rect.y0 - 6, rect.x1 + 10, rect.y1 + 6)
            page.insert_link({
                "kind": fitz.LINK_GOTO,
                "page": 7,  # Jump to Downloads page
                "from": btn_rect
            })
            
        # Header "Checklist" link
        checklist_btn_rects = [r for r in page.search_for("Checklist") if r.x0 > 500 and r.y0 < 80]
        if checklist_btn_rects:
            rect = checklist_btn_rects[0]
            btn_rect = fitz.Rect(rect.x0 - 25, rect.y0 - 6, rect.x1 + 15, rect.y1 + 6)
            page.insert_link({
                "kind": fitz.LINK_GOTO,
                "page": 5,  # Jump to Checklist page
                "from": btn_rect
            })

    # 2. Add interactive Checkbox widgets on Page 6 (Checklist)
    checklist_page = doc[5]
    checklist_items = [
        "Tipografia correta (Albert Sans e Cosmodrome)",
        "Paleta de cores oficial aplicada sem ruído",
        "Lettering manuscrito com boa escala",
        "Capa integrada e consistente com o feed",
        "Pausas da fala respeitadas",
        "Legendas 100% legíveis com Off White",
        "Grafismos com propósito narrativo claro",
        "Sem excesso de filtros e efeitos de zoom",
        "Vídeo reflete autoridade da Alice Stoff",
        "Branding discreto e de tom elegante",
        "Visual editorial consolidado e moderno",
        "Consistência estética e de paleta de cores"
    ]

    for idx, item_text in enumerate(checklist_items):
        rects = checklist_page.search_for(item_text)
        if rects:
            rect = rects[0]
            widget = fitz.Widget()
            # Place the widget exactly over the HTML-rendered checkbox box
            widget.rect = fitz.Rect(rect.x0 - 24, rect.y0 - 1, rect.x0 - 10, rect.y0 + 13)
            widget.field_type = fitz.PDF_WIDGET_TYPE_CHECKBOX
            widget.field_name = f"Check_{idx}"
            widget.field_value = "Off"
            checklist_page.add_widget(widget)

    # 3. Add font file attachments on Page 8 (Downloads) and embed in the PDF globally
    downloads_page = doc[7]
    fonts_mapping = [
        ("Cosmodrome Monoline", cosmo_data, "Cosmodrome Monoline.otf"),
        ("Albert Sans Regular", regular_data, "AlbertSans-Regular.ttf"),
        ("Albert Sans Bold", bold_data, "AlbertSans-Bold.ttf"),
        ("Albert Sans Italic", italic_data, "AlbertSans-Italic.ttf")
    ]

    for search_str, file_bytes, filename in fonts_mapping:
        rects = downloads_page.search_for(search_str)
        if rects:
            rect = rects[0]
            # Embed file in PDF globally (so it appears in the Attachments Pane/Tab)
            doc.embfile_add(filename, file_bytes)
            # Add visual clickable file attachment annotation on Page 8
            downloads_page.add_file_annot(fitz.Point(rect.x1 + 10, rect.y0), file_bytes, filename)
            print(f"Embutido {filename} na página 8 e anexado ao catálogo global do PDF.")

    # Save to a temporary file, then overwrite original
    temp_path = PDF_OUTPUT_PATH + ".tmp"
    doc.save(temp_path)
    doc.close()
    os.replace(temp_path, PDF_OUTPUT_PATH)
    print("Interações de PDF (links, checklists, anexos) adicionadas e salvas com sucesso.")

def render_pages_to_images():
    # Render PDF pages to PNG using PyMuPDF (fitz)
    doc = fitz.open(PDF_OUTPUT_PATH)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        output_image_path = os.path.join(CLIENT_DIR, f"briefing_page_{i+1}.png")
        pix.save(output_image_path)
        print(f"Página {i+1} renderizada como imagem em: {output_image_path}")

if __name__ == "__main__":
    generate_single_html()
    convert_html_to_pdf()
    embed_fonts_and_interactions()
    render_pages_to_images()
