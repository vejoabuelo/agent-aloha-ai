#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE DE LÓGICA - Sistema FuncionárioIA
Teste para calibrar detecção e salvamento correto
"""

import re
import json
from typing import Dict, List, Optional

class AgentData:
    def __init__(self):
        self.businessName = ""
        self.businessType = ""
        self.contactPhone = ""
        self.location = ""
        self.services = ""
        self.workingHours = ""
        self.paymentMethods = ""
        self.personality = ""

    def to_dict(self):
        return {
            'businessName': self.businessName,
            'businessType': self.businessType,
            'contactPhone': self.contactPhone,
            'location': self.location,
            'services': self.services,
            'workingHours': self.workingHours,
            'paymentMethods': self.paymentMethods,
            'personality': self.personality
        }

def test_analise_inteligente(content: str, agent_data: AgentData) -> Dict:
    """
    TESTE DA LÓGICA DE ANÁLISE INTELIGENTE
    """
    print(f"\n🧠 TESTE ANÁLISE: {content}")
    text = content.lower()
    updates = {}
    saved_something = False
    
    # ESTADO ATUAL ANTES DA ANÁLISE
    print(f"📋 ESTADO ANTES:")
    print(f"  Nome: '{agent_data.businessName}'")
    print(f"  Telefone: '{agent_data.contactPhone}'")
    print(f"  Endereço: '{agent_data.location}'")
    print(f"  Serviços: '{agent_data.services}'")
    
    # DETECÇÃO DE NOME - TESTE RIGOROSO CORRIGIDO
    if not agent_data.businessName or len(agent_data.businessName) < 3 or "nome do seu" in agent_data.businessName.lower():
        print("🔍 Procurando NOME...")
        
        # Padrões de detecção de nome - CORRIGIDOS
        nome_patterns = [
            r'(?:restaurante|pizzaria|loja|oficina|clínica)\s+([a-zA-ZÀ-ÿ\s\']{2,30})',  # "restaurante do amor"
            r'([a-zA-ZÀ-ÿ\s\']{2,30})\s+(?:restaurante|pizzaria|loja|oficina|clínica)',  # "amor restaurante"
            r'(?:chama|nome|chamado|se chama)\s+([a-zA-ZÀ-ÿ\s\']{2,30})',  # "se chama Pizza Legal"
            r'"([a-zA-ZÀ-ÿ\s\']{2,25})"',  # "Pizza do Amor"
            r'\b([A-ZÀ-Ÿ][a-zA-ZÀ-ÿ]{2,}\s+[A-ZÀ-Ÿ][a-zA-ZÀ-ÿ]{2,})\b',  # Pizza Legal (duas palavras capitalizadas)
            r'(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})',  # NOVO: captura "restaurante do amor" completo
            r'(pizzaria\s+[a-zA-ZÀ-ÿ\s\']{2,30})',     # NOVO: captura "pizzaria da mama" completo
            r'([a-zA-ZÀ-ÿ\s\']{2,30}\s+restaurante)',  # NOVO: captura "do amor restaurante" completo
        ]
        
        for pattern in nome_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                nome_raw = match.group(1) if len(match.groups()) > 0 else match.group(0)
                nome = nome_raw.strip()
                print(f"  🎯 Candidato RAW: '{nome_raw}' -> Limpo: '{nome}'")
                
                # Validação rigorosa CORRIGIDA
                if (3 <= len(nome) <= 50):
                    # Se contém a palavra tipo (restaurante, pizzaria), manter completo
                    if any(tipo in nome.lower() for tipo in ['restaurante', 'pizzaria', 'loja', 'oficina', 'clínica']):
                        nome_final = nome
                    else:
                        # Se não contém, é só o nome
                        nome_final = nome
                    
                    updates['businessName'] = nome_final
                    agent_data.businessName = nome_final
                    saved_something = True
                    print(f"  ✅ NOME SALVO: '{nome_final}'")
                    break
            if 'businessName' in updates:
                break
    else:
        print("✅ Nome já existe, pulando detecção")
    
    # DETECÇÃO DE TELEFONE - TESTE RIGOROSO
    if not agent_data.contactPhone or "xxxxx" in agent_data.contactPhone or len(agent_data.contactPhone) < 10:
        print("🔍 Procurando TELEFONE...")
        
        telefone_patterns = [
            r'(?:telefone|celular|whatsapp|contato|fone|número)\D*(\d{10,11})',
            r'\(?\d{2}\)?\s*\d{4,5}[-.\s]?\d{4}',
            r'(\d{11})',
            r'(\d{10})'
        ]
        
        for pattern in telefone_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                telefone = re.sub(r'\D', '', match.group(1) if match.group(1) else match.group(0))
                print(f"  🎯 Candidato: '{telefone}'")
                
                if 10 <= len(telefone) <= 11 and telefone != '11987654321':
                    updates['contactPhone'] = telefone
                    agent_data.contactPhone = telefone
                    saved_something = True
                    print(f"  ✅ TELEFONE SALVO: '{telefone}'")
                    break
            if 'contactPhone' in updates:
                break
    else:
        print("✅ Telefone já existe, pulando detecção")
    
    # APLICAR TEMPLATE SE NECESSÁRIO
    if ('restaurante' in text or 'pizza' in text) and not agent_data.businessType:
        print("🍕 Aplicando TEMPLATE RESTAURANTE...")
        updates.update({
            'businessType': 'restaurante',
            'personality': 'amigável, carinhoso e atencioso',
            'workingHours': 'Segunda a Domingo: 10h às 23h',
            'paymentMethods': 'PIX, Cartão de crédito, Cartão de débito, Dinheiro'
        })
        # Aplicar ao objeto
        agent_data.businessType = updates['businessType']
        agent_data.personality = updates['personality']
        agent_data.workingHours = updates['workingHours']
        agent_data.paymentMethods = updates['paymentMethods']
        saved_something = True
        print("  ✅ TEMPLATE RESTAURANTE APLICADO")
    
    # ESTADO FINAL APÓS ANÁLISE
    print(f"📋 ESTADO DEPOIS:")
    print(f"  Nome: '{agent_data.businessName}'")
    print(f"  Telefone: '{agent_data.contactPhone}'")
    print(f"  Endereço: '{agent_data.location}'")
    print(f"  Serviços: '{agent_data.services}'")
    print(f"  Tipo: '{agent_data.businessType}'")
    
    print(f"💾 SALVOU ALGO: {saved_something}")
    print(f"🔄 UPDATES: {updates}")
    
    return {
        'updates': updates,
        'saved_something': saved_something,
        'final_state': agent_data.to_dict()
    }

def verificar_o_que_falta(agent_data: AgentData) -> List[str]:
    """
    VERIFICAR O QUE REALMENTE ESTÁ FALTANDO
    """
    falta = []
    
    if not agent_data.businessName or len(agent_data.businessName) < 3 or "nome do seu" in agent_data.businessName.lower():
        falta.append("NOME DO NEGÓCIO")
    
    if not agent_data.contactPhone or "xxxxx" in agent_data.contactPhone or len(agent_data.contactPhone) < 10:
        falta.append("TELEFONE")
        
    if not agent_data.location or "ser definido" in agent_data.location.lower() or len(agent_data.location) < 5:
        falta.append("ENDEREÇO")
        
    if not agent_data.services or "ser definido" in agent_data.services.lower() or "será criada" in agent_data.services.lower():
        falta.append("CARDÁPIO/SERVIÇOS")
    
    return falta

def teste_completo():
    """
    TESTE COMPLETO DO FLUXO
    """
    print("="*80)
    print("🧪 TESTE COMPLETO - LÓGICA FUNCIONÁRIO IA")
    print("="*80)
    
    # Estado inicial
    agent = AgentData()
    agent.businessName = "Qual é o nome do seu"  # Estado inicial genérico
    agent.contactPhone = "(xx) xxxxx-xxxx"
    agent.location = "Endereço a ser definido"
    agent.services = "Lista de serviços será criada automaticamente"
    
    print("\n📋 ESTADO INICIAL:")
    print(json.dumps(agent.to_dict(), indent=2, ensure_ascii=False))
    
    # TESTE 1: Mensagem com nome de restaurante
    print("\n" + "="*50)
    print("TESTE 1: 'restaurante do amor'")
    resultado1 = test_analise_inteligente("restaurante do amor", agent)
    
    falta1 = verificar_o_que_falta(agent)
    print(f"❓ AINDA FALTA: {falta1}")
    
    # TESTE 2: Resposta com telefone
    print("\n" + "="*50)
    print("TESTE 2: 'o telefone é 11987654322'")
    resultado2 = test_analise_inteligente("o telefone é 11987654322", agent)
    
    falta2 = verificar_o_que_falta(agent)
    print(f"❓ AINDA FALTA: {falta2}")
    
    # TESTE 3: Verificar se não repete pergunta sobre nome
    print("\n" + "="*50)
    print("TESTE 3: Verificação - deve detectar que nome JÁ EXISTE")
    print(f"Nome atual: '{agent.businessName}'")
    print(f"Deve detectar nome? {not agent.businessName or len(agent.businessName) < 3}")
    
    # Estado final
    print("\n📋 ESTADO FINAL:")
    print(json.dumps(agent.to_dict(), indent=2, ensure_ascii=False))
    
    falta_final = verificar_o_que_falta(agent)
    print(f"\n❓ FALTA NO FINAL: {falta_final}")
    
    if not falta_final:
        print("🎉 CONFIGURAÇÃO 100% COMPLETA!")
    else:
        print(f"⚠️ Ainda faltam: {', '.join(falta_final)}")

if __name__ == "__main__":
    teste_completo() 