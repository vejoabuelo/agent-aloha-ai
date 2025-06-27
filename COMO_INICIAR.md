# 🤖 Como Iniciar o FuncionárioIA

## 🚀 Opção 1: Inicialização Automática (Recomendado)

### Windows
```bash
# Clique duplo no arquivo ou execute no terminal:
iniciar_sistema.bat
```

### Manual
```bash
cd agent-aloha-ai
npm install
npm run dev
```

## 🌐 Acesso ao Sistema

Após executar, o sistema estará disponível em:
- **URL Principal:** http://localhost:8080
- **URL Alternativa:** http://localhost:5173

⚠️ **Importante:** O Vite pode usar portas diferentes (8080, 5173, 3000). Verifique a saída do terminal.

## 🎯 Como Usar

### 1. Interface Principal
- **Lado Esquerdo:** Editor de configuração markdown
- **Lado Direito:** Chat IA estilo ChatGPT

### 2. Templates Disponíveis
- 🍕 Restaurante
- 🏪 Loja/Comércio  
- 🔧 Oficina Mecânica
- 🏥 Clínica Médica
- 💼 Escritório/Consultoria
- 🏨 Hotel/Pousada

### 3. Fluxo de Configuração
1. **Escolha um template** ou descreva seu negócio
2. **Responda às perguntas** da IA
3. **Veja a configuração** sendo gerada automaticamente
4. **Teste no WhatsApp** usando o botão "Testar"

## 🛠️ Solução de Problemas

### Problema: "ConfigurationEditor não encontrado"
```bash
# Execute estes comandos:
cd agent-aloha-ai
npm install
npm run dev
```

### Problema: "Porta já em uso"
```bash
# Pare todos os processos Node.js:
taskkill /f /im node.exe

# Reinicie:
npm run dev
```

### Problema: "Cannot find module"
```bash
# Limpe o cache e reinstale:
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Problema: Página não carrega
1. Verifique se o terminal mostra "ready in XXXms"
2. Teste URLs alternativas:
   - http://localhost:8080
   - http://localhost:5173
   - http://localhost:3000

## 📱 Recursos Principais

### ✅ Interface ChatGPT
- Design minimalista preto/branco
- Fontes profissionais (System UI, Inter)
- Templates persuasivos clicáveis
- Campo de input expandido

### ✅ IA Conversacional
- Detecção automática de informações
- Mistral AI integrado
- Configuração em tempo real
- Análise inteligente de texto

### ✅ Editor de Configuração
- Formato markdown
- Sincronização automática
- Botões copiar/download
- Progresso visual

### ✅ Teste WhatsApp
- Simulação real de conversas
- Link direto para WhatsApp
- Teste de fluxos de atendimento

## 🔧 Comandos Úteis

```bash
# Iniciar desenvolvimento
npm run dev

# Construir para produção  
npm run build

# Prévia da build
npm run preview

# Limpar cache
npm cache clean --force

# Parar servidor
Ctrl + C
```

## 📋 Requisitos

- **Node.js** 16+ (recomendado 18+)
- **npm** ou **yarn**
- **Navegador** moderno (Chrome, Firefox, Edge)
- **Conexão** com internet (para IA Mistral)

## 🆘 Suporte

Se encontrar problemas:

1. **Verifique a versão do Node.js:** `node --version`
2. **Reinstale dependências:** `npm install`
3. **Limpe o cache:** `npm cache clean --force`
4. **Reinicie o servidor:** `npm run dev`

---

**✨ Sistema criado com React + TypeScript + Tailwind CSS + shadcn/ui**

## ✅ Interface Completamente Redesenhada - Estilo ChatGPT

### 🎯 **Layout Profissional**
- **Chat IA** (lado direito): Interface minimalista igual ao ChatGPT
- **Editor de Configuração** (lado esquerdo): Arquivo editável que atualiza automaticamente
- **Cores**: Preto e branco, tipografia profissional
- **UX**: Seguindo as melhores práticas do mercado

## 🔧 Como Usar

### 1. **Inicializar o Sistema**

**Opção A - Arquivo .BAT (Recomendado):**
```powershell
# Na pasta funcionario inteligente
.\iniciar_sistema.bat
```

**Opção B - Comandos Manuais:**
```powershell
cd agent-aloha-ai
npm install
npm run dev
```

### 2. **Interface Explicada**

#### 🎨 **Chat IA (Lado Direito)**
- **Visual igual ao ChatGPT**: Preto e branco, minimalista
- **Avatar preto**: Representa a IA assistente
- **Tipografia profissional**: Fonte e espaçamento idênticos
- **Área de input**: Rounded, com botão de envio estilo ChatGPT
- **Loading states**: Animações sutis

#### 📝 **Editor de Configuração (Lado Esquerdo)**
- **Arquivo de texto editável**: Formato markdown limpo
- **Atualização automática**: Conforme você conversa, o arquivo se preenche
- **Edição manual**: Clique e edite diretamente
- **Progresso visual**: Barra de progresso na parte superior
- **Botões de ação**: Copiar e baixar configuração

### 3. **Fluxo de Trabalho**

#### 🤖 **Configuração via Chat (Recomendado)**
1. **Inicie a conversa**: "Tenho um restaurante chamado Pizza do João"
2. **A IA extrai informações**: Nome automaticamente capturado
3. **Editor atualiza**: Lado esquerdo mostra as informações
4. **Continue detalhando**: Horários, serviços, localização
5. **Refinamento**: A IA sugere melhorias

#### ✏️ **Edição Manual**
1. **Clique no editor** (lado esquerdo)
2. **Edite diretamente** o arquivo de configuração
3. **Mudanças refletem** na conversa automaticamente

### 4. **Funcionalidades Avançadas**

#### 🎯 **Detecção Inteligente**
- **Nome do negócio**: "Meu restaurante se chama Pizza do João"
- **Horários**: "Funcionamos das 18h às 23h de segunda a sábado"
- **Serviços**: "Vendemos pizzas, massas e bebidas"
- **Localização**: "Ficamos no centro da cidade"

#### 💾 **Gerenciamento de Configuração**
- **Copiar**: Botão no topo do editor
- **Download**: Salva arquivo .txt
- **Sincronização**: Chat ↔ Editor em tempo real

#### 📱 **Teste WhatsApp**
- **Botão "Testar"**: No header superior
- **Simulador realista**: Interface igual ao WhatsApp
- **Validação completa**: Teste antes de publicar

## 🎨 Design System

### **Cores Principais**
- **Background**: `#ffffff` (Branco)
- **Texto**: `#111111` (Preto)
- **Bordas**: `#e5e5e5` (Cinza claro)
- **Botões**: `#000000` (Preto) / `hover: #1f1f1f`

### **Tipografia**
- **Fonte**: Inter/System UI (igual ChatGPT)
- **Tamanhos**: 14px (pequeno), 16px (base), 18px (títulos)
- **Peso**: 400 (normal), 500 (médio), 600 (bold)

### **Espaçamento**
- **Padding**: 16px (base), 24px (seções)
- **Margin**: 8px (pequeno), 16px (médio), 24px (grande)
- **Border-radius**: 8px (cards), 16px (botões)

## 📊 Exemplo de Uso

### **Conversa Típica:**
```
👤 Usuário: "Tenho uma loja de roupas femininas chamada Bella Moda"

🤖 IA: "Perfeito! Registrei o nome 'Bella Moda' como loja de roupas femininas. 
     Agora me conte sobre os horários de funcionamento e principais produtos."

👤 Usuário: "Abrimos de segunda a sábado das 9h às 18h. Vendemos vestidos, 
           blusas, calças e acessórios. Aceitamos cartão e PIX."

🤖 IA: "Ótimo! Atualizei as informações. Sua configuração está 80% completa. 
     Falta apenas a localização para finalizar."
```

### **Editor Resultante:**
```markdown
# Configuração do Funcionário IA

## Informações Básicas
Nome do Negócio: Bella Moda
Tipo de Negócio: loja de roupas femininas
Personalidade: amigável e profissional

## Horários de Funcionamento
Segunda a sábado das 9h às 18h

## Serviços Oferecidos
Vestidos, blusas, calças e acessórios

## Formas de Pagamento
Cartão e PIX

---
Configuração gerada automaticamente pelo FuncionárioIA
```

## 🔧 Troubleshooting

### **Sistema não inicia:**
```powershell
# Verificar Node.js
node --version

# Limpar cache
npm cache clean --force

# Reinstalar
npm install
```

### **Erro de porta ocupada:**
```powershell
# Matar processo na porta 5173
netstat -ano | findstr :5173
taskkill /PID [NUMERO_DO_PID] /F
```

### **Chat não responde:**
- Verifique conexão com internet
- API do Mistral pode estar temporariamente indisponível
- Tente novamente em alguns segundos

## 🎯 **Interface Comparada**

### **Antes (Antigo):**
- ❌ Cores coloridas demais
- ❌ Layout confuso
- ❌ Muitos elementos visuais
- ❌ Não seguia padrões do mercado

### **Agora (Novo):**
- ✅ **Minimalista como ChatGPT**
- ✅ **Preto e branco profissional**
- ✅ **Tipografia idêntica aos melhores**
- ✅ **UX testada e validada**
- ✅ **Editor de configuração intuitivo**
- ✅ **Sincronização chat ↔ editor**

---

**🚀 Sistema pronto para revolucionar seu atendimento!**

*Acesse: http://localhost:5173 após executar o sistema* 