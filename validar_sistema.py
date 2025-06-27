#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VALIDADOR AUTOMÁTICO - Sistema FuncionárioIA
Verifica se todos os componentes estão funcionando corretamente
"""

import requests
import time
import subprocess
import json
from pathlib import Path

class ValidadorSistema:
    def __init__(self):
        self.base_url = "http://localhost:5173"
        self.projeto_path = Path("agent-aloha-ai")
        
    def verificar_servidor_rodando(self):
        """Verifica se o servidor React está rodando"""
        try:
            response = requests.get(self.base_url, timeout=5)
            if response.status_code == 200:
                print("✅ SERVIDOR REACT FUNCIONANDO")
                return True
            else:
                print(f"❌ SERVIDOR REACT RETORNOU STATUS: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ SERVIDOR REACT NÃO RESPONDE: {e}")
            return False
    
    def verificar_estrutura_arquivos(self):
        """Verifica se todos os arquivos essenciais existem"""
        arquivos_essenciais = [
            "agent-aloha-ai/package.json",
            "agent-aloha-ai/src/App.tsx", 
            "agent-aloha-ai/src/components/MonetizedAgentBuilder.tsx",
            "agent-aloha-ai/src/components/CalibrationChat.tsx",
            "agent-aloha-ai/src/components/ConfigurationEditor.tsx",
            "iniciar_sistema.bat",
            "teste_fluxo_completo.py",
            "teste_manual_validacao.md"
        ]
        
        print("\n🔍 VERIFICANDO ESTRUTURA DE ARQUIVOS...")
        todos_ok = True
        
        for arquivo in arquivos_essenciais:
            if Path(arquivo).exists():
                print(f"✅ {arquivo}")
            else:
                print(f"❌ {arquivo} - FALTANDO!")
                todos_ok = False
        
        return todos_ok
    
    def verificar_dependencias(self):
        """Verifica se as dependências estão instaladas"""
        print("\n🔍 VERIFICANDO DEPENDÊNCIAS...")
        
        node_modules = self.projeto_path / "node_modules"
        package_lock = self.projeto_path / "package-lock.json"
        
        if node_modules.exists() and package_lock.exists():
            print("✅ DEPENDÊNCIAS INSTALADAS")
            return True
        else:
            print("❌ DEPENDÊNCIAS NÃO INSTALADAS")
            return False
    
    def verificar_logica_python(self):
        """Executa o teste Python para validar a lógica"""
        print("\n🧪 EXECUTANDO TESTE LÓGICA PYTHON...")
        
        try:
            resultado = subprocess.run(
                ["python", "teste_fluxo_completo.py"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if resultado.returncode == 0:
                output = resultado.stdout
                
                # Verificar se os testes passaram
                if "🎉 CONFIGURAÇÃO COMPLETA!" in output and "100% completo" in output:
                    print("✅ LÓGICA PYTHON FUNCIONANDO")
                    
                    # Contar quantos estabelecimentos foram configurados 100%
                    configurados_100 = output.count("100% completo")
                    print(f"✅ {configurados_100} ESTABELECIMENTOS CONFIGURADOS 100%")
                    
                    return True
                else:
                    print("❌ LÓGICA PYTHON COM PROBLEMAS")
                    print("OUTPUT:", output[:500])
                    return False
            else:
                print(f"❌ ERRO NA EXECUÇÃO: {resultado.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ TIMEOUT NO TESTE PYTHON")
            return False
        except Exception as e:
            print(f"❌ ERRO EXECUTANDO TESTE: {e}")
            return False
    
    def verificar_codigo_react(self):
        """Verifica se o código React tem as funcionalidades corretas"""
        print("\n🔍 VERIFICANDO CÓDIGO REACT...")
        
        # Verificar CalibrationChat.tsx
        calibration_file = self.projeto_path / "src/components/CalibrationChat.tsx"
        
        if not calibration_file.exists():
            print("❌ CalibrationChat.tsx NÃO ENCONTRADO")
            return False
            
        with open(calibration_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Verificações críticas
        verificacoes = [
            ("ESTRATÉGIA 1", "detectar nome inteligente"),
            ("mistral-large", "modelo correto"),
            ("analyzeAndUpdateAgent", "função de análise"),
            ("detectarNomeInteligente", "detecção de nome"),
            ("TEMPLATE RESTAURANTE", "template automático"),
            ("businessName", "dados do agente")
        ]
        
        todas_ok = True
        for termo, descricao in verificacoes:
            if termo.lower() in content.lower():
                print(f"✅ {descricao.upper()}")
            else:
                print(f"❌ {descricao.upper()} - FALTANDO!")
                todas_ok = False
        
        return todas_ok
    
    def gerar_relatorio(self):
        """Gera relatório completo do sistema"""
        print(f"\n{'='*60}")
        print("📊 RELATÓRIO COMPLETO DO SISTEMA")
        print(f"{'='*60}")
        
        testes = [
            ("Servidor React", self.verificar_servidor_rodando),
            ("Estrutura de Arquivos", self.verificar_estrutura_arquivos),
            ("Dependências", self.verificar_dependencias),
            ("Lógica Python", self.verificar_logica_python),
            ("Código React", self.verificar_codigo_react)
        ]
        
        resultados = {}
        total_testes = len(testes)
        testes_passaram = 0
        
        for nome, teste_func in testes:
            print(f"\n🧪 EXECUTANDO: {nome}")
            resultado = teste_func()
            resultados[nome] = resultado
            
            if resultado:
                testes_passaram += 1
                print(f"✅ {nome}: PASSOU")
            else:
                print(f"❌ {nome}: FALHOU")
        
        # Resumo final
        print(f"\n{'='*60}")
        print("🏆 RESUMO FINAL")
        print(f"{'='*60}")
        print(f"✅ TESTES PASSARAM: {testes_passaram}/{total_testes}")
        print(f"📊 TAXA DE SUCESSO: {(testes_passaram/total_testes)*100:.1f}%")
        
        if testes_passaram == total_testes:
            print("\n🎉 SISTEMA 100% FUNCIONAL!")
            print("🚀 PRONTO PARA PRODUÇÃO!")
            return True
        else:
            print(f"\n⚠️ SISTEMA {(testes_passaram/total_testes)*100:.1f}% FUNCIONAL")
            print("🔧 REQUER AJUSTES ANTES DA PRODUÇÃO")
            
            # Listar problemas
            print("\n❌ PROBLEMAS ENCONTRADOS:")
            for nome, resultado in resultados.items():
                if not resultado:
                    print(f"  • {nome}")
            
            return False

def main():
    """Função principal"""
    print("🔧 VALIDADOR AUTOMÁTICO - FuncionárioIA")
    print("Verificando todos os componentes do sistema...\n")
    
    validador = ValidadorSistema()
    sistema_ok = validador.gerar_relatorio()
    
    if sistema_ok:
        print("\n📋 PRÓXIMOS PASSOS:")
        print("1. ✅ Sistema validado e funcionando")
        print("2. 🌐 Acesse: http://localhost:5173")
        print("3. 🧪 Execute teste manual: teste_manual_validacao.md") 
        print("4. 🚀 Deploy para produção quando pronto")
    else:
        print("\n🔧 AÇÕES NECESSÁRIAS:")
        print("1. Corrigir problemas encontrados")
        print("2. Executar validador novamente")
        print("3. Só fazer deploy após 100% dos testes passarem")

if __name__ == "__main__":
    main() 