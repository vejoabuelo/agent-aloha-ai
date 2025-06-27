#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TESTE FLUXO COMPLETO - Sistema FuncionárioIA
Simula conversação completa até configurar 100% estabelecimentos
"""

import re
import json
from typing import Dict, List, Optional

class AgentData:
    def __init__(self):
        self.businessName = "Como vai ser o nome do seu"
        self.businessType = ""
        self.contactPhone = "(xx) xxxxx-xxxx"
        self.location = "Endereço a ser definido"
        self.services = "Lista de serviços será criada automaticamente"
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

    def get_completion_status(self):
        """Retorna % de conclusão e campos faltantes"""
        total_fields = 8
        completed = 0
        missing = []
        
        if self.businessName and len(self.businessName) > 3 and "nome do seu" not in self.businessName.lower():
            completed += 1
        else:
            missing.append("NOME")
            
        if self.businessType:
            completed += 1
        else:
            missing.append("TIPO")
            
        if self.contactPhone and "xxxxx" not in self.contactPhone and len(self.contactPhone) >= 10:
            completed += 1
        else:
            missing.append("TELEFONE")
            
        if self.location and "ser definido" not in self.location.lower() and len(self.location) > 5:
            completed += 1
        else:
            missing.append("ENDEREÇO")
            
        if self.services and "será criada" not in self.services.lower() and "ser definido" not in self.services.lower():
            completed += 1
        else:
            missing.append("SERVIÇOS")
            
        if self.workingHours:
            completed += 1
        else:
            missing.append("HORÁRIOS")
            
        if self.paymentMethods:
            completed += 1
        else:
            missing.append("PAGAMENTO")
            
        if self.personality:
            completed += 1
        else:
            missing.append("PERSONALIDADE")
        
        percentage = int((completed / total_fields) * 100)
        return percentage, missing

class FuncionarioIASimulator:
    def __init__(self):
        self.agent_data = AgentData()
        
    def detectar_nome_inteligente(self, content: str) -> Optional[str]:
        """Detecção inteligente de nome com múltiplas estratégias CORRIGIDA"""
        print(f"    🔍 Detectando nome em: '{content}'")
        
        # ESTRATÉGIA 1: "nome é X" ou "se chama X" 
        match = re.search(r'(?:nome\s+(?:é|do\w*)\s*|se\s+chama\s+|chamado\s+|chama\s+)([a-zA-ZÀ-ÿ\s\']{2,40})', content, re.IGNORECASE)
        if match:
            nome = match.group(1).strip()
            # Limpar final comum
            nome = re.sub(r'\s*(?:restaurante|pizzaria|loja|oficina|clínica)$', '', nome, flags=re.IGNORECASE)
            if len(nome) >= 3:
                print(f"    📍 ESTRATÉGIA 1 (nome é/se chama): '{nome}'")
                return nome
        
        # ESTRATÉGIA 2: Capturar nome completo com tipo "restaurante do amor"
        if any(tipo in content.lower() for tipo in ['restaurante', 'pizzaria']):
            # "tenho um restaurante do amor" -> "restaurante do amor"
            match = re.search(r'(?:tenho\s+um\s+|é\s+um\s+)?(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
            if match:
                nome = match.group(1).strip()
                print(f"    📍 ESTRATÉGIA 2A (tenho um restaurante X): '{nome}'")
                return nome
            
            # "restaurante do amor" -> "restaurante do amor" 
            match = re.search(r'\b(restaurante\s+[a-zA-ZÀ-ÿ\s\']{2,30})', content, re.IGNORECASE)
            if match:
                nome = match.group(1).strip()
                print(f"    📍 ESTRATÉGIA 2B (restaurante X): '{nome}'")
                return nome
        
        # ESTRATÉGIA 3: Nome antes do tipo "amor restaurante"
        match = re.search(r'\b([a-zA-ZÀ-ÿ\s\']{2,30})\s+(restaurante|pizzaria|loja|oficina|clínica)', content, re.IGNORECASE)
        if match:
            nome = f"{match.group(1)} {match.group(2)}".strip()
            print(f"    📍 ESTRATÉGIA 3 (X tipo): '{nome}'")
            return nome
        
        # ESTRATÉGIA 4: Entre aspas
        match = re.search(r'"([a-zA-ZÀ-ÿ\s\']{2,30})"', content)
        if match:
            nome = match.group(1).strip()
            print(f"    📍 ESTRATÉGIA 4 (aspas): '{nome}'")
            return nome
        
        # ESTRATÉGIA 5: Palavras capitalizadas (melhorada)
        if not any(palavra in content.lower() for palavra in ['restaurante', 'pizzaria', 'loja', 'oficina', 'clínica']):
            # Se não tem tipo, procurar por palavras capitalizadas
            match = re.search(r'\b([A-ZÀ-Ÿ][a-zA-ZÀ-ÿ\s\']{2,30}[A-ZÀ-Ÿ][a-zA-ZÀ-ÿ]+)\b', content)
            if match:
                nome = match.group(1).strip()
                # Filtrar palavras comuns
                if not any(palavra in nome.lower() for palavra in ['auto center', 'nome', 'telefone', 'contato']):
                    print(f"    📍 ESTRATÉGIA 5 (capitalizadas): '{nome}'")
                    return nome
        
        print("    ❌ NENHUMA ESTRATÉGIA DE NOME FUNCIONOU")
        return None

    def analisar_e_atualizar(self, content: str) -> Dict:
        """Análise inteligente e atualização do agent_data - CORRIGIDA"""
        text = content.lower()
        updates = {}
        saved_something = False
        
        print(f"  🧠 ANÁLISE: '{content}'")
        
        # AUTO-COMPLETAR TEMPLATE PRIMEIRO (mas não sobrescrever nome)
        nome_antes = self.agent_data.businessName
        
        if (('restaurante' in text or 'pizza' in text) and not self.agent_data.businessType):
            print("    🍕 Aplicando TEMPLATE RESTAURANTE...")
            template_updates = {
                'businessType': 'restaurante',
                'personality': 'amigável, carinhoso e atencioso',
                'workingHours': 'Segunda a Domingo: 10h às 23h',
                'paymentMethods': 'PIX, Cartão de crédito, Cartão de débito, Dinheiro'
            }
            updates.update(template_updates)
            
            # Aplicar ao objeto
            for key, value in template_updates.items():
                setattr(self.agent_data, key, value)
            
            if not updates.get('services') and "será criada" in self.agent_data.services:
                updates['services'] = 'Cardápio variado, Delivery, Balcão, Reservas disponíveis'
                self.agent_data.services = updates['services']
            
            saved_something = True
            print("    ✅ TEMPLATE RESTAURANTE APLICADO")
        
        elif (('loja' in text or 'venda' in text) and not self.agent_data.businessType):
            print("    🛍️ Aplicando TEMPLATE LOJA...")
            template_updates = {
                'businessType': 'loja',
                'personality': 'prestativo, atencioso e vendedor',
                'workingHours': 'Segunda a Sábado: 9h às 18h',
                'paymentMethods': 'PIX, Cartão de crédito, Cartão de débito, Dinheiro',
                'services': 'Produtos variados, Atendimento personalizado, Promoções especiais'
            }
            updates.update(template_updates)
            
            for key, value in template_updates.items():
                setattr(self.agent_data, key, value)
            
            saved_something = True
            print("    ✅ TEMPLATE LOJA APLICADO")
        
        elif (('oficina' in text or 'mecânica' in text) and not self.agent_data.businessType):
            print("    🔧 Aplicando TEMPLATE OFICINA...")
            template_updates = {
                'businessType': 'oficina',
                'personality': 'técnico, confiável e profissional',
                'workingHours': 'Segunda a Sexta: 8h às 18h, Sábado: 8h às 12h',
                'paymentMethods': 'PIX, Cartão de crédito, Cartão de débito, Dinheiro',
                'services': 'Revisão geral, Troca de óleo, Freios, Suspensão, Diagnóstico'
            }
            updates.update(template_updates)
            
            for key, value in template_updates.items():
                setattr(self.agent_data, key, value)
            
            saved_something = True
            print("    ✅ TEMPLATE OFICINA APLICADO")
        
        # DETECÇÃO DE NOME (DEPOIS do template para não sobrescrever)
        if (not self.agent_data.businessName or 
            len(self.agent_data.businessName) < 3 or 
            "nome do seu" in self.agent_data.businessName.lower()):
            
            print("    🔍 Procurando NOME...")
            nome_detectado = self.detectar_nome_inteligente(content)
            
            if nome_detectado and 3 <= len(nome_detectado) <= 50:
                updates['businessName'] = nome_detectado
                self.agent_data.businessName = nome_detectado
                saved_something = True
                print(f"    ✅ NOME SALVO: '{nome_detectado}'")
        else:
            print("    ✅ Nome já existe, pulando")
        
        # DETECÇÃO DE TELEFONE
        if (not self.agent_data.contactPhone or 
            "xxxxx" in self.agent_data.contactPhone or 
            len(self.agent_data.contactPhone) < 10):
            
            print("    🔍 Procurando TELEFONE...")
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
                    print(f"    🎯 Candidato telefone: '{telefone}'")
                    
                    if 10 <= len(telefone) <= 11 and telefone != '11987654321':
                        updates['contactPhone'] = telefone
                        self.agent_data.contactPhone = telefone
                        saved_something = True
                        print(f"    ✅ TELEFONE SALVO: '{telefone}'")
                        break
                if 'contactPhone' in updates:
                    break
        else:
            print("    ✅ Telefone já existe, pulando")
        
        # DETECÇÃO DE ENDEREÇO
        if (not self.agent_data.location or 
            "ser definido" in self.agent_data.location.lower() or 
            len(self.agent_data.location) < 5):
            
            print("    🔍 Procurando ENDEREÇO...")
            endereco_patterns = [
                r'(?:endereço|localizado|fica|situado|rua|avenida|av\.?)\s+([^.,!?\n]{8,80})',
                r'(?:^|\s)((?:rua|avenida|av\.?|r\.?)\s+[^.,!?\n]{5,50})'
            ]
            
            for pattern in endereco_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    endereco = match.group(1).strip()
                    if 5 < len(endereco) < 80:
                        updates['location'] = endereco
                        self.agent_data.location = endereco
                        saved_something = True
                        print(f"    ✅ ENDEREÇO SALVO: '{endereco}'")
                        break
                if 'location' in updates:
                    break
        else:
            print("    ✅ Endereço já existe, pulando")
        
        # DETECÇÃO DE SERVIÇOS/CARDÁPIO
        if (not self.agent_data.services or 
            "será criada" in self.agent_data.services.lower() or 
            "ser definido" in self.agent_data.services.lower()):
            
            print("    🔍 Procurando SERVIÇOS...")
            
            # Detectar número de itens
            match = re.search(r'(\d+)\s*(?:sabores?|opções?|tipos?|pizzas?|pratos?|itens?)', content, re.IGNORECASE)
            if match:
                numero = match.group(1)
                updates['services'] = f"Cardápio com {numero} opções. Delivery, Balcão, Reservas disponíveis"
                self.agent_data.services = updates['services']
                saved_something = True
                print(f"    ✅ SERVIÇOS SALVOS: '{numero} opções'")
        else:
            print("    ✅ Serviços já existem, pulando")
        
        print(f"  💾 SALVOU ALGO: {saved_something}")
        print(f"  🔄 UPDATES: {list(updates.keys())}")
        
        return {
            'updates': updates,
            'saved_something': saved_something
        }

    def gerar_proxima_pergunta(self) -> str:
        """Gera a próxima pergunta baseada no que está faltando"""
        percentage, missing = self.agent_data.get_completion_status()
        
        if percentage == 100:
            return "🎉 Perfeito! Seu funcionário IA está 100% configurado!"
        
        # Priorizar perguntas essenciais
        if "NOME" in missing:
            return "Qual é o nome do seu negócio?"
        elif "TELEFONE" in missing:
            return f"✅ Nome '{self.agent_data.businessName}' salvo! Qual é o telefone?"
        elif "ENDEREÇO" in missing:
            return f"✅ Telefone salvo! Qual é o endereço do {self.agent_data.businessName}?"
        elif "SERVIÇOS" in missing:
            if self.agent_data.businessType == "restaurante":
                return "✅ Endereço salvo! Quantos sabores de pizza vocês têm?"
            elif self.agent_data.businessType == "loja":
                return "✅ Endereço salvo! Que tipos de produtos vocês vendem?"
            elif self.agent_data.businessType == "oficina":
                return "✅ Endereço salvo! Que serviços a oficina oferece?"
            else:
                return "✅ Endereço salvo! Que serviços vocês oferecem?"
        else:
            return f"Configuração {percentage}% completa! Faltam: {', '.join(missing)}"

    def simular_conversa(self, mensagens_usuario: List[str]) -> None:
        """Simula uma conversa completa"""
        print(f"\n{'='*80}")
        print("🎭 SIMULAÇÃO DE CONVERSA COMPLETA")
        print(f"{'='*80}")
        
        for i, mensagem in enumerate(mensagens_usuario):
            print(f"\n📝 TURNO {i+1}")
            print(f"👤 USUÁRIO: '{mensagem}'")
            
            # Analisar mensagem do usuário
            resultado = self.analisar_e_atualizar(mensagem)
            
            # Verificar status atual
            percentage, missing = self.agent_data.get_completion_status()
            print(f"📊 STATUS: {percentage}% completo - Faltam: {missing}")
            
            # Gerar próxima pergunta da IA
            proxima_pergunta = self.gerar_proxima_pergunta()
            print(f"🤖 IA: {proxima_pergunta}")
            
            print(f"📋 ESTADO ATUAL:")
            estado = self.agent_data.to_dict()
            for key, value in estado.items():
                print(f"  {key}: '{value}'")
            
            if percentage == 100:
                print("\n🎉 CONFIGURAÇÃO COMPLETA!")
                break

def teste_fluxo_restaurante():
    """Teste completo: configurar um restaurante"""
    print("TESTE: CONFIGURAR RESTAURANTE COMPLETO")
    
    simulator = FuncionarioIASimulator()
    
    mensagens = [
        "tenho um restaurante do amor",  # Nome + Template
        "o telefone é 11987654322",     # Telefone
        "fica na rua das flores 123",   # Endereço  
        "temos 50 sabores de pizza"     # Serviços
    ]
    
    simulator.simular_conversa(mensagens)
    return simulator.agent_data

def teste_fluxo_loja():
    """Teste completo: configurar uma loja"""
    print("\nTESTE: CONFIGURAR LOJA COMPLETA")
    
    simulator = FuncionarioIASimulator()
    
    mensagens = [
        "tenho uma loja de roupas",      # Template
        "o nome é Moda Legal",           # Nome (corrigido)
        "telefone 11888777666",          # Telefone
        "avenida brasil 500",            # Endereço
        "vendemos roupas femininas"      # Serviços
    ]
    
    simulator.simular_conversa(mensagens)
    return simulator.agent_data

def teste_fluxo_oficina():
    """Teste completo: configurar uma oficina"""
    print("\nTESTE: CONFIGURAR OFICINA COMPLETA")
    
    simulator = FuncionarioIASimulator()
    
    mensagens = [
        "oficina mecânica",              # Template
        "se chama Auto Center Silva",    # Nome (corrigido)
        "contato 11777888999",           # Telefone
        "rua são joão 200",              # Endereço
        "fazemos revisão completa"       # Serviços adicional
    ]
    
    simulator.simular_conversa(mensagens)
    return simulator.agent_data

if __name__ == "__main__":
    print("TESTE FLUXO COMPLETO - FUNCIONARIO IA")
    print("Simulando conversacoes completas ate 100%")
    
    # Testar todos os fluxos
    restaurante = teste_fluxo_restaurante()
    loja = teste_fluxo_loja()
    oficina = teste_fluxo_oficina()
    
    print(f"\n{'='*80}")
    print("RESUMO DOS TESTES")
    print(f"{'='*80}")
    
    # Resumo restaurante
    perc_rest, missing_rest = restaurante.get_completion_status()
    print(f"RESTAURANTE: {perc_rest}% completo - {restaurante.businessName}")
    
    # Resumo loja  
    perc_loja, missing_loja = loja.get_completion_status()
    print(f"LOJA: {perc_loja}% completo - {loja.businessName}")
    
    # Resumo oficina
    perc_ofic, missing_ofic = oficina.get_completion_status()
    print(f"OFICINA: {perc_ofic}% completo - {oficina.businessName}")
    
    print(f"\nTODOS OS TESTES CONCLUIDOS!") 