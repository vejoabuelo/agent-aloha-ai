@echo off
title FuncionarioIA - Sistema de Funcionarios Virtuais
color 0A
echo.
echo ========================================
echo  FuncionarioIA - Sistema ATUALIZADO!
echo ========================================
echo.
echo ✅ NOVAS FUNCIONALIDADES IMPLEMENTADAS:
echo.
echo 📱 Sistema de Perguntas Inteligentes:
echo    → Restaurantes: pergunta sobre entrega, taxa e reservas
echo    → Clinicas: pergunta sobre consultas e procedimentos
echo    → Lojas: pergunta sobre produtos e atendimento
echo.
echo 🧠 Sistema de Conhecimento Proprio:
echo    → IA conhece todas informacoes ja configuradas
echo    → Responde duvidas sobre precos, horarios, servicos
echo    → Nao inventa informacoes, usa dados reais
echo.
echo 📝 Editor Manual de Campos:
echo    → Botao "Editar" no lado esquerdo
echo    → Editar todos os campos manualmente
echo    → Botao "Salvar" para aplicar mudancas
echo    → Efeitos aparecem no teste automaticamente
echo.
echo 📋 Gestao Inteligente de Cardapio:
echo    → Sistema pergunta: "SUBSTITUIR ou ADICIONAR?"
echo    → Entende intencao: alterar = substituir
echo    → Entende intencao: acrescentar = adicionar
echo.
echo 💰 Sistema de Pagamento Completo:
echo    → PIX: 17 99161-0665 (com QR Code automatico)
echo    → Cartao: erro automatico + suporte WhatsApp
echo    → Planos: Starter R$47, Pro R$97, Enterprise R$197
echo.
echo 📞 Suporte WhatsApp Integrado:
echo    → Botao "Conectar WhatsApp" → assinar plano
echo    → Botao "Publicar" → obrigatorio assinar
echo    → Erro no pagamento → suporte (11) 3230-0474
echo    → Mensagens automaticas para WhatsApp
echo.
echo 🎨 Design Estilo ChatGPT:
echo    → Fontes: -apple-system, Segoe UI, Roboto
echo    → Tamanhos menores e mais elegantes
echo    → Layout fixo (lado esquerdo e direito)
echo    → Campo de input fixo na parte inferior
echo    → Responsivo para desktop e mobile
echo.
echo ========================================
echo.

REM Verificar se Node.js esta instalado
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERRO: Node.js nao encontrado!
    echo.
    echo 📥 Por favor, instale o Node.js:
    echo https://nodejs.org
    echo.
    pause
    exit /b 1
)

echo 🚀 Iniciando FuncionarioIA...
echo.

REM Navegar para a pasta do projeto
cd /d "%~dp0agent-aloha-ai"
if %errorlevel% neq 0 (
    echo ❌ ERRO: Pasta agent-aloha-ai nao encontrada!
    echo.
    echo 📁 Verifique se a pasta existe no mesmo local deste arquivo .bat
    echo.
    pause
    exit /b 1
)

echo 📦 Verificando dependencias...
if not exist "node_modules" (
    echo 📥 Instalando dependencias pela primeira vez...
    echo Isso pode levar alguns minutos...
    npm install
    if %errorlevel% neq 0 (
        echo ❌ ERRO na instalacao das dependencias!
        pause
        exit /b 1
    )
)

echo.
echo ✅ Sistema pronto! Funcionalidades disponiveis:
echo.
echo 1. Templates de Negocio (6 tipos diferentes)
echo 2. Chat IA com Mistral Large 2.1
echo 3. Deteccao automatica de informacoes
echo 4. Editor manual com campos editaveis
echo 5. Sistema de pagamento PIX + Cartao
echo 6. Conectar WhatsApp automatico
echo 7. Suporte via WhatsApp integrado
echo 8. Simulador de WhatsApp para testes
echo 9. Gestao inteligente de cardapio
echo 10. Sistema de conhecimento proprio
echo.
echo 🌐 Abrindo sistema em: http://localhost:5173
echo.

REM Matar processos Node.js existentes
taskkill /f /im node.exe >nul 2>&1

REM Aguardar um momento
timeout /t 2 /nobreak >nul

REM Iniciar o servidor
start /b npm run dev

REM Aguardar o servidor iniciar
echo ⏳ Aguardando servidor inicializar...
timeout /t 8 /nobreak >nul

REM Abrir navegador
start http://localhost:5173

echo.
echo ========================================
echo  FuncionarioIA EXECUTANDO!
echo ========================================
echo.
echo 📱 Sistema rodando em: http://localhost:5173
echo.
echo 💡 COMO USAR:
echo 1. Escolha um template de negocio
echo 2. Converse com a IA para configurar
echo 3. Use o botao "Editar" para ajustes manuais
echo 4. Teste no WhatsApp com o botao "Testar"
echo 5. Conecte ao WhatsApp real (requer assinatura)
echo 6. Publique seu funcionario IA
echo.
echo 🆘 SUPORTE: (11) 3230-0474 via WhatsApp
echo 💰 PIX para pagamentos: 17 99161-0665
echo.
echo Para parar o sistema, feche esta janela.
echo.
pause 