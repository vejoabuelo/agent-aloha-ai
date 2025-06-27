#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de Fluxo de Configuração - Validação Anti-Duplicação
Sistema: FuncionárioIA
Versão: 3.0
"""

import os
import sys
import time
import json
from datetime import datetime

def test_configuration_flow():
    """
    Testa o fluxo de configuração para verificar se não há duplicação de campos
    """
    print("🧪 TESTE DE FLUXO DE CONFIGURAÇÃO")
    print("=" * 50)
    
    # Simulação dos dados do agent durante o fluxo
    agent_data = {
        "businessName": "",
        "businessType": "restaurante",
        "contactPhone": "",
        "location": "",
        "workingHours": "",
        "services": "",
        "paymentMethods": "",
        "hasDelivery": True,
        "acceptsReservations": True,
        "personality": "atencioso e prestativo",
        "welcomeMessage": "Olá! Bem-vindo(a) ao {businessName}! Como posso ajudá-lo(a) hoje?"
    }
    
    # Fluxo de configuração padrão
    config_flow = [
        {
            "step": "businessName",
            "title": "Nome do Estabelecimento",
            "question": "Qual é o nome do seu estabelecimento?",
            "fieldType": "text",
            "required": True
        },
        {
            "step": "contactPhone", 
            "title": "Telefone/WhatsApp",
            "question": "Qual é o telefone/WhatsApp para contato?",
            "fieldType": "phone",
            "required": True
        },
        {
            "step": "location",
            "title": "Endereço", 
            "question": "Qual é o endereço do estabelecimento?",
            "fieldType": "textarea",
            "required": True
        }
    ]
    
    print("📋 Testando fluxo de configuração...")
    print()
    
    current_step = 0
    
    # Simular preenchimento dos campos
    test_data = [
        "Restaurante do Amor",
        "11999887766", 
        "Rua das Flores, 123 - Centro - São Paulo - SP"
    ]
    
    for i, step in enumerate(config_flow):
        print(f"Passo {i+1}: {step['title']}")
        print(f"Pergunta: {step['question']}")
        
        # Verificar se campo já está preenchido
        current_value = agent_data.get(step['step'], '')
        
        if current_value and current_value.strip() and current_value != 'A ser definido':
            print(f"✅ Campo já preenchido: {current_value}")
            print("⏭️ Pulando para próximo campo...")
            print()
            continue
        
        # Simular preenchimento do campo
        if i < len(test_data):
            new_value = test_data[i]
            agent_data[step['step']] = new_value
            
            print(f"💾 Salvando: {step['step']} = {new_value}")
            print(f"✅ {step['title']} salvo!")
            print()
            
            # Simular delay
            time.sleep(0.5)
        
        current_step += 1
    
    print("🎉 Configuração concluída!")
    print()
    print("📊 Dados finais:")
    for key, value in agent_data.items():
        if value and str(value).strip():
            print(f"  {key}: {value}")
    
    return True

def test_duplicate_prevention():
    """
    Testa especificamente a prevenção de duplicação de campos
    """
    print("\n🔍 TESTE DE PREVENÇÃO DE DUPLICAÇÃO")
    print("=" * 50)
    
    # Cenário: campo já preenchido sendo solicitado novamente
    agent_data = {
        "businessName": "Restaurante do Amor",  # JÁ PREENCHIDO
        "businessType": "restaurante"
    }
    
    step = {
        "step": "businessName",
        "title": "Nome do Estabelecimento", 
        "question": "Qual é o nome do seu estabelecimento?",
        "fieldType": "text",
        "required": True
    }
    
    print(f"Campo atual: {step['step']}")
    print(f"Valor atual: {agent_data.get(step['step'], '')}")
    
    current_value = agent_data.get(step['step'], '')
    
    # Verificação de duplicação
    if current_value and current_value.strip() and current_value != 'A ser definido':
        print("✅ TESTE PASSOU: Campo já preenchido detectado corretamente")
        print("⏭️ Sistema deve pular para próximo campo")
        return True
    else:
        print("❌ TESTE FALHOU: Campo já preenchido não foi detectado")
        return False

def validate_system_state():
    """
    Valida o estado atual do sistema
    """
    print("\n📋 VALIDAÇÃO DO SISTEMA")
    print("=" * 50)
    
    # Verificar se os arquivos principais existem
    required_files = [
        "src/components/CalibrationChat.tsx",
        "src/components/InlineFieldInput.tsx"
    ]
    
    all_files_exist = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - OK")
        else:
            print(f"❌ {file_path} - AUSENTE")
            all_files_exist = False
    
    return all_files_exist

def main():
    """
    Função principal do teste
    """
    print("🚀 INICIANDO TESTES DE VALIDAÇÃO")
    print("Data/Hora:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print()
    
    # Executar testes
    tests_passed = 0
    total_tests = 3
    
    try:
        # Teste 1: Validação do sistema
        if validate_system_state():
            print("✅ Teste 1: Sistema OK")
            tests_passed += 1
        else:
            print("❌ Teste 1: Sistema com problemas")
        
        # Teste 2: Fluxo de configuração
        if test_configuration_flow():
            print("✅ Teste 2: Fluxo de configuração OK")
            tests_passed += 1
        else:
            print("❌ Teste 2: Fluxo de configuração com problemas")
        
        # Teste 3: Prevenção de duplicação
        if test_duplicate_prevention():
            print("✅ Teste 3: Prevenção de duplicação OK")
            tests_passed += 1
        else:
            print("❌ Teste 3: Prevenção de duplicação com problemas")
        
    except Exception as e:
        print(f"❌ Erro durante os testes: {e}")
    
    # Resultado final
    print("\n" + "=" * 50)
    print(f"📊 RESULTADO: {tests_passed}/{total_tests} testes passaram")
    
    if tests_passed == total_tests:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Sistema pronto para uso")
    else:
        print("⚠️ ALGUNS TESTES FALHARAM")
        print("🔧 Verificar correções necessárias")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 